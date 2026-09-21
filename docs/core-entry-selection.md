# 首页核心条目选择

本文件为中英文 README 提供首页级推荐。完整目录仍保留在 `categories/`；首页每类只放一个最能说明使用边界、可迁移性和证据质量的条目，避免用长清单掩盖决策价值。

| 分类 | 核心项目 | URL | Jev 做什么决策 | 用户价值 | 选择理由 |
|---|---|---|---|---|---|
| Agent Decisions | Jev Ultrafast | https://github.com/browser-use/jev-ultrafast | 根据浏览器状态和候选控件选择下一步动作，仅在需要输入文本时调用语言模型。 | 将高频浏览动作从慢速生成循环中拆出，降低延迟和成本。 | 最直观地体现“LLM 负责理解，Jev 负责下一步选择”。 |
| Calibration & Research | Laya | https://github.com/NandhaKishorM/laya | 单次前向输出 `Choice`、`Score`、`Noul` 概率。 | 可在本地运行低延迟决策模型，适合隐私、成本和离线场景。 | 有公开模型、约 35 ms 推理和可安装包，复现门槛低。 |
| Classification & Routing | jev-logtriage | https://github.com/jyatesdotdev/jev-logtriage | 对 Loki 日志执行 `Noul`、`Score`、`Choice`，映射为 suppress/watch/review/notify/page，低置信度转 review。 | 把 Agent 或系统日志变成可执行的分级处置，而不是只生成摘要。 | 与本项目“读取日志并推荐实践”的目标最接近，且包含明确升级路径。 |
| Compliance & Legal | LegalForecast-MTD | https://github.com/johnhughes3/LegalForecastBench | 根据法官书面记录预测驳回动议结果，并用 micro-Brier 评估概率质量。 | 将法律建议与概率不确定性分开，便于审阅和校准。 | 该分类唯一直接条目，且评估指标明确。 |
| Content Moderation | mastra-jev-moderation | https://github.com/CodeAlive-AI/mastra-jev-moderation | 一次请求判断是否拦截及类别，超过 0.7 才中止；超时和熔断器定义故障行为。 | 低延迟、低成本阻断恶意输入，同时保持服务可用。 | 报告 9/9 hostile、0/49 正常消息和约 0.4 s 中位数，证据密度高。 |
| Data Labeling & Curation | jev-align | https://github.com/sutro-sh/jev-align | 对 CSV、Parquet、JSONL 行作 `Choice`、`Score` 或 `Boolean` 判断，歧义样本交给人并用修正标签优化定义。 | 持续改善数据分类规则，而非一次性批量打标。 | 同时具备人机协同、审计抽样和 GEPA 优化。 |
| Evaluation & Benchmarking | jevcal | https://github.com/abhixhek/jevcal | 在标注集上拟合问题级置信度阈值，用留出集验证；模型更新破坏阈值时失败 CI。 | 把低置信度升级规则变成可测试门槛。 | 直接覆盖本项目最需要的可信度治理和回归检测。 |
| Finance & Trading | Jev X Sentiment Analysis | https://github.com/brainstormity/Jev-X-Sentiment-Analysis | 将去重后的推文证据转为入场区间、止损和目标的决策卡，不直接执行交易。 | 将社交信号压缩为可审阅建议，保留人工确认边界。 | 比自动下单更适合作为可迁移的风险受控模式。 |
| Game & Simulation | jev-plays-pokemon-red | https://github.com/valentynkit/jev-plays-pokemon-red | 确定性代码负责路线和算术，Jev 只在分支和战斗节点选择；每回合预测用 Brier 评分。 | 把模型限制在可验证的小决策点。 | 同时展示职责分离、可测量预测和失败边界。 |
| Infra, SDKs & Integrations | typesafe-ai/skills | https://github.com/typesafe-ai/skills | 通过可安装 skill 教 Agent 何时把判断交给 Jev。 | 可把 Jev 能力挂载到已有 Agent。 | 与 Awsome-Jev-Router 的 skill 路由目标完全一致，适合作为入口实现。 |
| Related Practices & Discussions | Jev is a really smart switch statement | https://x.com/NathanFlurry/status/2100036101809619314 | 将 Jev 解释为受约束的 switch statement：输入上下文，输出分支。 | 帮用户快速建立“决策层而非聊天模型”的心智模型。 | 说法短而准确，能纠正“替代 GPT/Claude”的误解。 |
| Scoring & Ranking | citation-verifier | https://github.com/MarissaFamularo/citation-verifier | Claude 定位引文证据，Jev 评分句子是否被论文支持，人类保留最终裁决。 | 将事实核验拆成机器评分和人工复核，降低错误发布风险。 | 展示了多模型职责分离和高价值证据核验。 |
| Verification & Guardrails | jev-axi | https://github.com/shiftynick/jev-axi | PreToolUse 阶段对 shell 命令的破坏性、外泄、远程执行和安全弱化进行评分，决定放行或拦截。 | 在 Agent 产生副作用前增加低延迟安全门。 | 仓库公开了 44/44 标注工具调用测试，验证证据清晰。 |
| Scientific Pipelines | 暂无核心条目 | — | 当前没有直接相关的实验门控或科学结果验证项目。 | 避免用不相关项目填充分类，保持目录可信。 | 后续优先收录有实验数据、假设筛选或可复现实验脚本的项目。 |

## README 展示规则

每个分类在首页展示上表的一行，字段顺序固定为“项目—解决的问题—Jev 决策”。分类标题链接到对应完整分类页，完整条目、作者与来源归属继续保留在分类页和 `ATTRIBUTION.md`。首页不复制本文件的全部选择理由，以保持可扫描性。
