#!/usr/bin/env python3
"""Validate Agent Skills frontmatter, required sections, and eval files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_HEADINGS = ["## Purpose", "## Inputs", "## Workflow", "## Required output", "## Guardrails"]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        block = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    fields: dict[str, str] = {}
    in_metadata = False
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("metadata:"):
            in_metadata = True
            continue
        if line.startswith(" ") and in_metadata:
            continue
        in_metadata = False
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_file = path / "SKILL.md"
    if not skill_file.exists():
        return [f"{path.name}: missing SKILL.md"]
    text = skill_file.read_text(encoding="utf-8")
    try:
        meta = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{path.name}: {exc}"]

    name = meta.get("name", "")
    description = meta.get("description", "")
    if name != path.name:
        errors.append(f"{path.name}: frontmatter name must match directory")
    if not NAME_RE.fullmatch(name):
        errors.append(f"{path.name}: invalid name")
    if not 1 <= len(description) <= 1024:
        errors.append(f"{path.name}: description must be 1-1024 characters")
    if "use this skill when" not in description.lower():
        errors.append(f"{path.name}: description should say when to use the skill")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{path.name}: missing heading {heading}")

    eval_file = path / "evals" / "evals.json"
    if not eval_file.exists():
        errors.append(f"{path.name}: missing evals/evals.json")
    else:
        try:
            data = json.loads(eval_file.read_text(encoding="utf-8"))
            if data.get("skill_name") != path.name:
                errors.append(f"{path.name}: eval skill_name mismatch")
            evals = data.get("evals")
            if not isinstance(evals, list) or len(evals) < 3:
                errors.append(f"{path.name}: include at least three eval cases")
            elif not any(e.get("edge_case") for e in evals if isinstance(e, dict)):
                errors.append(f"{path.name}: include at least one edge_case eval")
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: invalid eval JSON: {exc}")
    return errors


def main() -> int:
    errors: list[str] = []
    paths = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not paths:
        errors.append("no skills found")
    for path in paths:
        errors.extend(validate_skill(path))
    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(paths)} skills successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
