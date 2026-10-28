#!/usr/bin/env python3
"""账本校验器：TPM 每次改完账本，保存或提交前必须跑一遍。

适用于两种账本：
- mode: team     —— 公司 AI 用（见 07-公司AI实施手册.md），规则更严
- mode: personal —— 一个人管自己的事项（owner 写 me）

用法：
    python3 -I ledger_check.py <账本.yaml>
退出码：0 = 通过；1 = 有错误（逐条打印）。

【这个校验器管什么】只管账本的**结构**：字段齐不齐、取值合不合法、编号重不重复、
时间格式对不对、团队模式必需的配置在不在、身份对照表能不能对上。

【它不管什么】它只看「现在这一份」账本，所以**不能**证明：
- 回复的人真的有权批准（要在运行时按平台账号 ID 核对）
- 阶段批准是真的（它只检查记录的格式）
- 批准仍然有效、对应的是当前版本
- 受众安全、消息没有重复发送
- 事项真的完成了（它只检查有没有写证据）
这些都必须在 TPM 的运行流程里检查，见 07 手册第 5.4 节。

校验不通过时：不要靠删历史、编造批准或证据来让它通过。保留上一份有效账本，本轮不保存、不发消息，把错误报告给流程负责人。
"""
import datetime as dt
import os
import re
import sys
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

import yaml


class UniqueKeyLoader(yaml.SafeLoader):
    """同一层出现重复的键（例如写了两个 items:）时直接报错，而不是悄悄用后一个覆盖前一个。"""

    def construct_mapping(self, node, deep=False):
        keys = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in keys:
                raise yaml.constructor.ConstructorError(
                    None, None, f"重复的键 {key!r}（第 {key_node.start_mark.line + 1} 行）", key_node.start_mark)
            keys.add(key)
        return super().construct_mapping(node, deep=deep)


REQUIRED = ["id", "revision", "title", "kind", "owner", "resource_id", "status",
            "next_action", "done_when", "closes_by"]

COMMON_STATUS = {"open", "blocked", "in_progress", "verifying", "done", "deferred", "paused", "dropped"}
RULES = {
    "team": {
        "phases": {"not_enabled", "shadow", "confirm", "auto"},
        "status": COMMON_STATUS | {"awaiting_decision"},
        "waiting": {"awaiting_decision"},
        "closes_by": {"tpm", "owner", "approver"},
        "privacy": {"normal"},          # 第一期不接入受限来源，见 07 手册 9.3
        "owner_re": re.compile(r"^(tpm|person:.+|agent:.+|external:.+)$"),
        "blocked_reason": {"awaiting_decision", "awaiting_owner", "awaiting_external", "dependency", "unknown"},
    },
    "personal": {
        "phases": {"not_enabled", "phase0", "phase1", "phase2"},
        "status": COMMON_STATUS | {"awaiting_me"},
        "waiting": {"awaiting_me"},
        "closes_by": {"tpm", "me"},
        "privacy": {"normal", "local-only"},
        "owner_re": re.compile(r"^(me|tpm|agent:.+|session:.+|external:.+)$"),
        "blocked_reason": {"awaiting_me", "awaiting_worker", "awaiting_external", "dependency", "unknown"},
    },
}
KINDS = {"commitment", "decision", "watch", "anomaly", "goal"}
REMINDER_STAGES = {"none", "first", "escalated", "final_asked", "stopped"}
TIME_FIELDS = ["waiting_since", "next_check", "worker_ack_at", "last_observed_at", "last_notified_at",
               "last_reminded_at", "last_verified_at", "approval_expires_at", "first_seen_at",
               "final_ask_at", "decision_expires_at"]
ID_RE = re.compile(r"^L-\d{8}-\d{2,}$")
DECISION_RE = re.compile(r"^D(\d+)$")
LOCAL_ONLY_MAX = 40


def parse_time(value):
    if isinstance(value, dt.datetime):
        return value if value.tzinfo else None
    if not isinstance(value, str):
        return None
    try:
        parsed = dt.datetime.fromisoformat(value)
    except ValueError:
        return None
    return parsed if parsed.tzinfo else None


def is_pos_int(value):
    return isinstance(value, int) and not isinstance(value, bool) and value >= 1


def nonempty_str(value):
    return isinstance(value, str) and value.strip() != ""


