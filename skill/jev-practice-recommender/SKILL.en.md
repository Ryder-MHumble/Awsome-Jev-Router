# Jev Practice Recommender

**Language:** English (current) · [中文](SKILL.md)

Convert an agent's local run logs into auditable Jev practice recommendations. Mount this directory as a skill in Codex, Claude Code, Pi, or a custom agent. The skill summarizes recurring task patterns and searches `categories/*.md` for reusable practices.

## Capabilities and boundaries

- Accepts JSONL, JSON exports, and plain text logs; common `messages`, `events`, and `conversation` fields are expanded automatically.
- Redacts API keys/tokens, bearer credentials, email addresses, phone numbers, credential-bearing URLs, and common absolute paths locally.
- Uses explainable keyword rules to identify frequent scenarios and returns frequency, trigger signals, source line numbers, and redacted excerpts.
- Reads practices from this repository's category files and returns the practice name, URL, source file, match reason, and score.
- Defaults to zero network and zero log writes. A recommendation is a candidate and must be reviewed against its source before adoption.

## Mounting and invocation

Mount this directory as an agent skill and run:

```bash
python3 skill/jev-practice-recommender/recommend.py ./session.jsonl \
  --output ./jev-recommendations.json
```

Input logs are read locally. Pass the output as context for a later agent turn instead of sending the complete raw log to a model. The current schema is `jev-practice-recommender/v1`; fields may be added without changing the input contract.

## Evidence chain

Each scenario includes `frequency`, `recommendations`, and `evidence`. Every evidence item contains a redacted `line`, `excerpt`, and `signals`; every recommendation includes a `source`, such as `categories/verification-guardrails.md`. A user can therefore trace a recommendation back to its triggering log line and then to the catalog entry.

## Privacy and limitations

Redaction is a conservative heuristic, not a complete DLP system. Clean custom credential formats and binary exports locally first. Scenario detection is an auditable keyword baseline, so low-frequency or ambiguous language may produce no recommendation. The script never claims that logs prove a capability and never executes a recommended practice.
