# Security Policy

## Supported versions

Only the latest tagged release receives security fixes during the 0.x phase.

## Reporting a vulnerability

Do not open a public issue for vulnerabilities involving command execution, secret exposure, unsafe file access, prompt injection, data leakage, cross-project access, token handling, OAuth redirect validation, webhook signature validation, or approval bypass. Contact the maintainer privately through the email listed on the maintainer's GitHub profile.

Include the affected file or skill, reproduction steps, impact, and suggested mitigation if known. Never include real credentials or personal customer data.

## Credential rules

- No access token, refresh token, client secret, password, Application Password, cookie, private key, or provider session belongs in this repository.
- Use encrypted secret references in production; examples contain non-working placeholders only.
- Redact authorization headers and provider payloads from logs and prompts.
- Handle expiry, revocation, rotation, offboarding, and compromised connections.
- OAuth state, redirect URI, PKCE where applicable, webhook signature, replay protection, and idempotency must be implemented by the deployed application.

## Data isolation

- Every record and asset is scoped to an organization and project.
- Mapping changes require review and an audit diff.
- Agents must not access or summarize another organization’s data.
- Prefer aggregated, redacted, or pseudonymous CRM data for AI analysis.

## Execution safety

- Read-only access is the default.
- Preparation and execution are separate capabilities.
- No AI agent may approve its own high-impact action.
- Production changes require explicit scope, named approval, expiry, preview, logs, verification, and rollback where possible.
- Anomaly detection alone cannot trigger spend, publishing, contact, deletion, or access changes.

## Script principles

Scripts must be non-interactive, deterministic where possible, and produce structured output. No script may collect telemetry by default. Mock connectors must use sanitized local fixtures.
