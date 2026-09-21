# 基础设施/SDK/集成

**语言 / Language:** 中文（当前） · [English](../infra-sdks-integrations.md)

使用此类别来构建围绕 Jev 构建的生态系统工具 - SDK、包装器、网关、框架适配器、评估支架、本地端口。

## 提交格式
```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```
## 条目

- [eve](https://github.com/vercel/eve) - 代理框架：Vercel 的 eve 引擎在其实验评估路径中将 Jev 作为默认评估模型 (`typesafe-ai/jev`)。
- [AI CLI](https://github.com/vercel-labs/ai-cli) - 开发人员工具：Vercel Labs CLI，可以运行 Jev 作为其 `evaluate` 命令的评估模型。
- [jev-mcp (jkudish)](https://github.com/jkudish/jev-mcp) - MCP 生态系统：概念验证 MCP 服务器，将 Jev 声明验证、内容筛选和候选排名置于标准 MCP 工具之后。
- [jev-mcp (blakestone-x)](https://github.com/blakestone-x/jev-mcp) - MCP 生态系统：MCP 服务器将 Jev 分类、评分、检查、匹配和筛选作为任何代理的工具，对每个答案都充满信心。
- [zio-typesafe-ai](https://github.com/jamesward/zio-typesafe-ai) - Scala 生态系统：TypeSafe AI 的 ZIO 客户端，具有基于 Jev 决策的类型化 DSL。
- [laya-mlx](https://github.com/mizorewww/laya-mlx) - 本地运行时：Laya 检查点的独立 MLX 端口，在 Apple Silicon 上本地运行类型化决策 — 每个短英文决策的端到端平均时间为 13.4 毫秒，多语言检查点为 7.4 毫秒，输出令牌为零，没有 PyTorch、Transformers 运行时或云 API。
- [TypeSafe AI Swift SDK](https://github.com/alterhq/typesafe-sdk-swift) - Swift 生态系统：用于 Jev Choice、Score 和 Noul 问题的无依赖性 Swift 6 客户端，具有严格的并发性、可配置的身份验证和重试以及离线传输测试。
- [laravel-typesafe-jev](https://github.com/Butochnikov/laravel-typesafe-jev) - PHP 生态系统：Jev 的非官方 Laravel 集成，具有类型化响应、异步请求、范围依赖注入和测试假货。
- [advocaat](https://github.com/pithings/advocaat) - 数据工具：小型类型安全客户端，用于向 Jev 询问有关数据集的问题。
- [jevclient](https://pypi.org/project/jevclient/) - Python 生态系统：在 PyPI 上发布的 Jev 异步客户端。
- [LlamaIndex Jev](https://github.com/WiktorB2004/llama-index-jev) - 检索/RAG：非官方 LlamaIndex 适配器，其中 Jev `Score` 检索每个段落，`Choice`/`Noul` 选择查询引擎，nfcorpus nDCG@5 0.340→0.396，每次查询价格约为 0.0003 美元。
- [safer-with-jev](https://github.com/andrelandgraf/safer-with-jev) - 云基础设施：Neon AI 网关的 Neon 功能代理，通过 Jev 路由决策。
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) - 官方工具：可安装的代理技能包 (`npx skills add typesafe-ai/skills`)，用于向代理传授 Jev 工作流程。
- [Smithers](https://github.com/smithersai/smithers) - 代理框架：TypeScript 工作流程框架，其工作流程中连接有 Jev 会话检查器。
- [skillbox](https://github.com/kitze/skillbox) - 技能基础设施：自托管版本化技能库，使用您自己的 TypeSafe 或网关密钥添加可选的 Jev 建议。
- [Jevbridge](https://github.com/tacticocc/Jevbridge) - 代理桥：ACP 和 MCP 适配器，将 Jev 类型的决策公开给 Codex、Claude、Grok 和其他 LLM。
- [jev (Elixir)](https://github.com/dannote/jev) - Elixir 生态系统：GenServer 客户端回复 Jev 的答案，以便调用者可以直接在其上进行模式匹配。
- [jev-go](https://github.com/Stumble/jev-go) - Go 生态系统：Jev 社区 Go SDK。
- [jev-cli](https://github.com/tumf/jev-cli) - 开发人员工具：适用于 Jev 的小型无依赖性 CLI。
- [decide-mcp](https://github.com/dakdevs/decide-mcp) - MCP 生态系统：可配置的决策服务器，在 Jev 之上具有百分比分数和偏差配置文件路由。
- [typesafe-jev-examples](https://github.com/rajivkuriakose/typesafe-jev-examples) - 入门示例：工作票分类和重新排名示例可通过 OpenRouter 运行，无需早期访问密钥，附带自己的示例数据和 Makefile。
- [ai-python](https://github.com/vercel-labs/ai-python) - Python 生态系统：Python 官方 Vercel AI SDK 通过其评估操作和网关示例承载 Jev。
- [Cline plugins](https://github.com/cline/plugins) - 编码代理：Cline 的官方插件集合包括 Jev 驱动的浏览器插件 (`jev-browser`)，因此 Jev 是一流的 Cline 功能。
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) - Web 框架：Hono 中间件，根据含义而不是方法和路径路由 HTTP 请求，由 Jev 决定。
- [rotom](https://github.com/RyanKung/rotom) - 本地网关：兼容 OpenAI 和 Anthropic 的 API 网关，通过其模型目录和评估路径承载 Jev。
- [Jev AI](https://jev-ai.pro) - 开发人员工具：公共 Jev 游乐场和 API，将输入的 `Choice`、`Score` 和是/否问题输入到有关粘贴文本的模型 - 票证分类、审核、审核评分 - 并返回一个已解析的答案，每个决策的置信度值约为 0.5 秒。
- [jevql](https://github.com/kylemclaren/jevql) - 数据工具：psql 型 CLI 和 Go/TypeScript/Python SDK，在普通 Postgres（无扩展）上运行普通 SQL，然后针对每个幸存行询问 Jev Noul、Choice 或 Score 问题，以便客户端可以应用 `jev()` 过滤器、`jev_prob` 排序和 `jev_choice` 组。
- [sqlite-jev](https://github.com/mgaitan/sqlite-jev) - SQLite 生态系统：可加载的 C 扩展和 Python 包，将 Jev Noul、Choice 和 Score 判断公开为 SQL 函数以及带有置信结果的批量虚拟表查询。
- [jevkit](https://github.com/ariel-frischer/jevkit) - 开发人员工具：Rust CLI 在任何 Jev 调用之前使用 13 个离线 lint 规则验证 `Choice`/`Score`/`Noul` 问题集，然后发送规范的线路负载并使用退出代码 2 将已解析的、可信的 JSON 答案打印到 stdout，以拒绝计费但无用的请求。
- [jev-use](https://github.com/shitianfang/jev-use) - MCP 生态系统：Claude Code / Codex / pi 插件（MCP 服务器 + 库、本机 pi 扩展），将不需要文本输出到 Jev 的代理步骤作为键入判断 — 不可键入和需要生成的问题在调用之前被拒绝，低置信度答案返回时标记为先验，并且失败打开的 PreToolUse 门只能拒绝或询问。
- [huncho](https://github.com/edgardcham/huncho) - TypeScript 生态系统：无依赖性 SDK，可将 Jev `Noul`、`Choice` 和 `Score` 答案转换为具有 `enter`/`exit` 阈值（滞后）的命名决策、一次调用中解决的嵌套决策树、JSONL 日志、在不进行推理的情况下重放记录答案的阈值更改，以及通过 TypeSafe direct、OpenRouter 或 Vercel AI Gateway 进行 Brier/可靠性校准。
- [jev-experiments](https://github.com/dabit3/jev-experiments) - 演示集合：由 Devin 构建的 22 个专注于延迟的 Jev 应用程序，每个应用程序都有自己的 README 和测试说明，涵盖 shell 防护、日志哨兵、即时搜索、重新排名和语音轮流。
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) - Ruby 生态系统：Jev 等决策模型的客户端，因此 Ruby 应用程序可以将键入的问题直接放入模型中。
- [s1_ruby](https://github.com/innocentdiaz/s1_ruby) - Ruby 生态系统：进行 System One 测量，以及随之而来的崩溃，一个 Ruby 原语，在其自己的规范套件背后有一个 TypeSafe 提供程序。
- [JarvisCore](https://github.com/Prescott-Data/jarviscore-framework) - 代理框架：从 1.12 开始原生提供 Jev 的 Python 多代理运行时，其中代理通过与文本模型分离的决策客户端询问键入的 `Choice`、`Score` 和 `Noul` 问题，内核通过 `Choice` 选择专业子代理，并且每个检索到的 RAG 段落在提示注入时都会从生成模型中保留`Noul`超过0.70。
- [hunch](https://github.com/carldaws/hunch) - Ruby 生态系统：将判断调用转变为控制流 - `if Hunch.likely?("fraudulent", given: order)` 读起来像普通的 Ruby，但在类型化的 Jev 答案上分支，其中 `pick` 代表 Choice，`rate` 代表 Score，分级谓词从 `possibly?` 到 `definitely?`。
- [Early experimentation using Jev to rethink harness UX](https://www.elvex.com/blog/early-experimentation-using-jev-to-rethink-harness-ux) - 线束集成：代理平台将 Jev 连接到其 LLM 线束中，作为搜索、审批和上下文的可调用工具，在 20 秒内报告分类的 2,000 份费用报告，只需 5 美分。
- [jev-mcp (burnigtm)](https://github.com/burnigtm/jev-mcp) - MCP 生态系统：将 Jev 放入 Cursor、Codex 和任何 MCP 客户端的编码循环中的服务器，后面有 20 个测试文件。
- [jev-skill-suggester](https://github.com/win4r/jev-skill-suggester) - 编码代理：建议哪些已安装的技能适用于请求，保持建议的范围并让 Jev 决定。
- [grok-bot-jev](https://github.com/Bodila51/grok-bot-jev) - 代理桥梁：将 Jev 连接到 Grok Bot 作为廉价的决策层，具有使用门、技能模板和工作示例。
- [jev-architect](https://github.com/karanb192/jev-architect) - 设计技能：查找、设计和评估 Jev 决策循环，打包为一项技能，并参考决策设计和交付。
- [Building a Harness with Jev](https://www.langchain.com/blog/building-a-harness-with-jev) - 框架指南：LangChain 将 Jev 连接到代理线束作为决策层的演练，来自一个团队，该团队随后发布了自己对 Jev 作为法官的评估。
- [openrouter-jev-mcp](https://github.com/ctmx/openrouter-jev-mcp) - MCP 生态系统：Python 决策网关和 stdio MCP 服务器通过 OpenRouter 的 alpha 决策端点公开 TypeSafe 的 Jev 模型。
