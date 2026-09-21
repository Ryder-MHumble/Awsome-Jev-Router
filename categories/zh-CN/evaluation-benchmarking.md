# 评估和基准测试

**语言 / Language:** 中文（当前） · [English](../evaluation-benchmarking.md)

将此类别用于 Jev 判断模型或系统输出的程序 - 评估工具、LLM-as-judge replacements、基准评分器、回归门。

## 提交格式
```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```
## 条目

- [Jev Web Analyzer](https://github.com/replynodes/jev-web-analyzer) - 产品评估：将公共 SaaS 登陆页面分析为干净的 Markdown，并向 Jev 询问 10 个有关首次访问理解的有限 `Choice` 问题，返回可检查的结果以进行第一次更改。

- [Jev Playground](https://github.com/hegargarcia/jev-playground) - 模型评估：在显式状态游戏中选择经过验证的合法动作，对 Jev 与 Luna、Haiku 和 Gemini 进行基准测试，对一系列动作的决策质量和一致性进行评分。
- [Jev vs Mistral and Gemini for event validation](https://nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation) - 事件发现：在验证本地事件列表时，Jev 与 Mistral Small 和 Gemini Flash-Lite 进行头对头测试。
- [jev-research-eval](https://github.com/jgridifier/jev-research-eval) - 研究自动化：可重复的评估工具以及 Jev Ultrafast 研究浏览器任务的现场注释，带有 QC 案例、套件运行程序和报告生成器。
- [Jev judge call vs dimension scores](https://agentjournal.dev/blog/llm-judge-vs-feature-extraction/) - 模型评估：针对 12-14 个 Jev 评分维度，在三个分类任务上使用局部拟合权重，测试每行一个直接 Jev 问题，在日语 NLI 上达到 0.9076，而在日语 NLI 上达到 0.8373，但将大约 25 倍以上的硬良性行标记为攻击。
- [Jev Pong](https://github.com/ably-labs/jev-pong) - 模型比较：乒乓球根据模型决策前进一步，让 Jev 通过 Vercel AI Gateway 与法学硕士进行正面交锋。
- [Jev reranking is not a free win](https://x.com/GoSailGlobal/status/2100877682972258619) - 搜索重新排名：对 33,047 个目录条目、164 个真实查询和 9,831 个分级对的测量运行表明，仅靠 Jev 重新排名并不能击败矢量检索。
- [An early-access test of TypeSafe's Jev](https://lindfors.no/blog/a-first-look-at-typesafes-jev/) - 独立试验：衡量对早期访问 Jev 的校准判断，并报告每个决定的最终成本。
- [jevcal](https://github.com/abhixhek/jevcal) - 模型评估：将每个问题的置信度阈值与您自己的标记数据的目标准确性相匹配，在保留的拆分上进行验证，报告仍有多少流量需要升级到 LLM，并在模型更新突破锁定阈值时使 CI 失败。
- [WindTunnel](https://github.com/nekuda-ai/WindTunnel) - 浏览器代理基准测试：针对其他浏览器代理接口测量 WebMCP，其中 Jev 作为比较配置之一。
- [jev-eval](https://github.com/Shogo-nfrealmusic/jev-eval) - 第三方检查：在相同判断任务的相同条件下将 Jev 与 GPT-4o-mini 和 Claude Sonnet 4.5 进行比较。
- [minutes](https://github.com/silverstein/minutes) - 会议记录：本地优先的转录应用程序，其实时语音路径通过 Jev 运行其评估。
- [jev-orderby-bench](https://github.com/yodablocks/jev-orderby-bench) - 模型评估：测量在 jev-1.13.0 传递 20 个新闻组主题并未能满足 Amazon ESCI 产品相关性的六个条件中的四个条件的预注册门下，对 Jev 概率的 SQL ORDER BY 是否合理（成对反转、针对人类评分的分数序数、校准、措辞不变量、排序键联系），并显示 DuckDB 扩展的默认 40 行批处理失败每个请求一行通过的排名门。
- [jev-ood-calibration](https://github.com/scienthoon/jev-ood-calibration) - 模型评估：Jev 对 900 个规则生成的支持票证进行独立校准测试，它无法看到，再加上三个公共基准，发布每个原始响应、针对模拟本底噪声的 ECE、温度改装以及每种类型的错误校准标志（选择和分数过度自信，布尔自信不足）。
- [BTK audit studies](https://boringtoolskit.com/blog/seo-audit-cost-2026/) - 内容和增长：Jev 惊人的距离分类排名 SEO 修复并驱动研究页面；每次运行判断 1,204 个页面，3 分钟内判断 4,816 个，每 12 个查询批次 0.0048 美元。
- [Can Jev Be a Better Agent Evaluator?](https://www.langchain.com/blog/jev-agent-evals-langsmith) - 代理评估：LangChain 将 Jev 与 LLM 法官在准确性、可重复性、延迟和成本方面进行比较，得出结论 Jev 是在线评估中更便宜且更一致的法官。
