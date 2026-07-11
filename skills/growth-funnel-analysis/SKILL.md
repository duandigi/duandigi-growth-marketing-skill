---
name: growth-funnel-analysis
description: Use this skill when mapping, diagnosing, or comparing a growth funnel across acquisition, activation, retention, referral, and revenue, including service-business lead funnels and product-led onboarding funnels.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Funnel Analysis

## Purpose

Find the highest-leverage bottleneck in a customer journey using evidence rather than channel assumptions.

## Inputs

- Stage definitions and event names
- Counts or conversion rates by stage
- Time window and segment definitions
- Known tracking gaps and business constraints


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Normalize the funnel so each stage has one clear entry condition and one clear success condition.
2. Check denominator consistency, duplicate users or leads, attribution windows, and missing events.
3. Calculate stage-to-stage and end-to-end conversion where data permits.
4. Segment by channel, landing page, device, geography, customer type, or cohort only when sample size is useful.
5. Identify the constraint with the largest combination of volume, value, and controllability.
6. Separate measurement failure from actual customer-behavior failure.
7. Return one primary bottleneck, secondary bottlenecks, and recommended next evidence.


## Required output

Return a concise, decision-oriented response containing:

- Funnel table
- Primary bottleneck
- Evidence and confidence
- Segment differences
- Tracking gaps
- Recommended next analyses


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Optimizing the stage with the lowest rate without considering volume or value
- Comparing incompatible time windows
- Treating correlation as causation

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
