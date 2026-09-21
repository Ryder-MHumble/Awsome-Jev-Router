# Jev Practice Recommender Skill

**Language:** English (current) · [中文](README.md)

An offline skill that identifies repeated tasks in agent logs, redacts them locally, and maps frequent scenarios to reusable Jev practices in this repository.

## Local demo

```bash
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
```

The sample input deliberately contains a fake token, an email address, and an absolute path. Inspect the output to confirm that they are not reproduced. The script uses only the Python standard library and makes no network request.

## Design trade-off

This is a small local baseline: rules are transparent, results are reviewable, and no database or model service is required. It trades semantic recall for keeping logs on the machine and making recommendation reasons inspectable. An offline semantic adapter may be added after `classify`, while preserving the current `evidence` contract.

See the [full English skill contract](SKILL.en.md) or the [中文版本](SKILL.md).
