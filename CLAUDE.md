# Claude instructions for this repository

This is a public Agent Skills repository. Treat skills, schemas, examples, scripts, connectors, and tests as reusable interfaces.

## Required behavior

- Never create or request real credentials.
- Keep provider authorization outside skills and examples.
- Default all provider capabilities to observe mode.
- Preserve organization, project, provider, asset, date, time zone, currency, attribution, and source lineage.
- Separate provider-reported, analytics-observed, CRM-qualified, business-confirmed, and experiment evidence.
- Gate AI evaluation on connection and data quality.
- Convert high-impact recommendations into approval cards; do not execute them.
- Add at least three evals, including one edge case, for every skill.
- Run `make validate` after changes.

## Repository design

Portable skills live in `skills/`. Claude Code subagents live in `agents/`. Provider registry and mock connector metadata live in `connectors/`. Production connectors and secret stores are out of scope for this public repository unless they can be shipped without credential risk and with provider-compliant tests.
