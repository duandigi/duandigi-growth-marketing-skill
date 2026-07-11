---
name: growth-experiment-design
description: Use this skill when turning a growth opportunity into a testable experiment with a falsifiable hypothesis, intervention, audience, primary metric, guardrail metrics, tracking plan, decision rule, and rollback plan.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Experiment Design

## Purpose

Design experiments that can produce a trustworthy decision, not merely activity.

## Inputs

- Opportunity and supporting evidence
- Baseline metric and target audience
- Implementation constraints
- Available tracking and expected traffic or sample


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Write a falsifiable hypothesis in the form: because evidence suggests X, changing Y for audience Z should move metric M through mechanism K.
2. Choose the smallest intervention that can test the mechanism.
3. Define eligibility, exposure, variants, exclusions, and contamination risks.
4. Choose one primary metric and a small set of guardrail metrics.
5. Define the measurement window, minimum data requirement, and decision rule before launch.
6. Specify instrumentation, QA, owner, launch checklist, rollback trigger, and stopping conditions.
7. If a controlled test is impossible, design a time-boxed observational test and label its weaker causal confidence.


## Required output

Return a concise, decision-oriented response containing:

- Hypothesis
- Experiment design
- Audience and variants
- Metrics
- Tracking plan
- Decision rule
- Risks and rollback


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Changing multiple unrelated mechanisms in one test
- Selecting several primary metrics
- Promising statistical significance without adequate data

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
