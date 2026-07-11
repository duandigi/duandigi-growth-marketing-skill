---
name: growth-metrics-diagnosis
description: Use this skill when investigating growth metric changes, anomalies, attribution conflicts, reporting discrepancies, or unclear performance across analytics, search, ads, CRM, product, or revenue systems.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Metrics Diagnosis

## Purpose

Diagnose what changed, why it may have changed, and what evidence is still missing.

## Inputs

- Metric definition and data source
- Comparison windows
- Segments and related metrics
- Tracking, release, campaign, and operational changes


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Restate the exact metric formula, entity, timezone, attribution model, and reporting window.
2. Validate data freshness, sampling, filters, consent changes, event definitions, and pipeline failures.
3. Decompose the metric into volume, rate, mix, and value components.
4. Compare leading, coincident, and lagging indicators.
5. Build competing explanations and list evidence for and against each one.
6. Separate confirmed causes, likely causes, and unknowns.
7. Recommend the minimum next checks that would materially reduce uncertainty.


## Required output

Return a concise, decision-oriented response containing:

- Metric definition
- Observed change
- Data-quality checks
- Driver decomposition
- Hypotheses
- Confidence
- Next checks


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Attributing every change to marketing
- Comparing partial current periods with complete prior periods
- Confusing platform-reported conversions with incremental impact

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
