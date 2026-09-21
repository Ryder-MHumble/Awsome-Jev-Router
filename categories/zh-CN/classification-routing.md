# 分类和路由

**语言 / Language:** 中文（当前） · [English](../classification-routing.md)

将此类别用于 Jev 对传入状态进行分类或选择下一个目的地（票证、意图、警报、文档或流量）的程序。

## 提交格式
```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```
## 条目

- [Notra](https://github.com/usenotra/notra) - 营销分析：生产 GEO 平台，其 `NOTRA_JEV_CLASSIFIERS` 标志将品牌可见性分类器从 LLM 路由到 Jev `Boolean` 决策，阈值为 0.5，目标为 300 ms p50。
- [jev-router](https://github.com/gargpratyush/jev-router) - 开发人员工具：通过要求 Jev 在候选者中进行选择，将 Claude Code 任务路由到最便宜的模型。
- [jev-router (prismhq)](https://github.com/prismhq/jev-router) - LLM 基础设施：基于 LiteLLM 的开源路由器，其中 Jev 决策选择哪个模型来服务每个请求。
- [pi-jev-router](https://github.com/mejiasd3v/pi-jev-router) - 编码代理：通过 Vercel AI Gateway 上的 Jev 决策，向 Pi 编码代理添加自动按请求模型路由。
- [jcm-router](https://github.com/adarshmishra07/jcm-router) - 编码代理：本地代理，通过 Jev 决策选择每条消息的 Claude 模型和推理工作，同时保持缓存的主聊天不变。
- [Jev Auto Router](https://github.com/miniLV/Jev-Auto-Router) - 编码代理：每次调用 Codex GPT 路由，其中​​ Jev 对主机可用（模型、工作量）对做出一种类型选择；本地Responses代理保持工具循环连续，然后独立验证和Router Compass记录任务是否仍然通过（原型）。
- [jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router) - 代理基础设施：通过键入的、有信心的 Jev 决策来路由代理技能选择，因此弱匹配会被拒绝而不是猜测。
- [typesafe-jev CV screener](https://github.com/gtaras7/typesafe-jev) - 招聘：筛选简历文件夹，其中包含 Jev 根据可编辑政策键入的判断，当政策发生变化时，免费重新对候选人进行评分。
- [Jev email intent workflow](https://github.com/GiesN/typesafe-jev-workflow) - 后台自动化：异步 LangGraph 工作流程获取类型化的 Jev `Choice`（`invoice` 或 `general`），并将每封入站电子邮件路由到匹配的处理程序。
- [unclutter](https://github.com/kitze/unclutter) - 浏览器工具：WXT 扩展，其中 Jev 决定每个页面元素是否混乱，并根据可重用模板规则将其删除。
- [typesafe-adblock](https://github.com/realZachi/typesafe-adblock) - 浏览器工具：Chrome 扩展程序询问 Jev 每个 DOM 元素是否是广告，将广告拦截转变为每个元素类型的问题流。
- [DiffJury](https://github.com/raihankhan-rk/diffjury) - 代码审查：在分配人工审查员之前，按风险与 Jev 路由每个拉取请求，兼任审查教练。
- [HA-Jev](https://github.com/AboveColin/HA-Jev) - 智能家居：家庭助理集成，以概率、选择或分数的形式回答有关房屋的问题。
- [secondlayer](https://github.com/ryanwaits/secondlayer) - 故障分类：自托管 Stacks 数据服务，其 Slack 门和故障分类路径均根据 Jev 决策运行。
- [jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage) - 随叫随到操作：批量折叠的 Loki 登录到 Noul、Score 和 Choice 问题的一个 Jev 调用中，然后将答案映射到代码中以抑制、观看、审阅、通知或寻呼，低置信度会审阅且不执行任何操作。
- [new-api-typesafe-plugin](https://github.com/FFatTiger/new-api-plugin-typesafe) - LLM 网关：向 new-api 添加本机 `/v1/systemone` 端点，因此键入的决策与聊天模型位于同一网关后面。
- [duet-agent](https://github.com/dzhng/duet-agent) - 代理工具：保留 Jev 支持的路由表，用于决定哪个模型应该服务请求。
- [json-render](https://github.com/vercel-labs/json-render) - 生成式 UI：Vercel Labs 的 UI 框架在其撰写路径中使用 Jev 来选择渲染界面应包含哪些组件和操作。
- [omo-jevlike-router](https://github.com/islee23520/omo-jevlike-router) - 技能路由：通过对冻结的 Qwen 进行一次前向传递来缩小系统提示中的技能目录，以 Jev 风格路由每个请求。
- [jev-cookbook](https://github.com/nexibeo/jev-cookbook) - 开发人员教育：15 个可运行的 Node 配方，用于路由支持票证、归档文档、对银行交易进行分类并使用 Jev `Choice` 和 `Noul` 问题标记 Gmail，发送低可信度答案以供人工审核。
- [flue-jev-demo](https://github.com/matthewp/flue-jev-demo) - 代理路由：通过 Cloudflare AI Gateway 路由 Flue 代理与 Jev 的工作。
- [sift](https://github.com/bohutang/sift) - 内容标签：Chrome 扩展程序，根据 Jev 的决定，标记 X 时间线中的每个帖子 - 实质内容、幽默、闲聊、促销、垃圾或 AI 编写。
- [DocJev](https://github.com/jerryjliu/docjev) - 文档管道：LlamaIndex 的开源库，可根据自然语言类别规则对文档进行分类或查找子文档之间的边界，具有可交换的 OCR 后端（liteparse 或 LlamaParse）和基准测试工具，其 40 个文档试点在大约 182 ms Jev 决策 p50 时正确分类了 40/40 个原始文档。
- [jev-fit](https://jev-fit.com) - 开发人员工具：托管适配检查器，在一次调用中向 Jev 发送粘贴的软件创意和固定类型的标题，其中 `Choice` 选择纯代码、Jev 或 `Noul` 门后面的推理 LLM 进行非任务，当创意需要图像时，代码否决 Jev，低置信度返回“不确定”；闭源、免费页面和 API。
