---
name: growth-experiment-analysis
description: Use this skill when evaluating a completed or in-progress growth experiment, A/B test, before-after test, cohort comparison, or rollout to decide whether to scale, iterate, stop, or gather more data.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Experiment Analysis

## Purpose

Turn experiment data into a calibrated decision with explicit uncertainty.

## Inputs

- Pre-registered hypothesis and decision rule
- Variant or period results
- Sample sizes and measurement window
- Guardrail metrics, incidents, and implementation notes


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Verify that the experiment ran as designed and that tracking was stable.
2. Check sample ratio, exposure, contamination, seasonality, concurrent changes, and missing data.
3. Compare the primary metric and guardrails using absolute and relative changes.
4. Distinguish directional evidence, practical significance, and statistical confidence.
5. Check important segments only if they were pre-specified or label them exploratory.
6. Make one decision: scale, iterate, stop, or inconclusive; explain what would change the decision.
7. Record the result in a reusable learning statement rather than declaring universal truth.


## Required output

Return a concise, decision-oriented response containing:

- Integrity checks
- Primary result
- Guardrail result
- Confidence and limitations
- Decision
- Learning
- Follow-up action


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- P-hacking or selective segments
- Calling an underpowered result a win
- Ignoring negative guardrails

- Claim guaranteed growth or present an estimate as observed fact.
- Recommend spam, fake reviews, impersonation, deceptive urgency, dark patterns, policy evasion, or unauthorized production changes.
- Hide material uncertainty, tracking limitations, or possible harm.

When an action can spend money, publish content, contact people, change production systems, delete data, or alter access, produce a plan and request explicit authorization rather than executing automatically.

## Completion check

Before finishing, verify that the output:

- answers a specific growth decision;
- uses the supplied business context;
- separates evidence from assumptions;
- defines a measurable next step;
- includes risks, constraints, and missing data;
- is no longer than necessary for the decision.