def check_team_config(doc, errors):
    """团队模式必需的顶层配置。返回 people 对照表（用于后续核对）。"""
    tz = doc.get("timezone")
    tz_ok = False
    if isinstance(tz, str) and tz:
        try:
            ZoneInfo(tz)
            tz_ok = True
        except (ZoneInfoNotFoundError, ValueError):
            pass
    if not tz_ok:
        errors.append(f"timezone={tz!r} 不是有效的 IANA 时区名（例如 America/New_York）")
    if not isinstance(doc.get("workdays"), list) or not doc["workdays"]:
        errors.append("缺少 workdays（哪几天算工作日，例如 [Mon, Tue, Wed, Thu, Fri]）")
    if not isinstance(doc.get("holidays"), list):
        errors.append("缺少 holidays（放假日期列表；没有就写 []）")
    if not isinstance(doc.get("do_not_remind"), list):
        errors.append("缺少 do_not_remind（说过「别再提醒我」的人；没有就写 []）")

    people = doc.get("people")
    if not isinstance(people, dict) or not people:
        errors.append("缺少 people（person:<名> → {平台: 账号ID} 的对照表，用来核对回复者身份）")
        people = {}
    seen_accounts = {}
    for name, accounts in people.items():
        if not str(name).startswith("person:") or not isinstance(accounts, dict) or not accounts:
            errors.append(f"people 里的 {name!r} 格式不对，应为 person:<名>: {{<平台>: <账号ID>}}")
            continue
        for platform, account in accounts.items():
            if not nonempty_str(str(account)) or str(account) in ("", "None"):
                errors.append(f"people.{name}.{platform} 的账号 ID 是空的")
            key = (platform, str(account))
            if key in seen_accounts:
                errors.append(f"{platform} 账号 {account} 同时对应 {seen_accounts[key]} 和 {name}")
            seen_accounts[key] = name

    owner = doc.get("process_owner")
    if owner not in people:
        errors.append(f"process_owner={owner!r} 必须是 people 里的人")
    approvers = doc.get("approvers")
    if not isinstance(approvers, dict) or not approvers:
        errors.append("缺少 approvers（审批类别 → 能批的人，例如 design_review: [person:Mei]）")
        approvers = {}
    for category, names in approvers.items():
        if not isinstance(names, list) or not names:
            errors.append(f"approvers.{category} 必须是非空列表")
            continue
        for name in names:
            if name not in people:
                errors.append(f"approvers.{category} 里的 {name} 不在 people 里")

    phase = doc.get("phase")
    if phase not in (None, "not_enabled"):
        ref = doc.get("phase_approval_ref")
        if not isinstance(ref, dict):
            errors.append("phase 不是 not_enabled 时，phase_approval_ref 必须是一个记录："
                          "{by: <流程负责人>, account_id: <他的平台账号>, message: <原始消息链接>, phase: <批准的阶段>, scope: <批准的范围>, at: <时间>}")
        else:
            for field in ("by", "account_id", "message", "phase", "scope", "at"):
                if not ref.get(field):
                    errors.append(f"phase_approval_ref 缺少 {field}")
            if ref.get("by") and ref.get("by") != owner:
                errors.append("phase_approval_ref.by 必须是流程负责人本人")
            if ref.get("phase") and ref.get("phase") != phase:
                errors.append(f"phase_approval_ref 批准的是 {ref.get('phase')}，和当前 phase={phase} 不一致")
            if ref.get("by") in people and ref.get("account_id") and \
                    str(ref.get("account_id")) not in {str(v) for v in people[ref["by"]].values()}:
                errors.append("phase_approval_ref.account_id 和 people 对照表里流程负责人的账号对不上")
            if ref.get("at") is not None and parse_time(ref.get("at")) is None:
                errors.append("phase_approval_ref.at 必须是带时区的 ISO 8601")
    return people, approvers


