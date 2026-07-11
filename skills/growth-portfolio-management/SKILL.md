---
name: growth-portfolio-management
description: Use this skill when comparing, prioritizing, or allocating people, budget, experiments, and attention across multiple products, clients, websites, or growth projects while preserving project-specific goals and constraints.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Portfolio Management

## Purpose

Manage growth as a portfolio instead of optimizing every project independently.

## Inputs

- Project goals and business value
- Current growth stage and constraints
- Performance, confidence, and opportunity backlog
- Shared capacity, budget, and strategic commitments


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Normalize projects by decision-relevant measures, not raw traffic or revenue alone.
2. Classify each project by stage: validate, build foundation, accelerate, defend, harvest, or pause.
3. Estimate marginal return and learning value of the next unit of effort.
4. Identify shared capabilities, reusable assets, cross-project experiments, and conflicts.
5. Allocate capacity across core, growth, and exploratory work with explicit rationale.
6. Set stop-loss, review dates, and reallocation triggers.
7. Return a portfolio view while preserving project-level North Stars and guardrails.


## Required output

Return a concise, decision-oriented response containing:

- Portfolio classification
- Resource allocation
- Top project opportunities
- Shared plays
- Risks
- Review triggers


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Ranking projects only by current size
- Applying identical KPIs to unlike businesses
- Spreading resources so thin that no experiment reaches a decision

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
