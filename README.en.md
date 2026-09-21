# Awsome-Jev-Router

> **Route repeated Agent judgments to reusable Jev practices.**

[![Jev](https://img.shields.io/badge/TypeSafe-Jev-0d9488)](https://typesafe.ai/blog/introducing-system-one-models-and-jev)
[![Catalog](https://img.shields.io/badge/catalog-14%20categories-2563eb)](categories/)
[![Skill](https://img.shields.io/badge/skill-local--first-16a34a)](skill/jev-practice-recommender/)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

[中文](README.md) · **English** · [Catalog](#catalog) · [Contributing](CONTRIBUTING.en.md)

Awsome-Jev-Router has two layers: a catalog of public Jev/System One projects, SDKs, engineering patterns, and practice discussions; and a local skill that turns recurring Agent-log tasks into traceable practice candidates. Use it to find an existing implementation before choosing a model, routing a skill, adding a tool gate, or designing a workflow.

## In 30 seconds

```text
Agent logs → local redaction → recurring scenarios → Jev candidates → sources and evidence
```

Jev takes state plus typed questions and returns structured judgments such as `Choice`, `Score`, and `Noul`. Awsome-Jev-Router leaves thresholds, escalation, and side effects in application code: a recommendation is a lead to review, never an automatic action.

## Quick start

Run the local skill from the repository root:

```bash
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
```

The input accepts JSONL, JSON exports, and plain text logs. The output contains scenario frequency, trigger signals, redacted excerpts, line numbers, candidate projects, and source files.

Copy `skill/jev-practice-recommender/` into a Codex, Claude Code, Pi, or custom Agent skill directory to mount it. Logs are read locally; the default run does not make network requests, install, or execute recommended projects.

Read the input contract and privacy boundary in [`SKILL.en.md`](skill/jev-practice-recommender/SKILL.en.md) · [中文 skill guide](skill/jev-practice-recommender/SKILL.md)

## Catalog

| Tag | Entries* | Use it for |
| --- | ---: | --- |
| [Classification & Routing](categories/classification-routing.md) | 24 | Intent, request, skill, model, and traffic routing |
| [Verification & Guardrails](categories/verification-guardrails.md) | 22 | Tool calls, permissions, code, and supply-chain checks |
| [Scoring & Ranking](categories/scoring-ranking.md) | 20 | Quality, relevance, risk, and candidate ranking |
| [Agent Decisions](categories/agent-decisions.md) | 31 | Browser, context, action, and workflow decisions |
| [Data Labeling & Curation](categories/data-labeling-curation.md) | 5 | Document, dataset, and content labeling |
| [Evaluation & Benchmarking](categories/evaluation-benchmarking.md) | 16 | Evaluation, regression, and reproducible experiments |
| [Calibration & Research](categories/calibration-research.md) | 22 | Confidence, latency, model, and method research |
| [Infrastructure, SDKs & Integrations](categories/infra-sdks-integrations.md) | 43 | APIs, gateways, SDKs, deployment, and adapters |
| [Game & Simulation](categories/game-simulation.md) | 10 | Games, world models, and simulated environments |
| [Finance & Trading](categories/finance-trading.md) | 4 | Trading, portfolio, and risk decisions |
| [Compliance & Legal](categories/compliance-legal.md) | 1 | Compliance, contracts, and legal workflows |
| [Content Moderation](categories/content-moderation.md) | 4 | Spam, ads, abuse, and safety judgments |
| [Scientific Pipelines](categories/scientific-pipelines.md) | 0 | Scientific data and experiment workflows |
| [Related Practices & Discussions](categories/related-practices-discussions.md) | 54 | X, blogs, interviews, and public signals without a standalone project |

\* Counts reflect the current category pages. Each project has one primary category. Chinese mirrors are in [`categories/zh-CN/`](categories/zh-CN/).

## Choose by problem

| Your question | Start with |
| --- | --- |
| “Which model or skill should handle this request?” | Classification & Routing; Agent Decisions |
| “Should this tool call be allowed?” | Verification & Guardrails; Compliance & Legal |
| “Which candidate is more relevant or safer?” | Scoring & Ranking; Evaluation & Benchmarking |
| “How do I connect Jev or swap a provider?” | Infrastructure, SDKs & Integrations |
| “What has been built or discussed in public?” | Related Practices & Discussions; Research sources |

## Research sources

- [Research sources (English)](research/sources.en.md)
- [研究资料（中文）](research/sources.md)
- [Source policy](docs/source-policy.en.md) · [Attribution](ATTRIBUTION.en.md)

The research chapter records official material, open-source projects, technical writing, and public social discussions. It distinguishes runnable implementations, public opinions, and leads that still need verification. Prices, model aliases, performance, and platform capabilities change; inspect the original source before adoption.

## Inclusion rules

- The source is public, citable, and explicitly uses Jev or System One typed decisions.
- The summary states the concrete scenario, judgment type, and implementation value.
- Pure opinion, unverifiable promotion, and projects that only resemble Jev stay out of practice entries; they may appear in discussions with evidence strength labeled.
- Inclusion is not an endorsement of code quality, security, stability, performance, or license suitability.

Found an outdated, duplicate, or weakly supported entry? Open an issue or pull request with the original link and verification evidence. See [Contributing](CONTRIBUTING.en.md).

## Verification

```bash
python3 -m py_compile skill/jev-practice-recommender/recommend.py
python3 skill/jev-practice-recommender/recommend.py \
  skill/jev-practice-recommender/examples/sample-agent.jsonl \
  --output /tmp/jev-recommendations.json
git diff --check
```

## License

New code and documentation are MIT licensed; see [LICENSE](LICENSE). Third-party projects, names, authors, links, and content in the catalog remain subject to their own licenses and rights.