def check_item(item, where, mode, rules, people, approvers, allowed_resources, errors):
    for field in REQUIRED:
        if item.get(field) in (None, ""):
            errors.append(f"{where}: 缺少必填字段 {field}")
    if item.get("id") is not None and not ID_RE.match(str(item["id"])):
        errors.append(f"{where}: id 格式应为 L-YYYYMMDD-NN")
    if not is_pos_int(item.get("revision")):
        errors.append(f"{where}: revision 必须是 >=1 的整数")

    enum_checks = {"kind": KINDS, "status": rules["status"], "closes_by": rules["closes_by"],
                   "blocked_reason": rules["blocked_reason"], "privacy": rules["privacy"],
                   "reminder_stage": REMINDER_STAGES}
    for field, allowed in enum_checks.items():
        value = item.get(field)
        if value is not None and (not isinstance(value, str) or value not in allowed):
            errors.append(f"{where}: {field}={value!r} 不合法（{mode} 模式只能是 {sorted(allowed)}）")
    res = item.get("resource_id")
    if res is not None and (not isinstance(res, str) or res not in allowed_resources):
        errors.append(f"{where}: resource_id={res!r} 不在顶层 resources 列表里（或写 none）")
    owner = item.get("owner")
    if owner is not None and not rules["owner_re"].match(str(owner)):
        errors.append(f"{where}: owner={owner!r} 格式不对（{mode} 模式）")
    if mode == "team" and isinstance(owner, str) and owner.startswith("person:") and owner not in people:
        errors.append(f"{where}: owner {owner} 不在 people 对照表里")
    for field in TIME_FIELDS:
        if item.get(field) is not None and parse_time(item[field]) is None:
            errors.append(f"{where}: {field} 必须是带时区的 ISO 8601，例如 2026-10-28T09:00:00-04:00")

    status, kind = item.get("status"), item.get("kind")
    waiting = status in rules["waiting"]

    # —— 决定 ——
    if kind == "decision":
        if mode == "team":
            for field in ("decision_id", "approver", "approval_type", "options", "decision_expires_at"):
                if not item.get(field):
                    errors.append(f"{where}: 团队模式的 decision 必须有 {field}")
            if item.get("approver") and item.get("approver") not in people:
                errors.append(f"{where}: approver {item.get('approver')} 不在 people 里")
            cat = item.get("approval_type")
            if cat and item.get("approver") and item.get("approver") not in (approvers.get(cat) or []):
                errors.append(f"{where}: {item.get('approver')} 不在 approvers.{cat} 名单里，无权审批这类事")
        elif waiting and item.get("privacy") != "local-only" and not item.get("decision_id"):
            errors.append(f"{where}: 等待回答的 decision 必须有 decision_id")
        opts = item.get("options")
        if item.get("privacy") != "local-only" and (waiting or mode == "team"):
            if not isinstance(opts, dict) or len(opts) < 2:
                errors.append(f"{where}: decision 必须保存 options（至少两个选项），就是发出去的那一版")

    # —— 等待 ——
    if waiting and not item.get("waiting_since") and item.get("waiting_since_unknown") is not True:
        errors.append(f"{where}: 等待中的事项要么写 waiting_since，要么写 waiting_since_unknown: true（不要编造时间）")
    # —— 延期 ——
    if status == "deferred":
        if not item.get("next_check"):
            errors.append(f"{where}: status=deferred 必须有 next_check（具体到时间和时区）")
        if not item.get("resume_status") or item.get("resume_status") not in rules["status"] - {"deferred", "done", "dropped"}:
            errors.append(f"{where}: status=deferred 必须有 resume_status（到期后恢复成什么状态）")
    # —— 关闭 ——
    if status in ("done", "dropped") and not item.get("evidence"):
        errors.append(f"{where}: status={status} 必须有 evidence（证据链接，或谁在何时取消的原话链接）")
    # —— 异常 ——
    if kind == "anomaly":
        if not item.get("anomaly_key"):
            errors.append(f"{where}: kind=anomaly 必须有 anomaly_key")
        if mode == "team" and not item.get("first_seen_at"):
            errors.append(f"{where}: kind=anomaly 必须有 first_seen_at（这一次首次发现的时间）")
    # —— 批准引用 ——
    if mode == "team" and item.get("authorization_ref"):
        ref = item["authorization_ref"]
        if not isinstance(ref, dict) or not all(ref.get(f) for f in ("decision_id", "choice", "by", "account_id", "message", "at")):
            errors.append(f"{where}: authorization_ref 必须是记录 {{decision_id, choice, by, account_id, message, at}}")
        if not item.get("approval_expires_at"):
            errors.append(f"{where}: 有 authorization_ref 就必须有 approval_expires_at（批准有效期）")
    # —— 个人版的本地专用事项 ——
    if item.get("privacy") == "local-only":
        for field in ("options", "notes"):
            if field in item:
                errors.append(f"{where}: local-only 事项不能有 {field}，只记占位标题")
        for field in ("title", "next_action", "done_when", "evidence", "source"):
            if isinstance(item.get(field), str) and len(item[field]) > LOCAL_ONLY_MAX:
                errors.append(f"{where}: local-only 事项的 {field} 超过 {LOCAL_ONLY_MAX} 字，只能写占位文字")


