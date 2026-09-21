# JEV / System One 研究来源

更新时间：2026-09-21（Asia/Shanghai）

本文件记录可复核的公开资料，服务于“把 Agent 日志转成行为模式，再推荐可复用 JEV 实践”的产品方向。GitHub 星标、提交时间和仓库内容会持续变化；文中的数字是本次检索快照，不代表质量或生产可用性。证据强度含义：

- **高**：官方文档/官方代码，或仓库中有可运行实现、测试、明确数据。
- **中**：公开仓库有实现和方法，但规模、独立复现或生产数据有限。
- **低**：公开账号/搜索线索，只有观点或索引，尚未能核验具体实践。

## 官方与协议来源

| 来源（作者/日期） | 核心观点与可复核证据 | 与本项目的复用关系 | 强度 |
| --- | --- | --- | --- |
| [TypeSafe AI：Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)（TypeSafe AI，页面可见发布时间 2026-09-20） | 官方将 Jev 定位为面向机器使用的 System One 模型：输入状态和 typed questions，返回 typed decisions / probabilities；不是用于写长文本的聊天模型。该页的 canonical URL、标题和描述可由页面源码核验。 | README 的基础抽象应固定为“日志/状态 → typed question → 代码策略”，不要把 JEV 当总结模型。行为习惯总结应由代码聚合日志，JEV 只做分类、相关性、风险和置信判断。 | 高 |
| [TypeSafe AI 官方 skills](https://github.com/typesafe-ai/skills)（TypeSafe AI，2026-08-24 创建，2026-09-12 最近推送） | 官方仓库提供可挂载的 `typesafe-ai` Agent skill，支持 Claude Code 和 `npx skills add` 等安装方式；其 README 明确用途是设计 TypeSafe 工作流、查文档/cookbook，并在代码中组合 typed judgments。MIT。 | 本项目应同时提供 Agent-agnostic `SKILL.md`，定义日志读取、脱敏、聚类、证据链、实践匹配和低置信人工复核，而不是只做 Markdown 索引。 | 高 |
| [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) / [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)（TypeSafe AI，均 2026-09 创建） | 官方 SDK 的 quickstart 展示 `Choice` 等问题类型、状态对象和结构化响应；JS SDK 支持类型推断，Python SDK 提供 `TypeSafeClient`。 | 适配层可以按 SDK 的同一协议实现 JS/Python 两条路径；将日志归一化为有限字段后再发给 JEV，便于审计输入和离线回放。 | 高 |
| [System One Adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python)（TypeSafe AI，2026-08-08 创建） | 官方提供由 LLM API 驱动的 drop-in adapter，补充 usage、latency、retry、debug attempt history，可用来比较 TypeSafe 与 LLM 的 cost/speed/intelligence。 | 为行为推荐器设计 provider 抽象和离线 A/B：JEV 负责 typed decision，LLM 作为基线；保存 attempts、latency 和成本，避免只报告命中率。 | 高 |

## 直接相关的开源实现

| 来源（作者/日期/快照） | 核心观点与可复核证据 | 与 Agent 日志/习惯分析的复用关系 | 强度 |
| --- | --- | --- | --- |
| [Hermes Jev Skills](https://github.com/kerpopule/hermes-jev-skills)（kerpopule，2026-09-18 创建；MIT；301 stars） | 一个可跨 Hermes、Claude Code、Codex 使用的技能包；README 描述 model routing、memory passage filtering、compaction、skill selection、triage、mail、browser/computer use，并强调 shadow mode、脱敏、超时/低置信 fail-open。 | 是本项目最直接的“技能挂载”参照：日志分析器应先 shadow 记录“如果使用 JEV 会推荐什么”，再由用户确认；只保存决策、置信度、延迟和脱敏后的特征；低置信不自动切换技能。 | 高（实现公开；其性能数字仍属作者自测） |
| [SkillRanker](https://github.com/Dicklesworthstone/skillranker)（Dicklesworthstone，2026-09-17 创建；104 stars） | Rust CLI 用当前会话、工作区信号和可见 skill inventory 做两阶段候选缩减与 Jev 排序，显式支持 `none`/`review`、`--why-not`、JSON hooks、离线 replay、反馈和风险监测；README 还披露网络 opt-in 和字段级 disclosure receipts。 | 推荐直接借鉴其决策契约：`route | no_skill | review` 三态；把“为什么没有推荐某实践”写入可读解释；用固定脱敏 context profile 和 replay 数据集评估推荐偏差。 | 高（代码/命令/设计均公开；尚需独立复现） |
| [Jev Agent Skill Router](https://github.com/GodsBoy/jev-agent-skill-router)（GodsBoy，2026-09-16 创建；11 stars） | Python 路由器将大 skill catalog 分批，通过 Choice 预筛、最终 Choice 及 need/ambiguity/fit Nouls 做决策，并保留 `route/no_skill/review`。README 报告 24 个合成技能、72 个请求、94.4% 对比词法基线 70.8%，同时明确这是复用数据的探索性结果。 | 可作为本项目日志到实践推荐的最小算法：本地先做候选分桶和显式技能请求优先，JEV 只比较候选；把合成评测和真实用户日志分开，不能把 94.4% 当生产效果。 | 高（仓库给出数据、报告和局限） |
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)（tamaratran，2026-09-17 创建；MIT；5,446 stars） | 对每个 tool call/result 发 typed keep/truncate/drop 判断；保留用户/助手文本原文，不改写，只删除低价值工具记录；支持阈值、最近消息保护、离线测试和自定义 transport。 | “自动读取 Agent 日志”应采用 append-only 原始日志 + 可重算派生索引；JEV 只给保留/归档/截断的判断。保留原文和 tool_use_id，保证行为模式可追溯，不以一次摘要覆盖证据。 | 高（实现公开；star 数量高但不等同验证） |
| [Jev Logs](https://github.com/reachjalil/jevlogs)（reachjalil，2026-09-17 创建；MIT；8 stars） | OpenTelemetry 日志预处理器：对每条记录打 diagnostic value、priority、actionable probability；默认保留所有记录并添加 `jev.*` 属性，只有低价值且高置信时才跳过深度分析；错误、受保护记录和失败保持可分析。 | 日志采集层可采用同一模式：保留完整原始事件，把 JEV 决策作为 sidecar annotation；使用规则先行、redaction 后模型调用、超时回退，并让“行为模式”从 annotation 聚合而不是删除原始数据。 | 高（README 描述协议、配置、失败策略；仓库状态为 preview） |
| [jevify](https://github.com/altryne/jevify)（altryne，2026-09-17 创建；MIT；18 stars） | Agent skill 用于发现“哪些问题适合 Jev”、设计 typed questions，并跟踪社区实验；其定位是让 Agent 先判断是否值得接入 Jev。 | 可增加“JEV 适配性诊断”阶段：当某高频任务不适合 typed decision（需要长文本/复杂生成）时输出 `not_applicable`，避免为了调用 JEV 而调用 JEV。 | 中（仓库定位明确，需进一步核验代码和评测） |
| [Cheshi](https://github.com/CheshiAI/Cheshi)（CheshiAI，2026-09-13 创建；MIT；18 stars） | macOS Agent 工作台，支持 Codex 会话、CodeGraph、终端和 Git；README 说明 AI 对话可回看，索引和工作区数据放在项目外部。GitHub 描述明确标注 Jev-powered conversation memory。 | 可借鉴“项目外部索引 + 原始会话回看”的产品形态：把日志解析数据库放在用户配置目录，保留来源会话、文件/命令证据和时间窗；不要把索引噪声写回项目仓库。 | 中（Jev 相关能力主要由描述/周边资料宣称） |
| [VexJoy Agent](https://github.com/notque/vexjoy-agent)（notque，2026-03-18 创建；MIT；421 stars） | `/do` 将自然语言请求路由到 specialist agent/skill/workflow，Jev 进行意图保持检查；README 强调 review、tests、deliver、record 六段流水线，并将 alignment receipt 写入 `learning.db` 而不保存原始请求。 | “行为习惯总结”必须区分观察与结论：保存无原文的 intent/route receipt、任务结果和验证证据；对可疑意图漂移触发 review，不直接自动执行推荐。 | 高（仓库代码、数据落盘约束和流程公开） |
| [Jev-powered conversation memory: Cheshi](https://github.com/CheshiAI/Cheshi) 与 [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 两个项目共同体现“原文可回溯 + JEV 做选择”的方向，但不是将用户行为直接归纳为永久画像。 | 本项目的行为画像应是时间窗内、可删除、可解释的派生统计；每个习惯标签绑定事件样本和置信区间，并支持用户重算/清除。 | 中 |

## 开源替代与协议兼容（用于成本、隐私和回退比较）

| 来源（作者/日期/快照） | 核心观点与可复核证据 | 对本项目的意义 | 强度 |
| --- | --- | --- | --- |
| [OpenJev](https://github.com/razorback16/openjev)（razorback16，2026-09-18 创建；Apache-2.0；225 stars） | 开源 System One decision server，声称兼容 TypeSafe `/v1/systemone`，支持 `noul`、`choice`、`score`，提供 vLLM/MLX 后端；README 明确声明独立项目、非 TypeSafe 官方。 | 可以作为可选本地/自托管 provider，支持敏感日志不出网；必须在 README 中将“协议兼容”与“模型等价”分开，并用同一离线数据集比较输出。 | 中（协议和代码公开，性能/兼容性需实测） |
| [Von](https://github.com/wfzyx/von)（wfzyx，2026-09-18 创建；Apache-2.0；262 stars） | 开源、非自回归 System One 风格模型，提供本地 Python/TS SDK，定义 Choice/Noul/Score；README 给出与 Jev 的自测对比及校准方法，同时声明本地开源替代。 | 适合设计 provider 抽象和隐私模式：`cloud_jev`、`openjev`、`von` 都返回同一 typed decision schema；对“行为模式”只依赖 schema，不绑定单一厂商。 | 中（自报 benchmark，应独立复现） |
| [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) | 见官方来源表；其 debug attempt history 让不同 provider 的请求、重试和延迟可回放。 | 统一评测 JEV/开源替代/LLM 基线时，记录输入 schema、provider、latency、cost、retry 和错误，不只比较最终 route。 | 高 |

## 社区与社交线索（待继续核验）

| 来源 | 已核验内容 | 处理方式 | 强度 |
| --- | --- | --- | --- |
| [TypeSafe AI 官方 X 账号 @typesafeai](https://x.com/TypeSafeAI) | 公开账号页可访问，账号名为 TypeSafe AI；本次无稳定、可引用的单条推文正文，因此不把账号页当作具体实验结论。 | 后续通过 X API/浏览器抓取单条推文的 URL、发布时间、作者和上下文后，才进入“社区观点”章节；在此之前只作为发现入口。 | 低 |
| [TypeSafe AI GitHub 组织](https://github.com/TypeSafe-AI) | 公开组织页列出官方 `skills`、JS/Python SDK 和 adapter 等仓库，可作为官方实现入口。 | 用 GitHub source 代替转述性社交帖子；社交帖子只补充动机/体验，不覆盖代码证据。 | 高（入口） |
| 微信公众号/中文文章检索 | 本次命令行检索未获得可稳定读取、可去重且能核验原文作者与发布时间的 JEV 专文；搜索摘要不足以支撑结论。 | 不虚构公众号观点；后续若有文章 URL，需保留原文链接、作者、发布日期、截图/存档和引用段落，并标低/中强度。 | 未纳入 |

仓库现有的 [Related Practices / Discussions](../categories/related-practices-discussions.md) 还保存了以下单条公开 X/博客线索。下面只把它们当作待复核的社区观点；X 的登录态/动态渲染会使命令行无法稳定取得正文，因此不把转述当作独立实验结果。

| 直接来源 | 社区观点（来自现有条目摘要） | 对本项目的启发 | 强度 |
| --- | --- | --- | --- |
| [Diogo Almeida 的发布帖](https://x.com/CompleteSkeptic/status/2099925682726002904) | TypeSafe 创始人从“RLCD 决策模型比聊天模型更快产生软件经济价值”角度介绍 Jev。 | 作为产品定位线索；README 应同时写清边界和失败策略，避免把创始人论点写成验证结论。 | 低（单帖待抓原文） |
| [Jev 作为 Agent 安全监视器](https://x.com/isNickMa/status/2100566407524344225) | 实践者称在每个 Agent action 前用 Jev 做检查，目标是低延迟拦截攻击。 | 与日志行为分析直接相关：把每次工具调用的风险判定写成 sidecar receipt，并让拒绝/复核原因可追踪。 | 低（作者自报） |
| [Jev instant compaction](https://x.com/tamarajtran/status/2100694549362553153) | 社区提出用 JEV 判断上下文保留，而不是让 LLM 重写摘要。 | 佐证“原文保留 + 派生判断”的实现方向；应配合 `fast-jev-compaction` 代码证据和回放集。 | 低（观点帖） |
| [任意分类是类型安全原语](https://x.com/cocktailpeanut/status/2100277062309179521) | 观点认为创新点在运行时定义、类型安全的任意分类，而非普通分类器。 | 日志 schema 可由任务定义 Choice/Noul/Score；实践库应保存问题定义和版本，才能比较行为习惯变化。 | 低（观点帖） |
| [Jev 是一个智能 switch statement](https://x.com/NathanFlurry/status/2100036101809619314) | 基础设施从业者认为 Jev 不替代 GPT/Claude，而是有 2026 知识的 switch statement。 | 支持“JEV 决策层 + Agent 执行层”架构；README 不应承诺 JEV 负责总结、规划或生成长文。 | 低（观点帖） |
| [Jev 中文解读](https://x.com/dotey/status/2100109937237987823) | 中文帖子将 System One 解释为面向代码的校准、类型化决策层。 | 可作为中文用户 onboarding 线索，但需回到官方 API/代码核对术语。 | 低（转述） |
| [Jev 不是 LLM 的新闻分析](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/) | 新闻评论将“不生成文本”视为设计特性，并讨论推理成本。 | 可用于项目介绍的背景段，但功能承诺仍以官方文档和可运行代码为准。 | 中（可直接访问的媒体文章，需核原文引用） |
| [Jev 复杂度与边界的中文深读](https://github.com/kuhung/understanding-jev) | 中文仓库讨论毫秒级判定及工程边界。 | 在中文 README 中保留“适合固定决策边界、不适合开放式长文生成”的反例和限制。 | 中（公开仓库，需逐段核验） |

## 面向本项目的可执行结论

1. **数据边界**：原始 Agent 日志 append-only 保存；JEV 输入只包含最小化、脱敏后的状态和结构化特征。派生的习惯标签必须能回指事件 ID、时间窗和规则版本。
2. **推荐协议**：统一返回 `route`、`no_skill`、`review` 三态，并附候选、Choice/Noul/Score 结果、置信度、provider、延迟和策略版本；显式用户点名的 skill 在本地优先解析。
3. **运行策略**：先 shadow mode 观察推荐与用户实际选择；低置信、超时、敏感日志或策略冲突时 fail-open 到原 Agent 流程，绝不因为 JEV 无响应阻塞任务。
4. **行为分析**：先做本地时间窗聚合（任务类型、工具序列、失败/重试、使用的 skill），JEV 只判断语义边界和候选匹配；高频不等于应该自动化，需同时观察成功率、用户采纳率和反例。
5. **评测**：建立带人工标签的回放集，分开评估 skill 推荐、日志保留/压缩和行为模式聚类；报告 coverage、abstention、误推荐成本、延迟、token/cost 和隐私字段暴露，不把仓库自报数字直接当生产指标。
6. **来源治理**：每条实践保留原始 URL、抓取日期、作者、license、代码证据位置和强度；GitHub star 只作发现信号，不作质量排序。
