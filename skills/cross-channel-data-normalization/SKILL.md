---
name: cross-channel-data-normalization
description: Use this skill when converting data from analytics, search, advertising, social, local, CRM, commerce, or website systems into a shared project, channel, asset, metric, date, currency, and attribution contract.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Cross Channel Data Normalization

## Purpose

Create a canonical data layer that supports safe cross-channel comparison without erasing provider-specific meaning.

## Inputs

- Provider fields, dimensions, metrics, and source metadata
- Project and asset mappings
- Canonical channel taxonomy and metric dictionary
- Time-zone, currency, attribution, identity, and deduplication rules

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Preserve the raw provider record and immutable source identifiers.
2. Map provider fields to canonical metric names, units, grain, and object types.
3. Normalize project, channel, campaign, content, landing-page, location, and lead identifiers.
4. Convert currency and time boundaries only with documented rates and time zones.
5. Keep provider-reported, analytics-observed, CRM-qualified, and revenue-confirmed conversions separate.
6. Record lineage, transformation version, freshness, and quality flags for every normalized record.
7. Validate that aggregation does not double count shared campaigns, cross-domain sessions, or assisted conversions.

## Required output

Return a concise, decision-oriented result containing:

- Canonical field mapping and transformation rules
- Normalized data contract and channel taxonomy
- Metric-definition registry with units and grains
- Lineage, quality flags, and unresolved mappings
- Aggregation and deduplication tests

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not rename different concepts into one metric merely because labels are similar.
- Do not sum users, reach, impressions, attributed conversions, or assisted conversions across platforms as unique people or outcomes.
- Do not discard provider-specific fields needed for later audit.
- Do not convert currencies or time zones without recording the method.

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