def check(doc):
    errors = []
    if not isinstance(doc, dict) or not isinstance(doc.get("items"), list):
        return ["顶层必须是一个 mapping，并且有 items: 列表"]
    mode = doc.get("mode")
    if mode not in RULES:
        return ["顶层缺少 mode（只能是 team 或 personal）"]
    rules = RULES[mode]
    if doc.get("phase") not in rules["phases"]:
        errors.append(f"phase={doc.get('phase')!r} 不合法（{mode} 模式只能是 {sorted(rules['phases'])}；没启用就写 not_enabled）")
    next_d = doc.get("next_decision_id")
    if not is_pos_int(next_d):
        errors.append("缺少 next_decision_id（正整数）")
        next_d = None
    resources = doc.get("resources")
    if not isinstance(resources, list) or not all(isinstance(r, str) for r in resources):
        errors.append("缺少 resources（字符串列表；没有就写 []）")
        resources = []
    allowed_resources = set(resources) | {"none"}

    people, approvers = ({}, {})
    if mode == "team":
        people, approvers = check_team_config(doc, errors)

    seen_ids, seen_d, max_d, open_anomaly_keys = set(), set(), 0, set()
    for idx, item in enumerate(doc["items"]):
        if not isinstance(item, dict):
            errors.append(f"items[{idx}]: 必须是 mapping")
            continue
        where = f"items[{idx}] {item.get('id', '?')}"
        check_item(item, where, mode, rules, people, approvers, allowed_resources, errors)
        item_id = str(item.get("id"))
        if item_id in seen_ids:
            errors.append(f"{where}: id 重复")
        seen_ids.add(item_id)
        d = item.get("decision_id")
        if d is not None:
            m = DECISION_RE.match(str(d))
            if not m:
                errors.append(f"{where}: decision_id 格式应为 D<数字>")
            else:
                if str(d) in seen_d:
                    errors.append(f"{where}: decision_id {d} 重复（编号永不复用）")
                seen_d.add(str(d))
                max_d = max(max_d, int(m.group(1)))
        if item.get("kind") == "anomaly" and item.get("anomaly_key") and item.get("status") not in ("done", "dropped"):
            if item["anomaly_key"] in open_anomaly_keys:
                errors.append(f"{where}: 有两条未关闭的异常用了同一个 anomaly_key {item['anomaly_key']!r}")
            open_anomaly_keys.add(item["anomaly_key"])
    if next_d is not None and next_d <= max_d:
        errors.append(f"next_decision_id={next_d} 必须大于已用的最大编号 D{max_d}")
    if "someday" in doc and not isinstance(doc["someday"], list):
        errors.append("someday 必须是列表")
    return errors


def main():
    if len(sys.argv) < 2:
        print("用法：python3 -I ledger_check.py <账本.yaml>")
        return 1
    path = os.path.expanduser(sys.argv[1])
    try:
        with open(path, encoding="utf-8") as fh:
            doc = yaml.load(fh, Loader=UniqueKeyLoader)
    except (OSError, yaml.YAMLError) as exc:
        print(f"✗ 读不了或解析不了 {path}：{exc}")
        return 1
    try:
        errors = check(doc)
    except Exception as exc:  # 校验器自己出错也要给出可读的提示，而不是崩溃
        print(f"✗ 校验器无法处理这个账本（{type(exc).__name__}: {exc}），请检查字段类型是否写成了列表或嵌套结构")
        return 1
    for err in errors:
        print("✗", err)
    if errors:
        print(f"共 {len(errors)} 处错误。不要靠删历史、编造批准或证据来修；改对了再跑，通过之前不要保存或发消息。")
        return 1
    print(f"✓ 结构校验通过：mode={doc['mode']}，phase={doc.get('phase')}，{len(doc['items'])} 条事项，"
          f"next_decision_id={doc['next_decision_id']}（注意：这不代表批准有效或事项真的完成，见文件开头说明）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
