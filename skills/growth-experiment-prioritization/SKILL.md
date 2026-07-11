---
name: growth-experiment-prioritization
description: Use this skill when scoring, ranking, sequencing, or selecting growth experiments and research tasks across one or many projects using impact, confidence, strategic fit, reusability, revenue relevance, effort, risk, and dependencies.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Experiment Prioritization

## Purpose

Create a transparent, comparable experiment queue without hiding judgment behind a score.

## Inputs

- Candidate experiments
- Required score dimensions from 1 to 10
- Dependencies and deadlines
- Available capacity and strategic priorities


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Reject experiments that lack a measurable outcome, owner, or minimum evidence.
2. Score each dimension using the rubric in references/scoring-rubric.md.
3. Run scripts/score_experiments.py for consistent calculation when structured data is available.
4. Apply dependency, capacity, legal, brand, and instrumentation gates after scoring.
5. Balance quick learning, near-term value, and strategic capability building.
6. Publish both the numeric ranking and the rationale; allow an explicit strategic override with a reason.
7. Limit active work to the team's realistic work-in-progress capacity.


## Required output

Return a concise, decision-oriented response containing:

- Ranked backlog
- Dimension scores
- Score explanation
- Dependencies
- Selected now/next/later
- Override reasons


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Treating the score as objective truth
- Using made-up precision
- Ranking unsafe or unmeasurable experiments

- Claim guaranteed growth or present an estimate as observed fact.
- Recommend spam, fake reviews, impersonation, deceptive urgency, dark patterns, policy evasion, or unauthorized production changes.
- Hide material uncertainty, tracking limitations, or possible harm.

When an action can spend money, publish content, contact people, change production systems, delete data, or alter access, produce a plan and request explicit authorization rather than executing automatically.

## Available script

- `scripts/score_experiments.py` — deterministic scoring utility bundled with this skill. It accepts JSON or CSV and returns structured JSON.

## Completion check

Before finishing, verify that the output:

- answers a specific growth decision;
- uses the supplied business context;
- separates evidence from assumptions;
- defines a measurable next step;
- includes risks, constraints, and missing data;
- is no longer than necessary for the decision.
