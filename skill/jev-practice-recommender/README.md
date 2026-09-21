# Jev Practice Recommender Skill

一个离线 skill：从 agent 日志中识别重复任务，脱敏后将高频场景映射到本仓库中的 Jev 实践，并保留证据链。

## 本地演示

```bash
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
```

演示输入故意包含一个假 token、邮箱和绝对路径；可在输出中确认它们不会原样出现。脚本只使用 Python 标准库，不访问网络。

## 设计取舍

这是一个最小可用的本地基线：规则透明、结果可复核、无需数据库和模型服务。它牺牲了语义召回率，换取日志不出本机和推荐理由可解释。若后续需要更强的语义聚类，可在 `classify` 之后增加离线模型适配器，并保留当前 `evidence` 契约。
