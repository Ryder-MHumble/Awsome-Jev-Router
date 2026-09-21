# Jev Practice Recommender

**语言 / Language:** 中文（当前） · [English](SKILL.en.md)

语言：中文 | [English](SKILL.en.md)

把 agent 的本地运行日志转换成可审计的 Jev 实践推荐。它适合作为一个 skill 挂载在 Codex、Claude Code、Pi 或自建 agent 上：先总结用户反复出现的任务场景，再从本仓库的 `categories/*.md` 中给出可复用的实践。

## 能力边界

- 支持 JSONL、JSON 导出和普通文本日志；常见的 `messages`、`events`、`conversation` 字段会自动展开。
- 在本地完成脱敏：API key/token、Bearer、邮箱、手机号、带凭据 URL 和常见绝对路径会替换为占位符。
- 用可解释的关键词规则归纳高频场景，并返回频次、触发信号、原始行号和脱敏摘录。
- 从当前仓库的分类文件读取实践，输出实践名称、URL、来源文件、匹配理由和分数。
- 默认零网络、零写入日志；推荐结果是候选，采用前必须打开来源自行复核。

## 挂载约定

将本目录作为 agent skill 目录挂载，并让 agent 在需要时运行：

```bash
python3 skill/jev-practice-recommender/recommend.py ./session.jsonl \
  --output ./jev-recommendations.json
```

输入日志只在本地读取。建议把输出作为下一轮 agent 的上下文，而不是把完整日志发给模型。`schema` 字段当前为 `jev-practice-recommender/v1`，后续可在不改变输入的情况下增加字段。

## 输出中的证据链

每个场景包含 `frequency`、`recommendations` 和 `evidence`。`evidence` 的每项至少有脱敏后的 `line`、`excerpt`、`signals`；推荐项带 `source`，例如 `categories/verification-guardrails.md`。这使用户能从推荐回到日志触发点，再回到实践目录核查。

## 隐私与限制

脱敏是保守的启发式规则，不是完整 DLP 系统；自定义凭据格式和二进制导出需要先在本地清洗。场景识别当前是可审计的关键词基线，低频或含混表达可能没有推荐。脚本不会声称日志证明了某种能力，也不会自动执行推荐实践。
