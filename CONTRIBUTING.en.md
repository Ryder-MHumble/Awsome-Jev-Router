# Contributing

**Language:** English (current) · [中文](CONTRIBUTING.md)

Contributions of public, reviewable Jev/System One practices and improvements to the log skill are welcome.

## Entry requirements

- Keep the original URL, project author or organization, and retrieval date.
- State the actual `Choice`, `Score`, `Boolean`, or `Noul` decision made by Jev.
- Put runnable implementations, technical opinions, and unverified leads in category pages or `research/sources.en.md` respectively.
- Do not treat GitHub stars, marketing copy, or a single social post as proof of quality.

## Skill code requirements

- Run locally by default and never upload raw logs.
- Make every output traceable to a redacted log line and source file.
- Keep low-confidence, timeout, and not-applicable cases for human review instead of executing automatically.
- Update the schema description and offline example when adding behavior fields.

Before submitting:

```bash
python3 -m py_compile skill/jev-practice-recommender/recommend.py
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
git diff --check
```
