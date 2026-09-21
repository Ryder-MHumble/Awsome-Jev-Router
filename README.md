# Jev 实践导航

**语言 / Language:** 中文（当前） · [English](README.en.md)

Jev 实践导航（`jev-practice-radar`）把公开的 Jev/System One 实践整理成可检索目录，并提供一个可以挂载到 agent 的本地 skill：读取 agent 日志，识别用户反复出现的任务场景，再把这些场景映射到已有的 Jev 实践。

它解决的是一个比“收藏链接”更具体的问题：当一个 agent 反复遇到路由、权限判断、质量评分、上下文压缩或数据整理任务时，用户能看到哪些成熟的 Jev 模式可以复用，为什么匹配，以及推荐是由哪几行脱敏日志触发的。

## 项目能力

```text
agent 日志
    ↓ 本地读取与脱敏
高频行为 / 任务场景
    ↓ 透明规则匹配
Jev 实践目录
    ↓ 来源与日志证据链
可复核的实践推荐
```

- **可挂载**：`skill/jev-practice-recommender/` 是独立 skill，可复制到 Codex、Claude Code、Pi 或自建 agent 的 skill 目录。
- **本地优先**：日志分析默认零网络、零上传，API key、Bearer token、邮箱、手机号和常见绝对路径会在输出前脱敏。
- **可解释**：每条推荐都包含场景频次、触发信号、脱敏摘录、日志行号、来源分类和原始 URL。
- **可替换**：当前使用标准库和透明关键词规则作为基线；后续可接入离线语义聚类，但不能绕过本地脱敏和来源复核。
- **证据导向**：分类页是实践索引，不代表项目质量、稳定性、安全性或许可证适用性；采用前应打开来源自行验证。

## 立即运行

在仓库根目录执行：

```bash
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
```

输入支持 JSONL、JSON 导出和普通文本日志。示例输出包含场景频次、推荐项目和证据链：

```json
{
  "schema": "jev-practice-recommender/v1",
  "privacy": {"network": false, "redacted": true},
  "scenarios": [
    {
      "scenario": "verification-guardrails",
      "frequency": 3,
      "recommendations": [{"name": "...", "source": "categories/verification-guardrails.md"}],
      "evidence": [{"line": 4, "excerpt": "...", "signals": ["权限"]}]
    }
  ]
}
```

完整输入约定、隐私边界和扩展方式见 [skill/jev-practice-recommender/SKILL.md](skill/jev-practice-recommender/SKILL.md)。本地演示不访问网络，也不会自动执行任何推荐。

## 实践目录

英文条目与中文入口：[`categories/`](categories/) · [中文分类入口](categories/zh-CN/README.md)

`categories/` 保留公开项目、工程实践和讨论线索，并按 Jev 实际做出的决策分类：

- [分类与路由](categories/classification-routing.md)
- [验证与护栏](categories/verification-guardrails.md)
- [评分与排序](categories/scoring-ranking.md)
- [Agent 决策](categories/agent-decisions.md)
- [数据标注与整理](categories/data-labeling-curation.md)
- [评测与基准](categories/evaluation-benchmarking.md)
- [校准与研究](categories/calibration-research.md)
- [基础设施与集成](categories/infra-sdks-integrations.md)
- [游戏与仿真](categories/game-simulation.md)、[金融与交易](categories/finance-trading.md)、[合规与法律](categories/compliance-legal.md)、[内容审核](categories/content-moderation.md)、[科研流水线](categories/scientific-pipelines.md)
- [相关实践与讨论](categories/related-practices-discussions.md)

目录条目来自公开页面；项目名称、作者/组织和链接归原发布者所有。条目只说明“值得进一步核查”，不构成推荐或背书。

## 研究资料

[research/sources.md](research/sources.md) 独立记录官方资料、开源项目、技术博客和公开社交讨论，包含检索日期、链接、观点摘要、可迁移模式和证据强度。研究章节与分类目录分开维护，便于把“有人提到”与“有公开实现”区分开。

## 为什么使用 Jev

Jev/System One 面向的是类型化决策：输入非结构化状态和一个有明确类型的问题，返回 `Choice`、`Score`、`Boolean` 等类型化结果及置信度。应用代码决定阈值、拒绝、升级和副作用，因此适合把 agent 中重复、窄范围、需要审计的判断从自由文本生成中拆出来。

本项目把这个思想落实到两个层面：分类目录展示可迁移的决策模式，日志 skill 则从真实使用行为中发现“哪些判断值得被类型化”。推荐结果始终是候选，最终采用仍由用户检查源代码、测试、数据声明和许可证。

## 隐私与安全

- 日志只在本机读取，脚本默认不发起网络请求。
- 脱敏是启发式基线，不是完整 DLP；未知凭据格式、二进制日志和团队自定义字段应先离线清洗。
- 原始日志不写入仓库；输出只保留有限长度的脱敏摘录和行号。
- skill 不会自动调用、安装或执行推荐项目，也不会替用户决定是否允许某个工具调用。

## 来源与许可证

本仓库是基于公开来源整理并新增日志分析能力的独立衍生项目。来源与核验规则见 [docs/source-policy.md](docs/source-policy.md) 与 [ATTRIBUTION.md](ATTRIBUTION.md)。分类页中的外部项目仍受其各自许可证约束。

新增代码与文档采用 MIT，详见 [LICENSE](LICENSE)。许可证不覆盖分类页所链接的第三方项目或外部内容。

## 开发与验证

```bash
python3 -m py_compile skill/jev-practice-recommender/recommend.py
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
git diff --check
```

提交前请检查输出中的 `privacy.network`、脱敏结果和证据链；不要把真实日志、token 或个人信息提交到仓库。
