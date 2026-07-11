---
name: marketing-health-scoring
description: Use this skill when calculating an explainable marketing or growth health score for a project, channel, or portfolio using data health, acquisition, activation, conversion, retention, revenue, experiment velocity, and risk.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Marketing Health Scoring

## Purpose

Provide a comparable directional summary without hiding missing data, project-specific objectives, or critical failures behind one number.

## Inputs

- Project growth model and dimension weights
- Dimension scores, confidence, evidence, and data-quality status
- Critical connection, tracking, compliance, or business-risk flags
- Historical score and change explanations

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Define the score’s decision purpose and project-specific dimension weights.
2. Calculate each dimension only from documented metrics and evidence.
3. Attach confidence and data-quality status to every dimension.
4. Apply caps or unavailable status when critical data, connection, tracking, or safety conditions fail.
5. Calculate a weighted score and band while preserving dimension-level detail.
6. Explain every material score change and distinguish performance from measurement changes.
7. Recommend the few actions most likely to improve business health, not merely the score.

## Required output

Return a concise, decision-oriented result containing:

- Overall score, band, confidence, and comparability scope
- Dimension scores, weights, evidence, and data-quality status
- Score caps, critical flags, and unavailable dimensions
- Change drivers and historical comparison
- Priority actions and anti-gaming checks

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not compare projects with different score definitions as if scores were directly equivalent.
- Do not assign high confidence when revenue, retention, or qualified outcomes are unavailable.
- Do not let strong traffic hide broken tracking, safety, or business-outcome failures.
- Do not optimize work merely to increase the score.

- Do not claim guaranteed growth or present an estimate as observed fact.
- Do not reveal secrets, personal data, private provider payloads, or cross-project information.
- When an action can spend money, publish, contact people, alter access, modify production, or delete data, prepare an approval request instead of executing automatically.

## Completion check

Before finishing, verify that the output:

- answers a specific business or implementation decision;
- uses the correct organization, project, asset, date range, time zone, and currency;
- separates performance problems from data, connection, and attribution problems;
- includes evidence, uncertainty, affected scope, and a measurable next step;
- respects least privilege, approval, audit, and rollback requirements;
- is no longer than necessary for the decision.
