# JEV / 系统一研究来源

**语言 / Language:** 中文（当前） · [English](sources.en.md)

更新时间：2026-09-21（亚洲/上海）

本文件记录了可复核的公开数据，服务于“把代理日志转成行为模式，再推荐可复用 JEV 实践”的产品方向。GitHub 星标、提交时间和仓库内容会持续变化；文中的数字是本次检索快照，不代表质量或生产可用性。证据强度启示：

- **高**：官方文档/官方代码，或仓库中有可运行实现、测试、明确数据。
- **中**：公开仓库有实现和方法，但规模、独立复现或生产数据有限。
- **低**：公开账号/搜索线索，只有观点或索引，尚未能核验具体实践。

## 官方与协议来源

| 来源（作者/日期） | 核心观点与可复核证据 | 与本项目的复用关系 | 强度 |
| --- | --- | --- | --- |
| [TypeSafe AI：Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)（TypeSafe AI，页面可见发布时间 2026-09-20） | 官方将 Jev 定位为面向机器使用的 System One 模型：输入状态和类型化问题，返回类型化决策/概率；不是用于写长文本的聊天模型。该页面的规范 URL、标题和描述页面源码核验。 README 的基础抽象应固定为“日志/状态 → 输入问题 → 策略代码”，不要把 JEV 当总结模型。习惯行为总结应由代码聚合日志，JEV 只做分类、相关性、风险和置信判断。 高|
| [TypeSafe AI 官方 skills](https://github.com/typesafe-ai/skills)（TypeSafe AI，2026-08-24创建，2026-09-12最近） | 官方仓库提供可挂载的`typesafe-ai`代理技能，支持Claude Code和`npx skills add`等安装方式；其README明确用途是设计TypeSafe工作流、查文档/cookbook，并在代码中组合类型判断。MIT。 本项目应同时提供与代理无关的 `SKILL.md`，定义日志读取、脱敏、死亡、证据链、实践匹配和低置信人工复核，而不是只做 Markdown 索引。 高|
| [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) / [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python)（TypeSafe AI，均2026-09创建） | 官方SDK的快速入门展示`Choice`等问题类型、状态对象和格式化响应；JS SDK支持类型推断，Python SDK提供`TypeSafeClient`。 车辆层可以按SDK的同种协议实现JS/Python的空白路径；将日志归一化为有限字段然后发给JEV，从而审计输入和离线回放。 高|
| [System One Adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python)（TypeSafe AI，2026-08-08 创建） | 官方提供由 LLM API 驱动的嵌入式适配器，补充使用、延迟、重试、调试尝试历史记录，可用于比较 TypeSafe 与 LLM 的成本/速度/智能。 为行为推荐器设计提供者抽象和离线A/B：JEV负责类型化决策，LLM作为核心；保存尝试、延迟和成本，避免只报告命中率。 高|

## 直接相关的开源实现

| 来源（作者/日期/快照） | 核心观点与可复核证据 | 与代理日志/习惯分析的复用关系 | 强度|
| --- | --- | --- | --- |
| [Hermes Jev Skills](https://github.com/kerpopule/hermes-jev-skills)（kerpopule，2026-09-18 创建；MIT；301 星） | 一个可跨Hermes、Claude Code、Codex使用的技能包；README描述了模型路由、内存通道过滤、压缩、技能选择、分类、邮件、浏览器/计算机使用，并强调影子模式、脱敏、超时/低置信失败打开。 是本项目最直接的“技能挂载”参照：日志分析器应先影子记录“如果使用JEV会推荐什么”，再由用户确认；只保存决策、置信度、延迟和脱敏后的特征；低置信不自动切换技能。 高（实现公开；其性能数字仍属作者自测） |
| [SkillRanker](https://github.com/Dicklesworthstone/skillranker)（Dicklesworthstone，2026-09-17创作；104星） | Rust CLI 利用当前会话、工作区信号和可视技能盘点做两阶段候选缩减与 Jev 监测排序，显式支持 `none`/`review`、`--why-not`、JSON hooks、离线重播、反馈和风险；README 还披露了网络选择加入和字段级披露收据。 直接推荐贡献其决策契约：`route | no_skill | review`三态；把“为什么没有推荐某实践”进行解释；用固定脱敏上下文概况和重播数据集评估推荐偏差。 高（代码/命令/设计均公开；尚需独立现） |
| [Jev Agent Skill Router](https://github.com/GodsBoy/jev-agent-skill-router)（GodsBoy，2026-09-16创作；11星） | Python路由器将大技能目录分批，通过Choice预筛、最终选择及need/ambiguity/fit Nouls做决策，并保留`route/no_skill/review`。README报告24个合成技能、72个请求、94.4%对比词法基线70.8%，同时明确这是复用数据的探索性结果。 可作为本项目日志到实践推荐的最小算法：本地先做候选分桶和显式技能请求优先，JEV只比较候选；把合成音乐和真实用户日志分开，不能把94.4%的生产效果。 高（仓库公布数据、报告和营业额）|
| [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)（tamaratran，2026-09-17 创建；MIT；5,446 颗星） | 每个工具调用/结果发类型保留/截断/删除判断；保留用户/助手文本文本，不改写，只删除低价值工具记录；支持阈值、最近消息保护、离线测试和自定义传输。 “自动读取代理日志”应采用仅追加原始日志+可重算派生索引；JEV只给保留/归档/截断的判断。保留原文和tool_use_id，保证行为模式可续，不需一次摘要覆盖证据。 高（实现公开；star 数量高但不需验证） |
| [Jev Logs](https://github.com/reachjalil/jevlogs)（reachjalil，2026-09-17 创建；MIT；8 星） | OpenTelemetry日志修复器：对每条记录打诊断值、优先级、可操作概率；默认保留所有记录并添加`jev.*`属性，只有低值且高置信时才跳过深度分析；错误、受保护记录和失败保留可分析。 日志采集层可采用相同模式：保留完整原始事件，将JEV决策边车标注；使用规则先行、编辑后模型调用、超时回退，并让“行为模式”作为标注聚合而不是删除原始数据。 高（README 描述协议、配置、失败策略；仓库状态为预览） |
| [jevify](https://github.com/altryne/jevify)（altryne，2026-09-17 创建；MIT；18 星） | Agent技能用于发现“哪些问题适合Jev”、设计输入问题，并跟踪社区实验；其定位是让Agent先判断是否值得接入Jev。 可增加“JEV设备性诊断”阶段：当某高频任务不适合类型化决策（需要长文本/复杂生成）时输出`not_applicable`，为了避免调用JEV而调用JEV。 中（仓库定位明确，需进一步核体验代码和体育） |
| [Cheshi](https://github.com/CheshiAI/Cheshi)（CheshiAI，2026-09-13创作；MIT；18星） | macOS Agent 工作台，支持 Codex 会话、CodeGraph、终端和 Git；README 说明 AI 对话可回看，索引和工作区数据放在项目外部。GitHub 描述了明显的 Jev 驱动的对话内存。 可形成“项目外部索引+原始会话回看”的产品形式：把日志解析数据库放在用户配置目录，保留源会话、文件/命令证据和时间窗；不要把索引噪声写回项目仓库。 中（Jev 相关能力主要由描述/周边资料提供） |
| [VexJoy Agent](https://github.com/notque/vexjoy-agent)（不是，2026-03-18 创建；MIT；421 颗星） | `/do` 将自然语言请求路由到专家代理/技能/工作流程，Jev 进行意图保留检查；README 强调审查、测试、交付、记录六段模拟，将对齐收据写入 `learning.db` 而不是保存原始请求。 “行为总结习惯”必须区分观察与结论：保存无源的意图/路线接收、任务结果和验证证据；对可疑威胁触发审查，直接不自动执行推荐。 高（仓库代码、数据落盘约束和流程公开） |
| [Jev-powered conversation memory: Cheshi](https://github.com/CheshiAI/Cheshi) 与 [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 项目体现了共同“译文可回溯二+JEV做选择”的方向，但并不是将用户行为直接结论为永久图像。 本项目的行为画像为时间窗内、可删除、可解释的派生统计；习惯每个标签绑定事件样本和置信区间，并支持用户重算/清除。 中文 |

## 开源替代与协议兼容（用于成本、隐私和回退比较）

| 来源（作者/日期/快照） | 核心观点与可复核证据 | 对本项目的意义 | 强度 |
| --- | --- | --- | --- |
| [OpenJev](https://github.com/razorback16/openjev)（razorback16，2026-09-18创建；Apache-2.0；225星） | 开源 System One 决策服务器，声称兼容 TypeSafe `/v1/systemone`，支持 `noul`、`choice`、`score`，提供 vLLM/MLX 许可证；README 明确声明独立项目、非 TypeSafe 官方。 可以作为任选本地/自托管提供商，支持敏感日志无法网；必须在 README 中将“协议兼容”与“模型等价”分开，并用相同的离线数据集比较输出。 中（协议和代码公开，性能/兼容性需实测） |
| [Von](https://github.com/wfzyx/von)（wfzyx，2026-09-18创建；Apache-2.0；262星） | 开源、非自回归System One风格模型，提供本地Python/TS SDK，定义Choice/Noul/Score；README给出与Jev的自测对比及调整方法，同时声明本地开源替代方案。 适合设计提供者抽象和隐私模式：`cloud_jev`、`openjev`、`von` 都返回相同的类型化决策模式；对“行为模式”只依赖模式，不绑定单一厂商。 中（自报基准，应独立复现） |
| [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) | 见官方来源表；其调试尝试历史记录不同提供商的请求、重试和延迟可回放。 统一体育JEV/替代/LLM开源时，记录输入schema、provider、latency、cost、retry和error，不只比较最终路线。 高|

## 社区与社交线索（待继续核验）

| 来源 | 已核验内容 | 处理方式 | 强度 |
| --- | --- | --- | --- |
| [TypeSafe AI 官方 X 账号 @typesafeai](https://x.com/TypeSafeAI) | 公开账号页面可访问，账号名为TypeSafe AI；本次无稳定、可引用的单条推文正文，因此不把账号页面实际具体实验结论。 后续通过X API/浏览器抓取单条推文的URL、发布时间、作者和上下文后，才进入“社区观点”章节；在此之前仅作为发现入口。 低|
| [TypeSafe AI GitHub 组织](https://github.com/TypeSafe-AI) | 公开组织页首发官方`skills`、JS/Python SDK和适配器等仓库，可作为官方实现入口。 用 GitHub 源码代替转述性社交帖子；社交帖子只是补充动机/体验，不覆盖代码证据。 高（入口） |
| 微信公众号/中文文章搜索 | 本次命令行搜索未获得可稳定读取、可去重且能验验原作者与发布时间的JEV专文；搜索摘要仍支持结论。 不虚构公众号观点；后续若有文章URL，需保留原文链接、作者、发布日期、截图/文档和引用段落，并标低/中强度。 未纳入 |

仓库现有的[Related Practices / Discussions](../categories/related-practices-discussions.md)还保存了以下单条公开X/博客线索。下面只把它们置于待复核的社区观点；X的登录态/动态渲染使得命令行无法稳定取得正文，因此不把转述为独立实验结果。

| 直接来源 | 社区观点（来自现有条目摘要） | 对本项目的启发 | 强度 |
| --- | --- | --- | --- |
| [Diogo Almeida 的发布帖](https://x.com/CompleteSkeptic/status/2099925682726002904) | TypeSafe创始人从“RLCD决策模型比聊天模型更快产生软件经济价值”角度介绍Jev。 作为产品定位线索；README应同时写清边界和失败策略，避免把创始人论点写成验证结论。 低（单帖待抓译） |
| [Jev 作为 Agent 安全监视器](https://x.com/isNickMa/status/2100566407524344225) | 实践者称在每个代理动作前用Jev做检查，目标是低延迟拦截攻击。 与日志行为分析直接相关：把每次工具调用的风险判定写成sidecar收据，并让拒绝/复核原因可追踪。 低（作者自报） |
| [Jev instant compaction](https://x.com/tamarajtran/status/2100694549362553153) | 社区提出用 JEV 上下文保留，而不是让 LLM 重写摘要。 佐证“文保留+派生判断”的实现方向；应配合`fast-jev-compaction`代码证据和回放集。 低（观点帖） |
| [任意分类是类型安全原语](https://x.com/cocktailpeanut/status/2100277062309179521) | 观点认为创新点在运行时定义、类型安全的任意分类，而非普通分类器。 日志模式 实习任务定义 Choice/Noul/Score；实践库应保存问题定义和版本，才能比较行为变化习惯。 低（观点帖） |
| [Jev 是一个智能 switch statement](https://x.com/NathanFlurry/status/2100036101809619314) | 基础设施从业者认为Jev不替代GPT/Claude，而是有2026知识的switch语句。 支持“JEV决策层+Agent执行层”架构；README不宜承诺JEV负责汇总、规划或生成长文。 低（观点帖） |
| [Jev 中文解读](https://x.com/dotey/status/2100109937237987823) | 中文帖子将系统一解释为面向代码的布局、类型化的决策层。 可以作为中文用户入门线索，但需要回到官方 API/代码核心对术语。 低（转述） |
| [Jev 不是 LLM 的新闻分析](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/) | 新闻评论将“不生成文本”视为设计特性，并讨论推理成本。 可用于项目介绍的背景部分，但功能承诺仍与官方文档和可运行代码一致。 中（可直接访问的媒体文章，需核译引用） |
| [Jev 复杂度与边界的中文深读](https://github.com/kuhung/understanding-jev) | 中文仓库讨论多层急救及工程边界。 在中文README中保留“适合固定决策边界、不适合开放式长文生成”的反例和限制。 中（公开仓库，需逐段核验） |

## 面向本项目的可执行结论

1. **边界数据**：原始代理日志仅附加保存；JEV输入只包含最小化、脱敏后的状态和格式化特征。派生的习惯标签必须能回指事件ID、时间窗和规则版本。
2. **推荐协议**：统一返回`route`、`no_skill`、`review`三态，并附候选、Choice/Noul/Score结果、置信度、提供商、延迟和策略版本；显式用户点名技能在本地优先解析。
3. **运行策略**：先影子模式观察推荐与用户实际选择；低置信、超时、敏感日志或策略冲突时fail-open到原Agent流程，模块因为JEV无响应阻塞任务。
4. **行为分析**：先做本地时间窗聚合（任务类型、工具序列、失败/重试、使用的技巧），JEV只判断边界和候选匹配；高度不相等应自动化，需同时观察成功率、用户采纳率和反例。
5. **评分**：建立带人工标签的回放集，同时评估技能推荐、日志保留/压缩和行为模式等；报告覆盖范围、弃权、错误推荐成本、延迟、令牌/成本和隐私字段暴露，不把仓库自报数字直接当指标生产。
6. **来源治理**：每条实践保留原始URL、提取日期、作者、许可证、代码证据位置和强度；GitHub star只作发现信号，不作质量排序。
