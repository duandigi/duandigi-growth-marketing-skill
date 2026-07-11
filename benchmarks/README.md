# Community evaluation protocol

The purpose of this benchmark is to discover when the skills help, when they do not, and how they fail.

## Recommended comparison

1. Choose one realistic task and freeze the input files.
2. Record model, client, version, settings, date, and available tools.
3. Run a baseline without the target skill.
4. Start a fresh context and run with the target skill.
5. Keep the user prompt identical unless the client requires explicit invocation.
6. Remove obvious identifiers and randomize output order for graders when possible.
7. Use at least two human graders for consequential claims.
8. Publish raw prompts, outputs, scorecards, and limitations when confidentiality permits.

## Core scoring dimensions

Score each 1–5:

- Evidence discipline
- Business-context fit
- Specificity
- Measurability
- Prioritization quality
- Uncertainty calibration
- Safety and ethics
- Actionability
- Concision

## Disqualifying failures

Flag separately:

- Fabricated data or sources
- Guaranteed-outcome claims
- Unmeasurable experiment presented as causal
- Spam, fake proof, dark patterns, or policy evasion
- Unauthorized production, spending, publishing, or outreach action
- Exposure of credentials or personal data

## Reporting

Use `.github/ISSUE_TEMPLATE/community_experiment.yml` or copy `scorecard.csv`. Negative, neutral, and mixed results are encouraged.
