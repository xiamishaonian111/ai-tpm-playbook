**主动型 / ambient / always-on agent 产品与平台调研**  
**资料截止：2026-10-27**

核心判断：用户 描述的四个名字，最可能是 **Meta Muse、OpenAI dots、Grok Bot、Claude Duet**，而且都有 2026 年官方公告。它们代表的新方向，是让 AI 持续接收信息、维护上下文、推进工作，并判断何时需要人类介入。不过，“能主动发消息”与“能可靠承担 TPM 职责”之间仍有距离。

本报告仅使用公开资料，未读取本机凭据。产品能力以官方声明为主，不代表独立实测。文中编号对应末尾完整来源；**D 表示网页未标明确发布日期，统一于 2026-10-27 查阅**。价格为公开页面信息，地区、账户和管理员配置可能影响实际可用性。

**一、四个口述名称的辨认**

| 口述 | 最可能对应 | 判断与候选 |
|---|---|---|
| 「Muse 的系统」 | **Meta Muse**，高置信 | Meta 于 **2026-09-08** 发布同名 personal agent，具备持续工作、记忆、主动建议和审批机制。Manus 是音近候选，但证据弱于同名官方产品。[1](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) |
| 「GPT 的 Dot」 | **OpenAI dots**，高置信 | **2026-09-29** 发布；官方明确称 always-on agents，可主动汇报并管理 Codex 等任务。Pulse 是旧功能候选；New Computer 的 Dot 厂商不同，且已宣布关停。[2](https://openai.com/index/introducing-dots/) [6](https://new.computer/) |
| 「GroupBot」 | **Grok Bot**，高置信 | **2026-08-11** 发布，支持多个 Bot 协作、chief of staff 管理其他 Bot，以及对停滞交接主动 follow up。“GroupBot”作为本次所指的准确产品名，**未核实**。[3](https://x.ai/news/introducing-grok-bot) |
| 「CloudDoIt」 | **Claude Duet**，高置信 | **2026-10-21** 发布，发音吻合；官方定位正是主动找用户、跟踪工作、晨间 briefing。“CloudDoIt”准确产品名**未核实**。[4](https://claude.com/resources/articles/claude-duet) |

还有一条交叉证据：**2026-10-22** 的《AI 懒人报》节目标题恰好并列 Claude Duet、Grok Bot、Muse、dots，其公开文字稿甚至将 Claude Duet 转写成“Cloud Do It”。这显著提高了上述组合的可信度，但不能证明 用户 听到的就是该节目。[5](https://www.podscan.fm/podcasts/ai-lan-ren-bao-1/episodes/ep441-claude-duet-wan-zheng-jie-xi-hui-xian-lai-zhao-ni-de-claude-gen-grok-botmusedots-cha-zai-na-1)

**二、产品能力对照**

“记忆与状态”列描述公开可见的保存位置和上下文边界；未公开的底层数据库、保留期限及跨任务记忆，不作推测。

先看最接近“持续在岗员工”的四款新品。

| 产品 | 触发方式 | 记忆与状态 | 主动 follow up / 汇报 | 人类审批 | 适用与价格／可用性 |
|---|---|---|---|---|---|
| **Muse** [1](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/) | 用户交办、目标持续推进、变化检测；底层周期未公开 | 专属 Muse Secure VM，保存数据及个人上下文 | Muse app、WhatsApp；变化或需要审批时回来找用户 | 发邮件、购买等敏感动作确认；独立 Sentinel 检查外发 | 个人；美国推出，基础免费、有付费扩容 |
| **dots** [2](https://openai.com/index/introducing-dots/) | 用户交办、后台 proactive research、持续任务 | 云端电脑、跨渠道上下文、反馈与自用笔记 | ChatGPT、Slack、Teams；进度、问题、待决策消息 | Custom Rules＋auto-review；后台 proactive research 工具限制为只读 | 个人及企业；合资格 Pro、Business Premium，Enterprise beta；首个 dot 随方案包含 |
| **Grok Bot** [3](https://x.ai/news/introducing-grok-bot) | 用户交办、保存的 routines、主动跟进 | 云端电脑、对话、工作方法；Bot 间共享线程上下文 | 自有桌面／移动应用、群聊；可催停滞交接，由一个 Bot 协调其他 Bot | 需要判断或批准时找人；完整逐动作规则未公开 | 个人、小团队；beta，包含于指定 SuperGrok、Cursor 订阅，独立用量 |
| **Claude Duet** [4](https://claude.com/resources/articles/claude-duet) | 晨间 brief、每隔数小时检查连接账户、用户任务 | 云端 VM；继承 Claude memory、skills、connected apps；单一持续线程 | 独立 app、网页、手机通知；完成、阻塞或需判断时汇报 | 发消息、付款、签署、删除前确认；部分操作即使批准也不执行 | 专业人士、小企业；美国 Pro／Max 候补研究预览，共享 Claude 用量 |

以下产品更偏向“明确配置后持续执行”，其中部分已经加入监控和事件触发。

| 产品 | 触发方式 | 记忆与状态 | 汇报渠道 | 人类审批 | 适用与价格／可用性 |
|---|---|---|---|---|---|
| **ChatGPT Pulse** [7](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) | 历史上每日异步研究 | chats、memory、反馈 | 个性化卡片 | 主要提供信息 | 原 Pro 功能；**2026-06-17 宣布正在 sunset**，主动更新转入 scheduled tasks |
| **ChatGPT Tasks / scheduled tasks** [8](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt) | 一次性、定时、monitoring、受支持 app 事件 | 保存的任务、对话及历史运行信息 | Scheduled、推送；连接工具中的动作依权限 | 需审批的外部写入会暂停 | 个人；合资格免费／付费账户；事件任务需 Work 及合资格付费方案 |
| **ChatGPT agent / Work** [9](https://openai.com/index/introducing-chatgpt-agent/) | agent 原为用户交办；Work 加入定时、事件及监控 | 任务会话、文件、连接工具；云端或桌面执行边界不同 | 任务进度、完成通知、审批请求 | 重要动作审批、可中断或接管 | 个人、团队；Work 于 **2026-07-09** 推出，按账户分批开放；不能假定旧 agent 功能全部一一对应 |
| **Codex Automations / cloud tasks** [10](https://openai.com/index/introducing-the-codex-app/) [11](https://learn.chatgpt.com/docs/automations) | 定时、同线程唤醒；cloud task 是执行载体，不能自动等同持续监控 | 本地项目／worktree、线程；云任务使用可访问的文件和工具 | 初始设计为 review queue；现可在 Scheduled 和线程查看 | 使用 sandbox、rules 和组织策略；无人值守不保证逐步询问 | 开发者、团队；本地任务需电脑和 app 在线，云任务不直接继承本机目录 |
| **OpenAI Agents API** [12](https://developers.openai.com/api/docs/guides/agents-api/sessions/automations) | 应用事件、cron；agent 可安排后续工作 | durable session，平台管理恢复与上下文压缩 | stream、webhook；消息渠道需应用接入 | 由应用的工具、审批和权限设计控制 | 开发平台；模型、工具、sandbox 分项计费 |
| **Claude Code cloud scheduled tasks，原 routines** [13](https://code.claude.com/docs/en/routines) | schedule、API、GitHub；可组合 | 云端任务配置、repo、connectors、运行会话；可依项目续线程 | History、PR、Slack 等 connector | 新云会话通常 auto mode；ask rules、重复阻止等情况仍会等待人 | Pro／Max／Team／Enterprise，研究预览，消耗订阅用量 |
| **Claude Code 本地调度、hooks、remote sessions** [14](https://code.claude.com/docs/en/scheduled-tasks) | `/loop` 定时或动态等待；hooks 响应生命周期事件 | 本地会话、项目文件；Remote Control 连接原本地会话 | terminal、hook 通知、网页／手机远程查看 | 沿用会话权限；hook 自身是确定性代码 | 开发者；本地进程必须存活。Remote Control 本身不是调度器 |
| **Claude Cowork / Dispatch** [17](https://claude.com/blog/cowork-web-mobile/) [18](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) | 用户交办、定时；Dispatch 是远程交办入口 | 新云会话和文件在 Claude 账户；每次 scheduled run 是独立会话 | Scheduled、跨设备会话、手机审批 | 可选 approval mode | 个人及团队；新云任务可离线运行；旧 Dispatch 桌面模式仍须电脑在线，现仅部分既有用户 beta |
| **OpenClaw** [21](https://docs.openclaw.ai/automation) | cron／Automations、事件、hooks、proactive check | 自托管状态库、job scratch；Markdown memory 与检索索引 | 配置的 Telegram、Slack、WhatsApp 等渠道 | exec/tool 策略、渠道审批，需自行配置 | 个人、自托管团队；模型和运维另计 |
| **Manus** [23](https://manus.im/blog/manus-schedules) | 用户任务、scheduled tasks、应用内 scheduled actions | 可续同一 task；Projects 共享文件、skills、connectors | 任务界面；Slack 集成可回传结果和文件 | 支持 Skip confirmations，开启后部分发送／发布不再询问 | 个人、团队；credits 制，当前完整标价未核实 |
| **Devin** [24](https://docs.devin.ai/product-guides/automations) | schedule、Slack、GitHub、Linear、webhook；persistent triage | 云会话；个人 Memory 为持久 Git Markdown notes，组织方法用 Skills | Slack、issue、PR；可新建或续已有 session | PR review；其他动作依 security profile，非统一人工确认 | 工程团队；ACU、频率和网络策略可限额，当前基础价格未核实 |
| **Google Jules** [25](https://blog.google/innovation-and-ai/technology/developers-tools/jules-proactive-updates/) | 用户任务、Scheduled Tasks、Suggested Tasks、部署失败事件 | repo、云端任务环境；跨任务个人长期记忆未核实 | 建议、修复 PR、任务结果 | 建议可接受／拒绝，修复 PR 人工 review | 开发者；定时及 Render 集成发布时面向所有用户，Suggested Tasks 面向 AI Pro／Ultra |
| **Gemini scheduled actions** [26](https://support.google.com/gemini/answer/16316416?hl=en) | 一次性／周期时间触发 | Google 账户、任务对话、connected apps；要求 Keep Activity | Gemini 未读对话、手机通知 | 用户确认任务和 app 接入；逐动作审批覆盖未核实 | 个人及合资格 Workspace；正向个人账户扩大开放，最多 10 个 active actions |

团队平台更擅长把责任、状态和共享上下文留在工作系统里。

| 产品 | 触发方式 | 记忆与状态 | 汇报渠道 | 人类审批 | 适用与价格／可用性 |
|---|---|---|---|---|---|
| **Microsoft Agent 365** [27](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) | 治理控制平面，本身不是任务执行 agent | agent 身份、权限、监控与治理信息 | 管理与安全控制面 | 身份、策略、访问治理 | 企业；**2026-05-01 GA**；公告价 $15／用户／月 |
| **Copilot Researcher** [28](https://www.microsoft.com/en-us/microsoft-365/blog/2025/03/25/introducing-researcher-and-analyst-in-microsoft-365-copilot/) | 主要用户触发，多步骤研究；原生持续催办未核实 | M365 工作数据、connectors、研究会话 | Copilot 研究输出 | 继承数据权限，结果供人审阅 | 团队；M365 Copilot 体系，不能把深度研究直接视为 TPM |
| **Facilitator / Channel Agent** [29](https://learn.microsoft.com/en-us/microsoftteams/copilot-ai-agents-overview) | 会议、频道活动、用户请求 | Teams 对话、会议记录、协作内容 | 共享笔记、状态摘要、任务与截止日期 | 组织／会议设置；具体动作依产品权限 | 团队；许可证及管理员配置决定可用性 |
| **Planner Agent，原 Project Manager Agent** [30](https://support.microsoft.com/en-au/planner/whats-new-in-microsoft-planner) | 分配任务、目标生成、状态报告 | Planner plans、tasks；报告存于 Loop／SharePoint | Planner、Teams、状态报告与邮件分享 | Copilot 中生成的计划／更新先以 draft 审阅 | 团队；需要 Copilot license，部分功能需 Planner premium |
| **Asana AI Teammates / Dash** [31](https://asana.com/product/ai/ai-teammates) | 分派、工作流；AI Studio 承接结构化自动化 | Work Graph、共享项目记忆 | subtasks、comments、状态／风险；Dash 提示需要注意的工作 | checkpoints、scoped permissions、审计与 spend controls | 团队；当前页面称付费 plans 包含 Teammates，按 AI requests 使用 |
| **Linear Agent / Loops** [32](https://linear.app/docs/loops) | 用户、定时、Linear／Slack／GitHub 事件 | workspace issues、projects、docs、运行记录 | Slack digest、issue、更新文档、派发 coding session | connector 可逐工具审批或自动批准 | 产品／工程团队；当前文档列付费 plans＋AI credits |
| **Notion Agent / Custom Agents** [33](https://www.notion.com/releases/2026-02-24) | 普通 Agent 交互；Custom Agents 定时／事件 | Notion pages、databases、agent instructions、连接来源 | Notion、Slack、项目报告 | agent 级访问控制、运行日志；部分连接动作需确认 | 团队；Custom Agents 用 Business／Enterprise 附加 credits，$10／1,000 credits |
| **Slackbot / Slack 内 agents** [34](https://slack.com/help/articles/115004846068-Slack-updates-and-changes) | mention、scheduled tasks、Workflow Builder 触发 | workspace 内容、Slackbot memory；第三方 agent 另有状态 | DM、频道、canvas、Activity | Slackbot 写入／发送动作可要求批准；第三方各自实现 | 团队；按 Slack 方案与 rollout，不能假定安装 bot 即持续在岗 |
| **Lindy** [35](https://www.lindy.ai/pricing) | scheduled routines、消息交办、工作流 | persistent workspace context、meeting library、files | Slack、iMessage、brief、nudges、follow-up | built-in approvals | 个人／团队；本次打开页 $49.99／人／月、5,000 credits；缓存存在不同标价，最终结账价未核实 |

有三处版本变化尤其影响选型：

- **Cowork 已不再普遍依赖“电脑开着”**：2026-07-07 公告引入云端执行；当前帮助页明确，Pro／Max 在 **2026-10-06** 后的新任务默认云端，旧本地任务保留原位置。Dispatch 的旧桌面配对限制不能套用到全部 Cowork。[17](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- **OpenClaw 的旧 heartbeat 教程可能失效**：当前文档将监控迁为普通 Automations jobs；旧 `HEARTBEAT.md` 属迁移输入。自动从对话推断 commitments 的实验已在 **v2026.8.1** 移除，明确调度任务才有跟进保证。[21](https://docs.openclaw.ai/gateway/heartbeat)
- **Linear 已超出“被 @ 后做事”**：**2026-07-20** 推出 Loops，**2026-10-22** 增强 Slack／GitHub 触发。Notion 也在 **2026-10-13** 增加更丰富的共享 context 与 sub-agent 能力。[32](https://linear.app/changelog) [33](https://www.notion.com/releases)

**三、共同设计模式**

以下是基于上述产品的研究归纳，而非任何一家已完整实现的保证。

1. **触发器＋持久账本。** cron、heartbeat 和 webhook 只负责唤醒。真正的 follow up 还需要保存 owner、deadline、依赖、上次证据、下一次检查时间及停止条件。聊天记忆适合偏好，任务账本适合承诺；两者不能互相替代。
2. **事件优先，周期检查补漏。** PR 失败、部署告警、客户回复适合事件触发；无人回复和超期依赖需要周期检查。Devin、Claude Code、Linear 都已提供两种入口。
3. **briefing 与 escalation 分流。** 日常进展汇入每日 brief；只有阻塞、风险或待批准决策即时推送。Duet 的数小时检查、dots 的只读 proactive research，体现了成本与打扰之间的取舍。
4. **agent inbox 集中人类判断。** 将完成结果、待审批动作、阻塞问题放进统一队列，比不断发送“我正在做”更有价值。Codex review queue、Scheduled 页面和团队任务系统都在承担这一角色。
5. **协调者＋执行者。** Grok Bot、Asana Dash、Linear Loops 展示了协调层向专门执行者派工的方向。是否部署多个 agent，应取决于任务边界；增加角色数量不会自动增加可靠性。
6. **以证据关闭任务。** “命令成功”“服务 active”“agent 自报完成”都不足以证明目标达成。部署后的真实请求、业务指标、交付物和接收状态才构成闭环。

**四、失败案例与实际代价**

**权限失控已有真实漏洞。** OpenClaw 的 **CVE-2026-25253** 公告于 **2026-01-31** 发布：恶意链接可利用未经验证的 `gatewayUrl` 外传 gateway token，进一步修改策略并执行代码；影响版本为 ≤2026.1.28，2026.1.29 修复。仅绑定 loopback 也不能挡住浏览器充当桥梁的攻击。它是已披露漏洞，不能据此声称所有部署已被入侵。[36](https://github.com/advisories/GHSA-g8p2-7wf7-98mq)

**skill 市场增加供应链和 prompt injection 风险。** OpenClaw 于 **2026-02-07** 接入 VirusTotal 扫描，同时明确提醒：自然语言恶意指令未必触发病毒特征，“扫描干净”不等于安全。[37](https://openclaw.ai/blog/virustotal-partnership)

**“像员工”也可能意味着长期犯经营错误。** Anthropic 的 **2025-06-27 Project Vend** 实验记录了 AI 店主错误定价、被说服亏本出售商品和虚构现实行为。这不是 Duet 的产品事故，但说明持续运行和工具权限无法替代业务约束与结果评估。[38](https://www.anthropic.com/research/project-vend-1)

**后台成本和噪音会持续累积。** Duet 明确说明后台检查共享订阅额度；Notion 按阅读量、步骤和频率消耗 credits。OpenClaw 迁移文档还明确指出，旧 heartbeat 的特殊重复抑制被移除，迁移后可能重复投递。[4](https://claude.com/resources/articles/claude-duet) [33](https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents) [21](https://docs.openclaw.ai/gateway/heartbeat)

其他常见限制包括本机休眠、连接授权失效、模型退役、任务自动暂停，以及把旧上下文当成当前状态。Gemini 更明确提醒：scheduled response 会提前准备，交付时快速变化的数据可能已经过时。[26](https://support.google.com/gemini/answer/16316416?hl=en)

**对 用户 的研究判断**

最值得验证的是三层组合：**项目系统保存承诺，执行 agent 完成工作，协调层检查证据并升级阻塞**。现有的定时任务、报告流水线和机器人已具备部分触发与汇报基础，无须先整体替换。

产品试用可以围绕一个两周验收案例：部署后自动检查真实健康状态；异常时生成可审阅修复；依赖超时后催办；每天只汇报变化；需要 用户 决策时提供选项及后果。比较指标应是漏跟进率、误报率、任务关闭证据和总成本。公开资料尚不足以证明任何一款产品能稳定承担全部 TPM 责任，**这一效果未核实**。

**完整来源列表**

所有 D 来源均于 **2026-10-27** 查阅；发布日期未标时不以抓取日期代替。

1. Meta：[Introducing Muse](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)，**2026-09-08**，页面另列更新 **2026-09-30**。
2. OpenAI：[Introducing dots](https://openai.com/index/introducing-dots/)，**2026-09-29**。
3. Grok：[Introducing Grok Bot](https://x.ai/news/introducing-grok-bot)，**2026-08-11**。
4. Anthropic：[Introducing Claude Duet](https://claude.com/resources/articles/claude-duet)，**2026-10-21**，安全说明更新 **2026-10-23**。
5. AI 懒人报／Podscan：[EP441：Claude Duet、Grok Bot、Muse、dots](https://www.podscan.fm/podcasts/ai-lan-ren-bao-1/episodes/ep441-claude-duet-wan-zheng-jie-xi-hui-xian-lai-zhao-ni-de-claude-gen-grok-botmusedots-cha-zai-na-1)，**2026-10-22**；二手辨名线索。
6. New Computer：[An update on New Computer and Dot](https://new.computer/)，**D**；公告未明确标年月日。
7. OpenAI：[ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)，采用 **2026-06-17** Pulse sunset 条目。
8. OpenAI：[Scheduled tasks in ChatGPT](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)，**D**。
9. OpenAI：[Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)，**2025-07-17**；[Enterprise/Edu release notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)，Work 条目 **2026-07-09**。
10. OpenAI：[Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)，**2026-02-02**。
11. OpenAI：[Scheduled tasks 当前文档](https://learn.chatgpt.com/docs/automations)，**D**。
12. OpenAI：[Agents API overview](https://developers.openai.com/api/docs/guides/agents-api/overview)、[Scheduled automations](https://developers.openai.com/api/docs/guides/agents-api/sessions/automations)，均 **D**。
13. Anthropic：[Claude Code cloud scheduled tasks / routines](https://code.claude.com/docs/en/routines)，**D**。
14. Anthropic：[Claude Code scheduled tasks / loop](https://code.claude.com/docs/en/scheduled-tasks)，**D**。
15. Anthropic：[Hooks](https://code.claude.com/docs/en/hooks-guide)，**D**。
16. Anthropic：[Remote Control](https://code.claude.com/docs/en/remote-control)，**D**。
17. Anthropic：[Cowork web/mobile](https://claude.com/blog/cowork-web-mobile/)，**2026-07-07**；[当前运行位置说明](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)，**D**，明确记载 **2026-10-06** 变化。
18. Anthropic：[Schedule recurring tasks in Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)，**D**。
19. Anthropic：[Dispatch / assign tasks from anywhere](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)，**D**。
20. OpenClaw：[Introducing OpenClaw，命名沿革](https://openclaw.ai/blog/introducing-openclaw)，**2026-01-29**。
21. OpenClaw：[Automation](https://docs.openclaw.ai/automation)、[Heartbeat migration](https://docs.openclaw.ai/gateway/heartbeat)，均 **D**。
22. OpenClaw：[Memory overview](https://docs.openclaw.ai/concepts/memory)，**D**。
23. Manus：[Scheduled Tasks 2.0](https://manus.im/blog/manus-schedules)，**2026-05-18**；[Slack 结果交付](https://help.manus.im/en/articles/14431752-chatting-with-manus-agent-on-slack-channels-dms-and-file-delivery)，**D**。
24. Cognition：[Devin Automations](https://docs.devin.ai/product-guides/automations)、[Memory and Dreaming](https://docs.devin.ai/product-guides/memory)，均 **D**。
25. Google：[Jules proactive updates](https://blog.google/innovation-and-ai/technology/developers-tools/jules-proactive-updates/)，**2025-12-10**。
26. Google：[Gemini scheduled actions 发布](https://blog.google/products-and-platforms/products/gemini/scheduled-actions-gemini-app/)，**2025-06-06**；[当前帮助文档](https://support.google.com/gemini/answer/16316416?hl=en)，**D**。
27. Microsoft：[Agent 365 GA](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/)，**2026-05-01**；[定价公告](https://blogs.microsoft.com/blog/2026/03/09/introducing-the-first-frontier-suite-built-on-intelligence-trust/)，**2026-03-09**。
28. Microsoft：[Researcher and Analyst](https://www.microsoft.com/en-us/microsoft-365/blog/2025/03/25/introducing-researcher-and-analyst-in-microsoft-365-copilot/)，**2025-03-25**。
29. Microsoft：[Teams AI agents overview](https://learn.microsoft.com/en-us/microsoftteams/copilot-ai-agents-overview)，**D**。
30. Microsoft：[Planner updates](https://support.microsoft.com/en-au/planner/whats-new-in-microsoft-planner)，采用 **2026-03、2026-06** 条目；[状态报告](https://support.microsoft.com/en-us/planner/copilot/generate-automatic-status-reports-with-planner-agent)，**D**。
31. Asana：[AI Teammates 当前产品页](https://asana.com/product/ai/ai-teammates)，**D**；[Agentic Work Management / Dash 公告](https://investors.asana.com/node/12041/pdf)，**2026-06-04**。
32. Linear：[Loops docs](https://linear.app/docs/loops)，**D**；[Changelog](https://linear.app/changelog)，采用 **2026-07-20、2026-10-22** 条目。
33. Notion：[Custom Agents](https://www.notion.com/releases/2026-02-24)，**2026-02-24**；[3.8 context 更新](https://www.notion.com/releases)，**2026-10-13**；[credits pricing](https://www.notion.com/help/buy-and-track-notion-credits-for-custom-agents)，**D**。
34. Slack：[Updates and changes](https://slack.com/help/articles/115004846068-Slack-updates-and-changes)，采用 **2026-01、2026-04、2026-06、2026-10** 条目，部分仅标月份。
35. Lindy：[Pricing](https://www.lindy.ai/pricing)，**D**；检索缓存与本次打开页标价不一致。
36. OpenClaw／GitHub：[CVE-2026-25253 / GHSA](https://github.com/advisories/GHSA-g8p2-7wf7-98mq)，项目公告 **2026-01-31**，GitHub 数据库发布／更新 **2026-02-02**。
37. OpenClaw：[VirusTotal partnership](https://openclaw.ai/blog/virustotal-partnership)，**2026-02-07**。
38. Anthropic：[Project Vend](https://www.anthropic.com/research/project-vend-1)，**2025-06-27**。