# GitHub publish checklist — v0.2.0

## Suggested repository settings

- Repository: `duan-growth-skills`
- Description: `Evidence-first Agent Skills for multi-channel growth intelligence, secure account integration, AI evaluation, experimentation, and approval.`
- Website: `https://duandigi.com`
- License: MIT
- Default branch: `main`

## Suggested topics

`agent-skills`, `growth-marketing`, `growth-hacking`, `claude-code`, `ai-agents`, `marketing-analytics`, `multi-channel`, `oauth`, `experimentation`, `attribution`, `seo`, `paid-media`, `crm`, `marketing-automation`, `open-source`

## Before publishing

- [ ] Confirm maintainer links and private security contact path
- [ ] Run `make validate`
- [ ] Run `claude plugin validate . --strict` on a Mac with Claude Code installed
- [ ] Confirm all example account IDs, domains, leads, and provider payloads are synthetic or sanitized
- [ ] Confirm no `.env`, token, secret, password, cookie, private key, or authorization header is present
- [ ] Review provider capabilities and permission guidance against current official documentation
- [ ] Test the mock connector and all benchmark cases
- [ ] Create or update the GitHub repository
- [ ] Confirm GitHub Actions passes
- [ ] Create release `v0.2.0`
- [ ] Enable Discussions and pin the community evaluation issue if public feedback is desired

## Initial push commands

```bash
git init
git add .
git commit -m "feat: publish Duan Growth Skills v0.2.0"
git branch -M main
git remote add origin https://github.com/duandigi/duan-growth-skills.git
git push -u origin main
```

## Existing v0.1 repository

```bash
git checkout -b release/v0.2.0
git add .
git commit -m "feat: add multi-channel integration and AI evaluation layer"
git push -u origin release/v0.2.0
```

Open a pull request, review the diff, merge after CI passes, then tag:

```bash
git tag -a v0.2.0 -m "Duan Growth Skills v0.2.0"
git push origin v0.2.0
```

## Suggested release title

`Duan Growth Skills v0.2.0 — multi-channel AI growth intelligence`

## Suggested announcement

Duan Growth Skills v0.2.0 is an open, evidence-first collection of 30 Agent Skills for growth strategy, secure account integration, project-to-asset mapping, data quality, cross-channel normalization, SEO, paid media, social, local search, CRM, anomaly detection, attribution, AI evaluation, health scoring, experimentation, and approval-safe optimization. The release includes mock connectors, deterministic utilities, schemas, 90 evals, and public benchmark cases. Real credentials are never included, and high-impact actions remain human-approved.
