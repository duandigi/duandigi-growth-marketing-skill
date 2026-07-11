---
name: ai-marketing-evaluator
description: Use this skill when producing an evidence-backed AI evaluation of a project, portfolio, channel, campaign, landing page, content group, funnel, lead source, or revenue outcome from normalized multi-source data.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents, JSON contracts, mock connectors, and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: marketing-intelligence
---

# Ai Marketing Evaluator

## Purpose

Explain what changed, why it may have changed, what the business impact is, what remains unknown, and which action or experiment should happen next.

## Inputs

- Project goals, growth model, and decision context
- Connection health and data-quality assessment
- Normalized channel, conversion, lead, and revenue data
- Historical baseline, seasonality, changes, experiments, and constraints

If a required input is unavailable, label it **unknown**, state how it limits the decision, and create a collection, mapping, validation, or instrumentation task. Never invent credentials, assets, metrics, permissions, or business outcomes.

## Workflow

1. Confirm the evaluation period, comparison period, data completeness, and decision owner.
2. Describe material changes from portfolio to project, channel, object, funnel stage, and business outcome.
3. Separate observed facts, calculated facts, plausible explanations, and unknowns.
4. Test measurement, mix, seasonality, campaign, landing-page, operational, and market explanations before selecting a likely cause.
5. Assess impact on customer value, qualified outcomes, revenue, efficiency, and risk rather than vanity metrics alone.
6. Create no more than five prioritized findings, each with evidence, confidence, missing data, and next action.
7. Convert eligible findings into alerts, research tasks, experiments, or approval requests.

## Required output

Return a concise, decision-oriented result containing:

- Executive evaluation and scope
- Prioritized evaluation cards
- Evidence, confidence, competing explanations, and missing data
- Business impact and affected funnel stage
- Recommended task, experiment, or decision with approval level

Label material statements as **confirmed**, **calculated**, **inferred**, **assumed**, or **unknown**. Include the data period, last complete period, source lineage, and confidence whenever they can change the decision.

## Guardrails

- Do not produce an AI score or causal explanation when connection health or data quality is insufficient.
- Do not state that correlation, attribution, or before-after change proves causality.
- Do not recommend optimization toward unqualified leads, platform conversions, or engagement if business outcomes worsen.
- Do not hide uncertainty behind polished narrative.

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
