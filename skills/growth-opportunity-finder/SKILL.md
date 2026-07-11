---
name: growth-opportunity-finder
description: Use this skill when identifying evidence-backed growth opportunities, quick wins, constraints, or next actions across acquisition, activation, retention, referral, revenue, content, SEO, paid media, CRM, or product experience.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Opportunity Finder

## Purpose

Convert business context and performance evidence into a ranked opportunity backlog.

## Inputs

- Project context and strategic goals
- Funnel, channel, customer, or revenue evidence
- Resource, budget, policy, and technical constraints
- Previous experiments and decisions


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. State the business objective and the metric that represents success.
2. Inventory observed signals, anomalies, customer friction, and underused assets.
3. Distinguish opportunities from unverified ideas; every opportunity needs evidence or an explicit research task.
4. Map each opportunity to a funnel stage, mechanism, target segment, and expected behavior change.
5. Estimate impact, confidence, effort, risk, strategic fit, revenue relevance, and reusability.
6. Remove duplicates and dependencies; identify what must happen first.
7. Return a ranked backlog with no more than five top recommendations unless the user asks for more.


## Required output

Return a concise, decision-oriented response containing:

- Opportunity statement
- Evidence
- Growth mechanism
- Target metric
- Confidence
- Dependencies
- Recommended experiment or research task


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Generic tactic lists
- Calling an idea a quick win without estimating effort
- Suggesting spam, fake reviews, dark patterns, policy evasion, or doorway pages

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
