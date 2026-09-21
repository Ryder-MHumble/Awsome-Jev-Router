# JEV / System One Research Sources

**Language:** English (current) · [中文原文](sources.md)

Updated: 2026-09-21 (Asia/Shanghai)

This file is the English companion to the Chinese research catalog. It keeps the same source set and separates official evidence, runnable implementations, open alternatives, and community leads. Star counts, commit dates, and repository contents change over time; snapshot numbers are not quality claims.

## Official and protocol sources

- [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) — TypeSafe describes Jev as a System One model for typed questions and typed decisions/probabilities, rather than long-form chat generation. **Strength: high.**
- [TypeSafe AI skills](https://github.com/typesafe-ai/skills) — official mountable skills for designing TypeSafe workflows and composing typed judgments. **High.**
- [TypeSafe JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) and [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) — official SDK quickstarts for state objects and `Choice`-style questions. **High.**
- [System One Adapter for Python](https://github.com/typesafe-ai/system-one-adapter-python) — a drop-in adapter with usage, latency, retry, and attempt history for comparing providers. **High.**

## Directly related open-source implementations

The following links preserve the complete implementation set from the Chinese catalog. They are discovery evidence; reported performance still needs independent reproduction.

- [Hermes Jev Skills](https://github.com/kerpopule/hermes-jev-skills) — cross-agent skills for routing, memory filtering, compaction, and triage, with shadow mode and fail-open guidance. **High.**
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) — Rust skill routing with `route`, `no_skill`, `review`, replay, feedback, and “why not” explanations. **High.**
- [Jev Agent Skill Router](https://github.com/GodsBoy/jev-agent-skill-router) — candidate batching and typed routing decisions, with an exploratory synthetic evaluation. **High.**
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — typed keep/truncate/drop decisions for tool records while retaining original user and assistant text. **High.**
- [Jev Logs](https://github.com/reachjalil/jevlogs) — OpenTelemetry preprocessing that annotates diagnostic value and priority while retaining records for analysis. **High.**
- [jevify](https://github.com/altryne/jevify) — a skill for deciding which problems are suitable for Jev before adding a Jev call. **Medium.**
- [Cheshi](https://github.com/CheshiAI/Cheshi) — macOS agent workspace with reviewable conversations and project-external indexes. **Medium.**
- [VexJoy Agent](https://github.com/notque/vexjoy-agent) — specialist routing with review, tests, delivery, and intent receipts. **High.**
- [Jev-powered conversation memory](https://github.com/CheshiAI/Cheshi) and [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) — examples of preserving source text while using Jev for selection. **Medium.**

## Open alternatives and protocol compatibility

- [OpenJev](https://github.com/razorback16/openjev) — an independent, open System One decision server claiming compatibility with TypeSafe-style endpoints. **Medium.**
- [Von](https://github.com/wfzyx/von) — an open, non-autoregressive System One-style model with local Python and TypeScript SDKs. **Medium.**
- [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) — useful for replaying attempts and comparing latency, cost, retries, and errors across providers. **High.**

Protocol compatibility is not model equivalence. Compare cloud Jev, open alternatives, and an LLM baseline on the same redacted replay set.

## Community and social leads

These pages are discovery leads rather than independently verified experiments. Dynamic X pages may require a logged-in browser, so the project does not turn a paraphrase into a measured result.

- [TypeSafe AI on X](https://x.com/TypeSafeAI) — official account and discovery entry point.
- [TypeSafe AI GitHub organization](https://github.com/TypeSafe-AI) — official repository index.
- [Diogo Almeida launch post](https://x.com/CompleteSkeptic/status/2099925682726002904) — founder framing of RLCD decision models and software value. **Low.**
- [Jev as an agent safety monitor](https://x.com/isNickMa/status/2100566407524344225) — reported pre-action checks for agent tool calls. **Low.**
- [Jev instant compaction](https://x.com/tamarajtran/status/2100694549362553153) — community proposal for typed context retention decisions. **Low.**
- [Arbitrary classification as a type-safe primitive](https://x.com/cocktailpeanut/status/2100277062309179521) — opinion on runtime-defined typed classification. **Low.**
- [Jev as an intelligent switch statement](https://x.com/NathanFlurry/status/2100036101809619314) — opinion that Jev complements rather than replaces GPT/Claude. **Low.**
- [Chinese Jev explainer](https://x.com/dotey/status/2100109937237987823) — Chinese-language System One overview. **Low.**
- [Jev is not an LLM](https://forkast.news/typesafe-ais-jev-is-not-an-llm-and-that-may-be-the-point/) — media commentary on non-generative decisions and inference cost. **Medium.**
- [Chinese deep dive on Jev boundaries](https://github.com/kuhung/understanding-jev) — community discussion of latency and engineering limits. **Medium.**

## Reusable conclusions for this project

1. Keep append-only raw events and send only minimized, redacted state to a typed decision provider.
2. Use a shared `route` / `no_skill` / `review` contract with candidate, confidence, provider, latency, and policy version.
3. Start in shadow mode. Timeouts, low confidence, sensitive input, or policy conflicts must fail open to the original agent flow.
4. Aggregate behavior locally over time windows. High frequency alone does not justify automation; also measure success, adoption, counterexamples, latency, cost, and privacy exposure.
5. Maintain a labeled replay set and evaluate recommendation, compaction, and behavior clustering separately.
6. Preserve source URL, author, retrieval date, license, evidence location, and strength for every practice.
