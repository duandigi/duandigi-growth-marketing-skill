# v0.2 multi-channel evaluation suite

This suite evaluates whether the integration and AI-evaluation skills improve decision quality, not whether they produce longer answers.

## Protocol

For each case:

1. Use the same model, settings, prompt, and files.
2. Run once without the target skill and once with it.
3. Hide which output used the skill when possible.
4. Score both outputs using `rubric.json`.
5. Record factual errors, unsupported claims, unsafe actions, omissions, and useful decisions.
6. Report negative or neutral results as well as wins.

## Cases

| Case | Target skills | Primary failure being tested |
|---|---|---|
| `01-connection-vs-performance` | connection health, data quality, AI evaluator | Calling stale or broken data a performance decline |
| `02-seo-quality-gap` | SEO analysis, CRM funnel, AI evaluator | Treating traffic growth as business growth |
| `03-paid-qualified-outcomes` | paid media, attribution | Optimizing platform CPA instead of qualified outcomes |
| `04-cross-channel-double-counting` | normalization, attribution | Adding platform conversions as unique outcomes |
| `05-approval-safety` | approval planner, ethics review | Executing a high-impact action without approval or rollback |

Submit sanitized results through the community experiment issue form. Never include credentials, personal lead data, or confidential client identifiers.
