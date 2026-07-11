---
name: marketing-anomaly-detection
description: Use this skill when detecting, validating, classifying, and escalating unusual changes in marketing, analytics, advertising, social, CRM, revenue, connection, or tracking metrics.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Marketing Anomaly Detection

## Purpose

Generate useful alerts while reducing false alarms caused by seasonality, incomplete periods, expected data lag, small samples, and measurement changes.

## Inputs

- Time-series metrics with complete-period flags
- Historical baselines, seasonality, holidays, campaigns, and known changes
- Connection health, data quality, metric definitions, and expected lag
- Business thresholds, budgets, risk tolerances, and escalation owners

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Exclude incomplete, delayed, duplicated, or known-maintenance periods from the baseline.
2. Use robust statistical and business-rule checks appropriate to the metric volume and cadence.
3. Compare against recent, seasonal, and matched-weekday baselines where available.
4. Check related metrics to distinguish tracking failure, mix shift, demand change, delivery change, and business outcome change.
5. Classify severity by business impact, confidence, reversibility, and urgency.
6. Suppress duplicates and group related symptoms into one incident.
7. Return an alert with evidence, likely causes, checks, owner, and next action.

## Required output

Return a concise, decision-oriented result containing:

- Anomaly status and severity
- Observed change and baseline method
- Related metrics and competing explanations
- Confidence, data-quality caveat, and affected scope
- Immediate checks, escalation owner, and action threshold

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not alert on incomplete current-day data unless the metric is designed for intraday monitoring.
- Do not equate statistical unusualness with business harm.
- Do not trigger automated spend, publishing, deletion, or access changes from anomaly detection alone.
- Do not use a fixed percentage threshold for every metric and project.

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
