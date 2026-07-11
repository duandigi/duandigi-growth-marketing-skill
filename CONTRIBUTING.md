# Contributing

Thank you for helping improve Duan Growth Skills.

## What makes a useful contribution

- A realistic eval prompt and a clear success definition
- A failure case showing where a skill overreaches or misses context
- A correction that improves evidence quality or measurability
- A workflow adapted to a business model not yet represented
- A safer or less manipulative alternative to a growth tactic
- A script improvement with tests and structured output

## Skill requirements

Every skill must:

1. Follow the Agent Skills naming and frontmatter rules.
2. Explain both what it does and when to use it.
3. Produce a decision-oriented output, not a generic tactic list.
4. Distinguish facts, inferences, assumptions, and unknowns.
5. Include at least three eval cases, including one edge case.
6. Avoid claims of guaranteed growth.
7. Reject spam, fake proof, deception, dark patterns, policy evasion, and unsafe automation.

## Pull request process

1. Open an issue describing the problem or evidence.
2. Keep each pull request focused.
3. Run `make validate`.
4. Explain expected behavior changes and possible regressions.
5. Add or update evals and tests.
6. Do not include credentials, personal data, client-confidential data, or copied proprietary material.

## Evidence standard

When changing a workflow, provide at least one of:

- Real, anonymized failure or success case
- Reproducible benchmark comparison
- Primary documentation supporting a technical constraint
- A clear reasoning argument with a testable eval

Popularity, intuition, and tool output alone are not proof.
