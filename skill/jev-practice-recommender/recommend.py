#!/usr/bin/env python3
"""Offline Jev practice recommender for agent session logs.

The script intentionally uses only the Python standard library. It reads JSONL,
JSON message arrays, or plain text logs and emits a small, auditable JSON report.
No log contents leave the local machine.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


SCENARIOS: dict[str, tuple[str, tuple[str, ...]]] = {
    "classification-routing": ("分类与路由", ("route", "routing", "classif", "intent", "分类", "路由", "分流")),
    "verification-guardrails": ("验证与护栏", ("guard", "verify", "permission", "safety", "security", "审核", "校验", "权限", "安全")),
    "scoring-ranking": ("评分与排序", ("score", "rank", "ranking", "grade", "评分", "排序", "评级")),
    "agent-decisions": ("Agent 决策", ("agent", "tool call", "tool_call", "decision", "工具调用", "决策")),
    "data-labeling-curation": ("数据标注与整理", ("label", "curat", "tag", "标注", "整理", "标签")),
    "evaluation-benchmarking": ("评测与基准", ("eval", "benchmark", "test case", "评测", "基准", "测试")),
    "calibration-research": ("校准与研究", ("calibrat", "confidence", "research", "校准", "置信度", "研究")),
    "infra-sdks-integrations": ("基础设施与集成", ("sdk", "api", "gateway", "plugin", "integration", "接口", "插件", "集成")),
    "game-simulation": ("游戏与仿真", ("game", "simulation", "游戏", "仿真")),
    "finance-trading": ("金融与交易", ("finance", "trading", "trade", "金融", "交易")),
    "compliance-legal": ("合规与法律", ("compliance", "legal", "policy", "合规", "法律", "政策")),
    "content-moderation": ("内容审核", ("moderation", "spam", "toxicity", "内容审核", "垃圾", "违规")),
    "scientific-pipelines": ("科研流水线", ("science", "scientific", "pipeline", "科研", "流水线")),
}

SENSITIVE_PATTERNS = (
    (re.compile(r"(?i)\b(?:sk|pk|rk)-[A-Za-z0-9_\-]{12,}\b"), "[REDACTED_KEY]"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"), "[REDACTED_TOKEN]"),
    (re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._~+/=-]{12,}"), "Bearer [REDACTED_TOKEN]"),
    (re.compile(r"(?i)\b(api[_-]?key|token|secret|password|passwd)\s*[:=]\s*[^\s,;]+"), r"\1=[REDACTED]"),
    (re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b"), "[REDACTED_EMAIL]"),
    (re.compile(r"(?<!\d)(?:\+?86[- ]?)?1[3-9]\d{9}(?!\d)"), "[REDACTED_PHONE]"),
    (re.compile(r"(?<!\w)/(?:Users|home|private|var|tmp)/[^\s\"']+"), "[REDACTED_PATH]"),
    (re.compile(r"(?i)(?:https?://)(?:[^\s/@]+:[^\s/@]+)@"), "https://[REDACTED_CREDENTIALS]@"),
)


def redact(text: str) -> str:
    for pattern, replacement in SENSITIVE_PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def _text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (int, float, bool)):
        return str(value)
    if isinstance(value, list):
        return " ".join(_text(item) for item in value)
    if isinstance(value, dict):
        preferred = [value.get(k) for k in ("content", "text", "message", "prompt", "input", "output")]
        chosen = [item for item in preferred if item is not None]
        return _text(chosen[0]) if chosen else " ".join(_text(item) for item in value.values())
    return ""


def _records(value: Any, line_hint: int = 1) -> Iterable[tuple[int, str]]:
    if isinstance(value, list):
        for index, item in enumerate(value, line_hint):
            yield from _records(item, index)
    elif isinstance(value, dict):
        # Common agent exports: {messages: [...]}, {events: [...]}, or one event per object.
        for key in ("messages", "events", "conversation", "transcript", "records"):
            if key in value and isinstance(value[key], (list, dict)):
                yield from _records(value[key], line_hint)
                return
        text = _text(value)
        if text.strip():
            yield line_hint, text
    elif _text(value).strip():
        yield line_hint, _text(value)


def read_log(path: Path) -> list[dict[str, Any]]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    records: list[tuple[int, str]] = []
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        parsed = None
    if parsed is not None:
        records.extend(_records(parsed))
    else:
        for number, line in enumerate(raw.splitlines(), 1):
            if line.strip():
                try:
                    records.extend(_records(json.loads(line), number))
                except json.JSONDecodeError:
                    records.append((number, line))
    return [{"line": line, "text": redact(text).strip()} for line, text in records if text.strip()]


def load_practices(root: Path) -> list[dict[str, str]]:
    practices: list[dict[str, str]] = []
    for source in sorted((root / "categories").glob("*.md")):
        category = source.stem
        for line in source.read_text(encoding="utf-8", errors="replace").splitlines():
            match = re.match(r"^- \[([^\]]+)\]\(([^)]+)\) - (.+)$", line)
            if match:
                practices.append({"name": match.group(1), "url": match.group(2), "description": match.group(3), "source": str(source.relative_to(root))})
    return practices


def terms(text: str) -> set[str]:
    return {token for token in re.findall(r"[a-z][a-z0-9_-]{2,}|[\u4e00-\u9fff]{2,}", text.lower())}


def classify(records: list[dict[str, Any]]) -> tuple[Counter[str], list[dict[str, Any]]]:
    counts: Counter[str] = Counter()
    evidence: list[dict[str, Any]] = []
    for record in records:
        lowered = record["text"].lower()
        matched: list[dict[str, Any]] = []
        for key, (label, signals) in SCENARIOS.items():
            hits = [signal for signal in signals if signal.lower() in lowered]
            if hits:
                counts[key] += len(hits)
                matched.append({"scenario": key, "label": label, "signals": hits})
        if matched:
            evidence.append({"line": record["line"], "excerpt": record["text"][:360], "matches": matched})
    return counts, evidence


def recommend(counts: Counter[str], evidence: list[dict[str, Any]], practices: list[dict[str, str]], top: int) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for scenario, count in counts.most_common():
        label, signals = SCENARIOS[scenario]
        scenario_terms = set(signals) | terms(label)
        candidates = []
        for practice in practices:
            haystack = f"{practice['name']} {practice['description']}".lower()
            overlap = sorted(term for term in scenario_terms if term.lower() in haystack)
            category_bonus = 2 if scenario in practice["source"] else 0
            score = count + category_bonus + len(overlap)
            candidates.append((score, practice, overlap))
        candidates.sort(key=lambda item: (-item[0], item[1]["name"].lower()))
        recs = []
        for score, practice, overlap in candidates[:top]:
            recs.append({"name": practice["name"], "url": practice["url"], "source": practice["source"], "why": f"场景信号 {', '.join(overlap) if overlap else '分类匹配'}；请打开来源复核。", "score": score})
        result.append({"scenario": scenario, "label": label, "frequency": count, "recommendations": recs, "evidence": [item for item in evidence if any(match["scenario"] == scenario for match in item["matches"])][:8]})
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Offline, privacy-aware Jev practice recommender")
    parser.add_argument("log", type=Path, help="JSONL, JSON export, or plain text agent log")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2], help="Jev Practice Radar repository root")
    parser.add_argument("--top", type=int, default=3, help="recommendations per scenario")
    parser.add_argument("--output", type=Path, help="write JSON report to this path")
    args = parser.parse_args()
    records = read_log(args.log)
    counts, evidence = classify(records)
    report = {"schema": "jev-practice-recommender/v1", "privacy": {"network": False, "redacted": True, "records": len(records)}, "scenarios": recommend(counts, evidence, load_practices(args.root), max(1, args.top))}
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
