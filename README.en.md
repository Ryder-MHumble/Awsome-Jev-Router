# Jev Practice Radar

**Language:** English (current) · [中文](README.md)

Jev Practice Radar turns public Jev/System One practices into a searchable catalog and provides a mountable local skill. The skill reads an agent's local logs, identifies recurring task patterns, and maps them to Jev practices that may be reusable.

It answers a concrete question beyond bookmarking links: when an agent repeatedly handles routing, permission checks, quality scoring, context compaction, or data curation, which Jev patterns are relevant, why did they match, and which redacted log lines support the recommendation?

## Capabilities

```text
agent logs
    ↓ local parsing and redaction
recurring behaviors / task patterns
    ↓ transparent rule matching
Jev practice catalog
    ↓ source and log evidence
reviewable practice recommendations
```

- **Mountable:** `skill/jev-practice-recommender/` is an independent skill that can be copied into Codex, Claude Code, Pi, or a custom agent skill directory.
- **Local-first:** log analysis is offline by default. API keys, bearer tokens, email addresses, phone numbers, and common absolute paths are redacted before output.
- **Explainable:** each recommendation includes frequency, trigger signals, a redacted excerpt, line number, source category, and original URL.
- **Replaceable:** the baseline uses the standard library and transparent keyword rules. An offline semantic adapter can be added later without bypassing redaction or source review.
- **Evidence-led:** category pages are indexes for further investigation. They are not quality, security, stability, or license endorsements.

## Quick start

Run this from the repository root:

```bash
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
```

The input accepts JSONL, JSON exports, and plain text logs. The output contains scenario frequency, candidate practices, and an evidence trail.

See the [English skill guide](skill/jev-practice-recommender/SKILL.en.md) for the input contract, privacy boundary, and extension points. The local demo does not access the network or execute a recommendation.

## Practice catalog

The English category pages are kept in `categories/`. Chinese readers can use the translated mirrors in [`categories/zh-CN/`](categories/zh-CN/).

- [Classification and routing](categories/classification-routing.md)
- [Verification and guardrails](categories/verification-guardrails.md)
- [Scoring and ranking](categories/scoring-ranking.md)
- [Agent decisions](categories/agent-decisions.md)
- [Data labeling and curation](categories/data-labeling-curation.md)
- [Evaluation and benchmarking](categories/evaluation-benchmarking.md)
- [Calibration and research](categories/calibration-research.md)
- [Infrastructure and integrations](categories/infra-sdks-integrations.md)
- [Game and simulation](categories/game-simulation.md)
- [Finance and trading](categories/finance-trading.md)
- [Compliance and legal](categories/compliance-legal.md)
- [Content moderation](categories/content-moderation.md)
- [Scientific pipelines](categories/scientific-pipelines.md)
- [Related practices and discussions](categories/related-practices-discussions.md)

Entries come from public pages. Project names, authors, organizations, and links belong to their original publishers. An entry means “review this source,” not “adopt or endorse it.”

## Research sources

[research/sources.en.md](research/sources.en.md) records official material, open-source projects, technical writing, and public social discussions. Each record includes a retrieval date, link, claim summary, reusable pattern, and evidence strength. The research chapter is maintained separately from the category index so that public discussion can be distinguished from runnable implementation.

## Why Jev

Jev/System One is designed for typed decisions: given unstructured state and a typed question, it returns a typed result such as `Choice`, `Score`, or `Boolean`, often with confidence. Application code owns thresholds, abstention, escalation, and side effects. This makes Jev useful for narrow, repeated, auditable judgments inside an agent.

This project applies that idea at two levels: the catalog shows reusable decision patterns, while the log skill discovers which recurring user tasks may benefit from typed decisions. Recommendations remain candidates. Users must inspect source code, tests, data claims, and license terms before adoption.

## Privacy and safety

- Logs are read locally; the script does not make network requests by default.
- Redaction is a heuristic baseline, not a complete DLP system. Clean custom credentials, binary logs, and team-specific fields offline first.
- Raw logs are not written to the repository. Output keeps only bounded redacted excerpts and line numbers.
- The skill never installs, invokes, or executes a recommended project and never decides whether a tool call is allowed.

## Sources and license

This is an independent derivative project built from public sources with a new local log-analysis skill. See [docs/source-policy.en.md](docs/source-policy.en.md) and [ATTRIBUTION.en.md](ATTRIBUTION.en.md) for source and verification rules. Linked third-party projects keep their own licenses.

New code and documentation are MIT licensed; see [LICENSE](LICENSE).

## Development and verification

```bash
python3 -m py_compile skill/jev-practice-recommender/recommend.py
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
git diff --check
```

Before submitting, inspect `privacy.network`, redaction output, and the evidence chain. Do not commit real logs, tokens, or personal information.
