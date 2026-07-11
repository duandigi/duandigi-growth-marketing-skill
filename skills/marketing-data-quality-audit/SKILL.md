---
name: marketing-data-quality-audit
description: Use this skill when auditing whether marketing, analytics, CRM, revenue, conversion, or experiment data is complete, consistent, timely, deduplicated, comparable, and fit for a specific decision.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Marketing Data Quality Audit

## Purpose

Establish whether available data can support descriptive reporting, diagnosis, attribution, forecasting, or causal claims before AI evaluation begins.

## Inputs

- Raw or normalized records and source metadata
- Metric definitions, event taxonomy, attribution windows, and conversion rules
- Expected data ranges, grain, time zone, and currency
- Known tracking changes, migrations, outages, and consent effects

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. State the decision the data is expected to support.
2. Check schema validity, required fields, types, duplicate keys, null rates, and impossible values.
3. Check completeness by provider, project, channel, asset, date, device, and conversion stage.
4. Reconcile totals across source systems without assuming they should match exactly.
5. Identify definition, attribution, time-zone, currency, and identity-resolution conflicts.
6. Score fitness for reporting, diagnosis, attribution, experiment analysis, and automated action separately.
7. Create instrumentation or repair tasks for critical gaps.

## Required output

Return a concise, decision-oriented result containing:

- Data-quality score with confidence and decision fitness
- Critical, major, and minor issues
- Reconciliation table and expected discrepancies
- Affected reports, scores, and automated actions
- Repair, validation, and monitoring plan

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not silently fill missing observations with zero.
- Do not compare metrics with different definitions, windows, currencies, or grains without normalization.
- Do not infer revenue quality from platform conversion counts alone.
- Do not approve automated optimization when critical conversion or spend data is unreliable.

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
