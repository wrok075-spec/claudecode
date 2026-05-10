# CRO Proposal Generator

Generate a Revenue Growth Report + CRO Proposal for a prospect. One command, full output.

Prospect info: 

## Flow

### Phase 1: Collect Info

Ask these questions in order:

1. **Your name and company** (e.g., "Muhammad Abdullah, Validare")
2. **Prospect's name and company** (e.g., "Wajid Hussain, Sonnobed")
3. **Current conversion rate?** (e.g., 1.4%)
4. **Average monthly traffic?** (e.g., 80,000)
5. **Average Order Value (AOV)?** (e.g., $89)
6. **Anticipated CVR increase?** (e.g., 20% relative or 0.20% absolute)
7. **Monthly CRO investment?** (e.g., $3,500)
8. **Which proposal types?** (Flat Fee / Performance-Based / Revenue Share / All Three)

If any info is provided in the argument, skip those questions.

### Phase 2: Calculate Revenue Growth Report

#### Core Metrics
- **Current CVR**: as provided
- **CVR Improvement**: If "20%" = relative (1.4% x 1.20 = 1.68%, improvement = 0.28%). If "0.20%" = absolute (1.4% + 0.20% = 1.60%). ASK if unclear.
- **New CVR**: Current + Improvement
- **Customers Before**: Traffic x Current CVR
- **Customers After**: Traffic x New CVR
- **Monthly Revenue Before**: Customers Before x AOV
- **Monthly Revenue After**: Customers After x AOV
- **Monthly Revenue Increase**: After - Before

#### ROI Ratios (monthly investment)
- 1 Month: Revenue Increase / Investment (X:1)
- 3 Months: (Increase x 3) / Investment
- 6 Months: (Increase x 6) / Investment
- 1 Year: (Increase x 12) / Investment
- 3 Years: (Increase x 36) / Investment

#### Net Revenue Increase (minus CRO cost)
- 1 Month: Increase - Investment
- 3 Months: (Increase x 3) - (Investment x 3)
- 6 Months through 3 Years: same pattern

#### Scenario Table
3 columns: CVR at -0.10pp, current, +0.10pp with customers, revenue growth, 1yr ROI, 3yr net gain

### Phase 3: Generate Proposals

#### Proposal 1: Flat Fee
- **Investment**: 2x monthly investment (e.g., $3,500/mo → $7,000 flat)
- One-time comprehensive CRO project
- 4 phases: Audit & Analysis → Strategic Recommendations → Implementation & Testing → Reporting

#### Proposal 2: Performance-Based Transition
- **Initial Fee**: ~1.5x monthly investment (e.g., $5,000)
- **Transition**: After measurable 15% CVR lift, move to monthly retainer at ~3x investment (e.g., $10,000/mo)
- "Our success is tied directly to yours"

#### Proposal 3: Revenue Share
- **Base Fee**: ~1.5x monthly investment (e.g., $5,000/mo)
- **Revenue Share**: 15% of incremental revenue above baseline
- Example: $14,240 increase → $2,136 share → total $7,136/mo
- "You only pay more when you're earning more"

### Each Proposal Includes:
1. Executive Summary — who, what, expected impact with revenue numbers
2. Scope of Work — 4 phases (Audit, Strategy, Implementation, Reporting)
3. Revenue Growth Report — full metrics + ROI + net revenue tables
4. Investment — specific amounts with structure explained
5. Next Steps — 3 action items
6. Signature block — prospect name, date line

## Output

Generate a single HTML file: `cro-proposal-{prospect-slug}.html`

### Styling
- Clean, professional — not flashy
- Use Validare branding by default (or CROtactic if specified):
  - Logo: `https://framerusercontent.com/images/9JLB1g4I28JoADbhY2CFdXt2P0.png`
  - Accent: #F5903E (orange)
  - Dark: #0D0D0D
- Clean tables with alternating rows
- Metric cards for key numbers
- Page breaks between each proposal type
- Print-ready (body 10px in print media query)
- Each proposal stands alone (can be sent independently)

### Also:
- Generate PDF via Playwright
- Publish to here.now

## Rules
- NEVER fabricate or round numbers beyond 2 decimal places
- Currency: $ with commas (e.g., $14,240.00)
- Percentages: 2 decimal places
- ROI ratios: rounded to nearest integer
- Use prospect's company name throughout — feels custom, not templated
- Professional but approachable tone
- Never mention AI, automation, or tools
- Investment amounts are GUIDELINES — if user specifies different, use those

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
