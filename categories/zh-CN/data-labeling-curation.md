# 数据标签和管理

**语言 / Language:** 中文（当前） · [English](../data-labeling-curation.md)

将此类别用于 Jev 大规模注释、过滤、重复数据删除或分类数据的程序，以取代较慢或成本较高的人工和法学硕士标记步骤。

## 提交格式
```md
- [Name](URL) - Industry: one-sentence description of the Jev use case.
```
## 条目

- [jev-align (Sutro)](https://github.com/sutro-sh/jev-align) - 数据集工程：使用 Jev `Choice`、`Score` 或 `Boolean` 决策评估 CSV、Parquet 和 JSONL 行，将不明确的样本和审核样本发送给人工，并使用可接受的人工标签通过 GEPA 优化保存的定义。
- [jev-curate](https://github.com/AkashPriyadarshii/jev-curate) - 数据集工程：使用 Jev Noul 检查和校准置信度分数筛选合成 JSONL 和 Parquet 行，将通过的记录和拒绝的记录直接流式传输到磁盘。
- [typeful-triage](https://github.com/cephalization/jev-triage) - 开源维护：多人分类仪表板，Jev 在其中回答每个问题的一组固定的键入问题 - 类型、严重性、紧急性、重复和下一步 - 并且保留每个人工更正并在以后的运行中显示回模型。
- [jlink](https://github.com/keltokhy/jlink) - 研究数据：使用 Jev Noul 对判断在简单英语匹配规则下链接记录，并具有本地候选阻止和匹配解析。
- [jgrep](https://github.com/keltokhy/jgrep) - 数据过滤：使用 Jev Noul 判断，根据简单的英语描述过滤文本、结构化记录、函数和差异块。
