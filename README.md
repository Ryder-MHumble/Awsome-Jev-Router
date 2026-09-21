# Awsome-Jev-Router

> **把 Agent 日志里的重复判断，路由到可复用的 Jev 实践。**

[![Jev](https://img.shields.io/badge/TypeSafe-Jev-0d9488)](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
[![目录](https://img.shields.io/badge/目录-14%20类-2563eb)](categories/)
[![Skill](https://img.shields.io/badge/Skill-本地优先-16a34a)](skill/jev-practice-recommender/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

**中文**（当前） · [English](README.en.md) · [目录](#目录) · [贡献](CONTRIBUTING.md)

Awsome-Jev-Router 是一个双层目录：一层收录公开的 Jev/System One 项目、SDK、工程模式和实践讨论；另一层把本地 Agent 日志归纳为高频任务，并给出可追溯的实践候选。适合在选择模型、路由技能、验证工具调用或设计工作流之前，先找到已有实现，再决定是否复用。

## 30 秒了解

```text
Agent 日志 → 本地脱敏 → 高频场景 → Jev 实践候选 → 来源与证据
```

Jev 接收状态和类型化问题，返回 `Choice`、`Score`、`Noul` 等结构化判断。Awsome-Jev-Router 把阈值、升级和副作用控制留在业务代码中：推荐是线索，不是自动执行。

## 快速开始

从仓库根目录运行本地 skill：

```bash
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
```

支持 JSONL、JSON 导出和普通文本日志。输出包含场景频次、匹配信号、脱敏摘录、行号、候选项目及来源文件。

把 `skill/jev-practice-recommender/` 复制到 Codex、Claude Code、Pi 或自建 Agent 的 skill 目录即可挂载。输入日志只在本机读取，默认不联网、不安装、不执行被推荐项目。

详细输入格式与隐私边界：[`SKILL.md`](skill/jev-practice-recommender/SKILL.md) · [English skill guide](skill/jev-practice-recommender/SKILL.en.md)

## 精选实践

完整目录目前有 256 个条目；首页每类选一个最能说明 Jev 用法的代表项目，完整清单仍在分类页。

| 分类 | 项目 | Jev 做什么 | 适合借鉴 |
| --- | --- | --- | --- |
| 分类与路由 | [jev-logtriage](https://github.com/jyatesdotdev/jev-logtriage) | 对 Loki 日志执行 `Noul`、`Score`、`Choice`，映射为 suppress/watch/review/notify/page，低置信度转 review。 | 把日志变成分级处置，而不是只生成摘要。 |
| 验证与护栏 | [jev-axi](https://github.com/shiftynick/jev-axi) | 在 PreToolUse 阶段评估命令的破坏性、外泄、远程执行和安全弱化。 | 在 Agent 产生副作用前增加安全门。 |
| 评分与排序 | [citation-verifier](https://github.com/MarissaFamularo/citation-verifier) | Claude 找证据，Jev 评分论文是否支持句子，人类保留最终裁决。 | 将机器评分与人工复核拆开。 |
| Agent 决策 | [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) | 根据浏览器状态和候选控件选择下一步动作，仅在需要输入文本时调用语言模型。 | 让 LLM 负责理解，Jev 负责高频动作选择。 |
| 数据标注与整理 | [jev-align](https://github.com/sutro-sh/jev-align) | 对 CSV、Parquet、JSONL 行作类型化判断，把歧义样本交给人并用修正标签优化定义。 | 构建可审计的人机协同标注。 |
| 评测与基准 | [jevcal](https://github.com/abhixhek/jevcal) | 在标注集上拟合置信度阈值，用留出集验证，阈值失效时让 CI 失败。 | 把低置信升级规则变成回归测试。 |
| 校准与研究 | [Laya](https://github.com/NandhaKishorM/laya) | 单次前向输出 `Choice`、`Score`、`Noul` 概率。 | 本地研究低延迟、隐私和离线决策模型。 |
| 基础设施、SDK 与集成 | [typesafe-ai/skills](https://github.com/typesafe-ai/skills) | 通过可安装 skill 教 Agent 何时把判断交给 Jev。 | 把 Jev 能力挂载到现有 Agent。 |
| 游戏与仿真 | [jev-plays-pokemon-red](https://github.com/valentynkit/jev-plays-pokemon-red) | 确定性代码负责路线和算术，Jev 只在分支和战斗节点选择，并用 Brier 评分。 | 将模型限制在可验证的小决策点。 |
| 金融与交易 | [Jev X Sentiment Analysis](https://github.com/brainstormity/Jev-X-Sentiment-Analysis) | 将去重后的推文证据转为入场区间、止损和目标决策卡，不直接交易。 | 把社交信号变成可审阅建议。 |
| 合规与法律 | [LegalForecast-MTD](https://github.com/johnhughes3/LegalForecastBench) | 预测驳回动议结果，并用 micro-Brier 评估概率质量。 | 把法律建议与不确定性分开。 |
| 内容审核 | [mastra-jev-moderation](https://github.com/CodeAlive-AI/mastra-jev-moderation) | 一次请求判断是否拦截及违规类别，并用超时、熔断器和阈值控制风险。 | 构建低延迟、可回退的审核链路。 |
| 科研流水线 | 暂无核心条目 | 当前没有直接相关的实验门控或科学结果验证项目。 | 保持空缺，避免用不相关项目填充。 |
| 相关实践与讨论 | [Jev is a really smart switch statement](https://x.com/NathanFlurry/status/2100036101809619314) | 将 Jev 解释为输入上下文、输出受约束分支的决策层。 | 快速理解 Jev 与聊天模型的边界。 |

每个条目都说明“Jev 判断什么”和“代码负责什么”；更多项目、作者和来源见对应分类页与 [研究资料](research/sources.md)。

## 目录

| 标签 | 条目* | 适合查找 |
| --- | ---: | --- |
| [分类与路由](categories/classification-routing.md) | 24 | 意图、请求、技能、模型和流量路由 |
| [验证与护栏](categories/verification-guardrails.md) | 22 | 工具调用、权限、代码与供应链检查 |
| [评分与排序](categories/scoring-ranking.md) | 20 | 质量、相关性、风险和候选排序 |
| [Agent 决策](categories/agent-decisions.md) | 31 | 浏览器、上下文、动作和工作流决策 |
| [数据标注与整理](categories/data-labeling-curation.md) | 5 | 文档、数据集和内容标注 |
| [评测与基准](categories/evaluation-benchmarking.md) | 16 | 评测、回归、可复现实验 |
| [校准与研究](categories/calibration-research.md) | 22 | 置信度、延迟、模型和方法研究 |
| [基础设施、SDK 与集成](categories/infra-sdks-integrations.md) | 43 | API、网关、SDK、部署与适配器 |
| [游戏与仿真](categories/game-simulation.md) | 10 | 游戏、世界模型和模拟环境 |
| [金融与交易](categories/finance-trading.md) | 4 | 交易、组合和风控判断 |
| [合规与法律](categories/compliance-legal.md) | 1 | 合规、合同和法律工作流 |
| [内容审核](categories/content-moderation.md) | 4 | 垃圾、广告、滥用和安全内容判断 |
| [科研流水线](categories/scientific-pipelines.md) | 0 | 科研数据与实验流程 |
| [相关实践与讨论](categories/related-practices-discussions.md) | 54 | X、博客、访谈和暂无代码的公开实践信号 |

\* 条目数按目录页当前内容统计；一个项目只归入一个主分类。中文镜像见 [`categories/zh-CN/`](categories/zh-CN/)。

## 按问题选择

| 你的问题 | 先看 |
| --- | --- |
| “这个请求应该交给哪个模型或技能？” | 分类与路由、Agent 决策 |
| “这个工具调用是否允许执行？” | 验证与护栏、合规与法律 |
| “候选结果哪个更相关、更安全？” | 评分与排序、评测与基准 |
| “如何接入 Jev 或替换供应商？” | 基础设施、SDK 与集成 |
| “有没有真实项目或作者观点？” | 相关实践与讨论、研究资料 |

## 研究资料

- [研究资料（中文）](research/sources.md)
- [Research sources (English)](research/sources.en.md)
- [来源政策](docs/source-policy.md) · [归属说明](ATTRIBUTION.md)

研究记录官方资料、开源项目、技术文章和公开社交讨论，并区分“可运行实现”“公开观点”和“待核查线索”。价格、模型别名、性能和平台能力可能变化；采用前请打开原始来源复核。

## 收录标准

- 来源公开、可引用，并明确使用 Jev 或 System One 类型化决策。
- 摘要说明具体场景、判断类型和实现价值。
- 纯观点、无法核验的宣传和只在名称上类似 Jev 的项目不进入实践条目，可进入讨论章节并标明证据强度。
- 收录不代表代码质量、安全性、稳定性、性能或许可证背书。

发现过时、重复或证据不足的条目？请提交 Issue 或 PR，并附原始链接和核验依据。见 [贡献指南](CONTRIBUTING.md)。

## 验证

```bash
python3 -m py_compile skill/jev-practice-recommender/recommend.py
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
git diff --check
```

## 许可证

新增代码和文档采用 MIT，见 [LICENSE](LICENSE)。目录中的第三方项目、名称、作者、链接和内容仍受其各自许可证与原发布者权利约束。
