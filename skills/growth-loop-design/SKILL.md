---
name: growth-loop-design
description: Use this skill when designing, auditing, or improving a compounding growth loop such as referral, review, content, SEO, product, community, partnership, user-generated content, or tool-led growth.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Loop Design

## Purpose

Design a repeatable loop where outputs create new inputs and value increases with each cycle.

## Inputs

- Customer value moment
- Existing user or customer behaviors
- Shareable assets, incentives, or distribution surfaces
- Loop friction, time delay, and quality constraints


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Define the loop's entrant, trigger, action, value exchange, output, and reinvestment path.
2. Explain why a participant would complete each step without coercion.
3. Identify the loop coefficient, cycle time, quality filter, saturation point, and failure modes.
4. Separate a true loop from a one-way funnel or recurring campaign.
5. Design instrumentation for each step and one leading indicator of loop health.
6. Start with a manual or narrow prototype before automating.
7. Include abuse, privacy, brand, and platform-policy controls.


## Required output

Return a concise, decision-oriented response containing:

- Loop diagram in text
- Participant value exchange
- Loop equation or health metrics
- Friction map
- Prototype
- Risks and controls


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Calling a channel a loop without reinvestment
- Incentives that encourage low-quality or fraudulent behavior
- Assuming virality

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
