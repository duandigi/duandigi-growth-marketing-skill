---
name: growth-retrospective
description: Use this skill when converting completed growth work, campaigns, launches, experiments, or failures into reusable lessons, decision records, playbooks, and changes to future operating rules.
license: MIT
compatibility: Portable Agent Skill. Optional Claude Code agents and Python 3.10+ utilities are included at repository level.
metadata:
  author: duandigi
  version: "0.2.0"
  category: growth
---

# Growth Retrospective

## Purpose

Create organizational learning so the team does not repeat avoidable mistakes or lose successful patterns.

## Inputs

- Original goal and hypothesis
- What was shipped and when
- Results and guardrails
- Implementation notes, surprises, and stakeholder feedback


If critical input is unavailable, label it **unknown** and create a research or instrumentation task. Do not invent values.

## Workflow

1. Compare the original plan with what actually happened.
2. Separate outcome quality from decision quality and execution quality.
3. Identify which assumptions were confirmed, weakened, disproved, or left unresolved.
4. Capture context boundaries so a learning is not overgeneralized.
5. Decide what to standardize, change, automate, monitor, or stop.
6. Create a concise learning card and link it to relevant projects, metrics, and future experiments.
7. Update the backlog, playbook, and instrumentation requirements.


## Required output

Return a concise, decision-oriented response containing:

- Outcome summary
- Decision and execution review
- Validated and invalidated assumptions
- Reusable learning
- Playbook change
- Follow-up


Label important statements as **confirmed**, **inferred**, **assumed**, or **unknown** when the distinction affects the decision.

## Guardrails

Do not:

- Blame-focused retrospectives
- Celebrating activity instead of outcomes
- Recording lessons without changing future behavior

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
