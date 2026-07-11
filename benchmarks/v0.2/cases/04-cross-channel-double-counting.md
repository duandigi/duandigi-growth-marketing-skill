# Case 04 — Cross-channel double counting

## Prompt

Google Ads reports 70 conversions, Meta Ads reports 55, GA4 reports 82 key events, CRM has 61 unique leads, 37 qualified leads, and 12 wins. Produce the total number of conversions and attribute them to channels.

## Expected strengths

- Refuses to add provider totals as unique conversions.
- Preserves provider-reported, analytics-observed, CRM-unique, qualified, and won layers.
- Explains attribution windows and identity limitations.
- Reports what is known and proposes reconciliation or incrementality work.
