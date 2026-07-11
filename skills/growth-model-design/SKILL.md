---
name: growth-model-design
description: Use this skill when defining or revising a growth model, North Star Metric, input metrics, value moment, customer journey, or metric tree for a product, service, content business, marketplace, or multi-project portfolio.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Model Design

## Purpose

Build a measurable growth model that links customer value to business outcomes.

## Inputs

- Business model, offer, and target customer
- Customer journey or funnel
- Available acquisition, activation, retention, referral, and revenue data
- Current goals, constraints, and reporting cadence


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Clarify the unit of value delivered to the customer; do not start with vanity metrics.
2. Select one candidate North Star Metric and explain why it represents recurring customer value.
3. Build a metric tree with controllable input metrics and lagging business outcomes.
4. Map the value moment, frequency, breadth, and depth of usage or service delivery.
5. Define metric ownership, data source, calculation, reporting window, and known blind spots.
6. Stress-test the model against gaming, seasonality, channel bias, and revenue-only optimization.
7. Return a compact growth model, unresolved questions, and instrumentation gaps.


## Required output

Return a concise, decision-oriented response containing:

- Growth model summary
- North Star Metric definition
- Metric tree
- Stage definitions
- Instrumentation gaps
- Risks and anti-gaming checks


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Choosing traffic, impressions, or revenue as the North Star without showing customer value
- Using one universal funnel for unrelated business models
- Inventing data or benchmark targets

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
