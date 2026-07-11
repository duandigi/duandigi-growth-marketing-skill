#!/usr/bin/env python3
"""Score growth experiments from JSON or CSV with a transparent 0-100 model."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

BENEFIT_WEIGHTS = {
    "impact": 0.30,
    "confidence": 0.20,
    "strategic_fit": 0.20,
    "reusability": 0.10,
    "revenue_relevance": 0.20,
}
COST_WEIGHTS = {"effort": 0.65, "risk": 0.35}
REQUIRED = tuple(BENEFIT_WEIGHTS) + tuple(COST_WEIGHTS)


def _number(value: Any, field: str) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric, got {value!r}") from exc
    if not 1 <= number <= 10:
        raise ValueError(f"{field} must be between 1 and 10, got {number}")
    return number


def score_experiment(item: dict[str, Any]) -> dict[str, Any]:
    values = {field: _number(item.get(field), field) for field in REQUIRED}
    benefit = sum(values[key] * weight for key, weight in BENEFIT_WEIGHTS.items()) / 10
    cost = sum(values[key] * weight for key, weight in COST_WEIGHTS.items())
    cost_factor = 1 - 0.45 * ((cost - 1) / 9)
    score = round(max(0, min(100, 100 * benefit * cost_factor)), 1)

    if score >= 75:
        priority = "high"
    elif score >= 55:
        priority = "medium"
    else:
        priority = "low"

    result = dict(item)
    result.update(
        {
            "priority_score": score,
            "priority_band": priority,
            "score_components": {
                "benefit_index": round(benefit * 100, 1),
                "cost_index": round(cost * 10, 1),
                "cost_factor": round(cost_factor, 3),
            },
            "score_warning": (
                "Apply dependency, capacity, safety, instrumentation, and strategic gates "
                "after numeric scoring."
            ),
        }
    )
    return result


def load_items(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8-sig") as handle:
            return list(csv.DictReader(handle))
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "experiments" in data:
        data = data["experiments"]
    if not isinstance(data, list) or not all(isinstance(x, dict) for x in data):
        raise ValueError("Input JSON must be a list of experiments or an object with experiments[]")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON or CSV input")
    parser.add_argument("--output", type=Path, help="Write JSON output to this path")
    args = parser.parse_args()

    try:
        scored = [score_experiment(item) for item in load_items(args.input)]
        scored.sort(key=lambda x: x["priority_score"], reverse=True)
        payload = json.dumps({"experiments": scored}, ensure_ascii=False, indent=2)
        if args.output:
            args.output.write_text(payload + "\n", encoding="utf-8")
        else:
            print(payload)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
