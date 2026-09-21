# 评分与排名

**语言 / Language:** 中文（当前） · [English](../scoring-ranking.md)

对于 Jev 生成评分标准、质量等级或推动下游决策的相关性和优先级排序的项目，请使用此类别。

## 提交格式

```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```

## 条目

- [Clean Code Judge](https://github.com/frostney/clean-code-review) - 代码质量：对 31 个布尔清洁代码气味以及函数大小和嵌套的拉取请求的每个文件进行评分，然后将结论交给写作模型以进行审查散文。
- [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) - 学术出版：检查每篇被引用的论文是否真正支持引用它的句子，克劳德找到引用，杰夫评分支持，最后由人工做出决定。
- [jev-bfs](https://github.com/komikat/jev-bfs) - 搜索工具：通过让 Jev 对每个页面的传出链接进行排名，同时由 Python 控制搜索，来查找英文维基百科文章之间的链接路径。
- [Jev Search](https://github.com/superagents-lab/jev-search) - Web 搜索：使用 Jev Noul 对结果标题和片段的判断，按相关性对 Search1API 结果进行排名，应用程序代码合并重复的 URL 并分别对得分较低的匹配项进行分组。
- [pagegrade](https://github.com/kitze/pagegrade) - 内容质量：使用 Jev 对页面部分的清晰度、写作和页面 SEO 进行评分，并返回每个部分的分数。
- [jev-scout](https://github.com/AkashPriyadarshii/jev-scout) - 开发人员工具：亚秒级零幻觉开源存储库和使用 TypeSafe Jev 推测扇出评分的 crate scout。
- [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) - 零成本、代理优先的 SEO 和生成引擎优化 (GEO) 搜索雷达 CLI 套件和 MCP 服务器，由 DuckDuckGo 和 TypeSafe Jev System One 提供支持。
- [JevSlop](https://github.com/TKY-27/JevSlop) - 写作质量：对单个 `systemOne` 请求中的八个 Jev `Score` 轴上的公共 note.com 文章进行评分，并将其转换为普通 TypeScript 中的 0-100 Slop Score。
- [SemanticSpace](https://semanticspace.dev/) - 语义映射：通过询问 Jev 每个短语与两个选定轴概念的相关程度有多强，并使用这些分数作为坐标，将短语置于 2D 中。
- [Supercov](https://github.com/supercorp-ai/supercov) - 编码代理的代码质量：Jev 回答每个源文件的 12 个 `Noul` 属性，以便代理知道首先要修复什么。
- [jev.nvim](https://github.com/valentynkit/jev.nvim) - 开发人员工具：Neovim 插件，使用 Treesitter 将缓冲区拆分为多个函数，使用 Jev 对每个简单语言问题进行评分，并在 Quickfix 中按概率对答案进行排名。
- [jev-reranker](https://github.com/hotchpotch/jev-reranker) - 检索和 RAG：使用 Jev Noul 判断来评估检索到的文档作为答案证据的相关性和有用性，然后对结果进行排序，并可选择使用可配置的阈值对其进行过滤。
- [Jev Reranker (Rust CLI)](https://github.com/shinpr/jev-reranker) - 检索和 RAG：JSON 输入/JSON 输出 CLI，使用单独的 Jev `Noul` 检查对候选者进行排名、应用证据阈值或提取源文本，同时保持这些决策的独立性。
- [jev-skip](https://github.com/valentynkit/jev-skip) - 媒体：浏览器扩展，可读取 YouTube 字幕轨道，并在介绍结束前对搜索栏上每个片段的赞助商概率进行评分，报告 SponsorBlock 的赞助商秒数中有 77% 捕获了超过 23 个视频，每个视频 0.0008 美元。
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) - 语义搜索：按跨语言的含义进行 grep，让 Jev 根据含义对每一行进行评分，并让含义与 AND 结合，由 13 个文件的测试套件支持。
- [nlgrep](https://github.com/YehuiTang0316/jev-nlgrep) - 开发人员工具：使用 Jev `Noul` 判断来查找满足自然语言条件的代码、文档、日志和文本，并具有可配置的概率阈值和链接到源行的排名文件结果。
- [slop-grader](https://github.com/lukstei/slop-grader) - 内容质量：CLI 工具，使用 Jev 分数和行级标志根据 AI 语法、语法和技术文档质量的自定义规则集对文本文件进行评分，然后指导 AI 代理自动修复违规行为。
- [jselect](https://github.com/keltokhy/jselect) - 研究和检索：使用 Jev Noul 相关性判断和本地多样性意识选择在代币预算内选择与源相关的证据。
- [jsort](https://github.com/keltokhy/jsort) - 文本测量：使用成对的 Jev Noul 比较和本地拟合的 Bradley-Terry 量表，按照简单英语标准对文本进行排名。
- [jgrep (kyu1204)](https://github.com/kyu1204/jgrep) - 开发人员工具：语义 grep，要求 Jev 每 5-60 行代码块、diff hunk 或 CSV 行（每个请求 16 行）输入一个 Noul，并打印 grep 样式文件：行命中超过阈值，因此英语句子可以用作 CI lint 规则。
