---
name: crm-funnel-analysis
description: Use this skill when analyzing lead capture, qualification, response time, pipeline stages, sales outcomes, retention, reactivation, source quality, revenue, and CRM data integrity.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Crm Funnel Analysis

## Purpose

Connect marketing activity to qualified leads, customers, revenue, retention, and operational follow-up rather than stopping at form or platform conversions.

## Inputs

- Lead, contact, account, deal, stage, owner, activity, outcome, and revenue records
- Source, campaign, landing-page, content, and tracking identifiers
- Qualification criteria, SLA, sales process, loss reasons, and retention definitions
- Consent, privacy, deduplication, and identity-resolution rules

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Validate stage definitions, mandatory fields, deduplication, source capture, timestamps, and outcome completeness.
2. Map the funnel from contact through qualification, consultation, proposal, win, repeat, and referral as applicable.
3. Analyze conversion, velocity, response time, aging, owner performance, loss reasons, source quality, revenue, and retention.
4. Identify lead leakage, stale records, missing follow-up, stage inflation, source loss, and channel-quality differences.
5. Compare cohorts by source, landing page, campaign, service, segment, location, and time.
6. Separate marketing quality, sales execution, capacity, pricing, and product or service fit explanations.
7. Recommend instrumentation, routing, nurturing, follow-up, offer, qualification, or acquisition changes.

## Required output

Return a concise, decision-oriented result containing:

- CRM data-quality and funnel summary
- Stage conversion, velocity, leakage, and source-quality findings
- Revenue, retention, and loss-reason analysis
- Operational and attribution limitations
- Prioritized CRM, sales, and marketing actions

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not expose personally identifiable lead data in analysis outputs.
- Do not contact leads or change stages automatically without authorization and consent rules.
- Do not judge a marketing channel solely by raw lead count.
- Do not interpret missing loss reasons as customer objections.

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
