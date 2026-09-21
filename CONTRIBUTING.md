# 参与贡献

欢迎补充公开、可复核的 Jev/System One 实践，或改进日志 skill。

## 条目要求

- 保留原始 URL、项目作者/组织和检索日期。
- 明确 Jev 实际做出的 `Choice`、`Score`、`Boolean` 或 `Noul` 决策。
- 把“公开实现”“技术观点”“待核验线索”分别放入分类页或 `research/sources.md`。
- 不把 GitHub star、宣传语或单条社交帖当作质量证明。

## skill 代码要求

- 默认本地运行，不上传原始日志。
- 输出必须可回指脱敏日志行和来源文件。
- 低置信度、超时和不适用场景应保留为人工复核，而不是自动执行。
- 新增行为字段时更新 `schema` 说明和离线示例。

提交前运行：

```bash
python3 -m py_compile skill/jev-practice-recommender/recommend.py
python3 skill/jev-practice-recommender/recommend.py \\
  skill/jev-practice-recommender/examples/sample-agent.jsonl \\
  --output /tmp/jev-recommendations.json
git diff --check
```
