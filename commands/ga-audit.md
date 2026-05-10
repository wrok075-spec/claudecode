Run a GA4 CRO Funnel Analysis for a client.

GA4 property and date range: $ARGUMENTS

## Pre-requisite
GA4 MCP must be connected with read access to the property. If not available, ask the user for the GA4 property ID.

## Cross-Reference Rule (CRITICAL)
This report does NOT exist in isolation. Before generating recommendations, read these files from the client folder if they exist:
- `research/shopify-analytics.md` -- for revenue data, discount patterns, product performance
- `research/visual-audit-report.html` -- for existing test recommendations and screenshots
- `research/competitor-analysis-report.html` or `competitor-analysis.md` -- for competitor patterns
- `research/rapid-research.md` -- for ICP and product insights

Every recommendation MUST cite its data source AND cross-reference at least one other research file when available. Format: "Source: GA4 funnel data + Visual Audit TEST 3 + Competitor Analysis (Alpha Infuse cart drawer)"

## GA4 Queries to Run

Run ALL queries for the specified date range. Run them in parallel where possible.

```
1. Overall metrics: users, sessions, purchases, revenue, CVR, AOV, engagement_rate, bounce_rate
2. Funnel steps: session_start > page_view (product pages) > add_to_cart > begin_checkout > purchase -- with user counts at each step
3. Funnel by channel: same funnel broken by sessionDefaultChannelGroup
4. Funnel by device: same funnel broken by deviceCategory
5. Funnel by user type: same funnel broken by newVsReturning
6. Funnel by product variant: item_view > add_to_cart > purchase broken by item_name or item_variant
7. Landing pages: landingPage with sessions, bounceRate, engagementRate, conversions, purchaseRevenue
8. Channel performance: sessionDefaultChannelGroup with users, sessions, CVR, AOV, purchaseRevenue, ARPU (revenue/users)
9. Device performance: deviceCategory with full funnel rates + CVR + AOV
10. Screen resolution: screenResolution with users, purchases, CVR, AOV, ARPU
11. New vs returning: newVsReturning with full funnel rates + CVR + AOV
12. Top pages by engagement: pagePath with screenPageViews, avgSessionDuration, bounceRate
```

## Report Structure (10 sections, exact order)

### 1. Executive Summary -- Key Metrics + Callouts
- 6-card metric grid: Total Users, Revenue, Purchases, CVR, AOV, Cart-to-Checkout Rate
- 3 callout boxes (auto-generated from data):
  - **Critical Leak** (red): The worst funnel drop-off with dollar impact
  - **Critical Leak** (red): The second worst funnel drop-off
  - **Bright Spot** (green): What's working well (e.g., email CVR, cart-to-checkout rate)
- Include target benchmarks: Landing-to-PDP 50-70%, PDP-to-ATC 12-18%, ATC-to-Checkout 40-60%, Checkout-to-Purchase 45-60%

### 2. Full Conversion Funnel -- Visual + Table
- Visual funnel diagram: Landing > Product View > Add to Cart > Checkout > Purchase
  - Show user count at each step
  - Show pass-through rate between each step
  - Color-code: green (above target), amber (at target), red (below target)
- Table: Funnel Stage | Rate | Target Range | Status | Users Lost
- Calculate dollar impact of each leak: users_lost x current_CVR_of_later_stages x AOV

### 3. Critical Leak Analysis -- PDP to Add to Cart
This is typically the biggest leak. Dedicate a full section:
- **By Channel**: table with Channel, Users, PDP-to-ATC rate, CVR, AOV, ARPU
- **By Device**: table with Device, Users, PDP-to-ATC rate, CVR, AOV
- **By User Type**: table with New/Returning, Users, PDP-to-ATC rate, CVR, Purchases
- **By Product Variant**: table with Product, Views, PDP-to-ATC rate, Purchase Rate
  - Flag any variant with >5,000 views and <2% ATC as a broken experience
- Include current state screenshots from visual audit if available
- 2-3 recommended tests with:
  - Wireframe mockups (current vs proposed, side by side)
  - Dollar impact estimate
  - Cross-reference to Visual Audit test number and/or Competitor pattern
  - Priority tag (Priority #1, #2, etc.)

### 4. Critical Leak Analysis -- Checkout to Purchase
Second biggest leak. Same structure:
- **By Channel**: flag worst-performing channel
- **By Device + User Type**: table
- Include competitor screenshots showing what they do at checkout (from competitor audit)
- 2-3 recommended tests with wireframes, impact, cross-references

### 5. Landing Page Analysis -- Landing to Product View
- **By Landing Category**: group pages into Homepage, Collections, Products (PDP), Pages (LP/advertorial)
  - Show Users, Landing-to-PDP rate, Bounce Rate, CVR, AOV per category
  - Flag categories with >80% bounce rate
  - Flag high-traffic categories with <1% CVR as revenue leaks
  - Highlight any category converting significantly above average
- **Top Individual Pages**: table with top 10 by traffic + top 5 by CVR
  - Flag pages with >10K sessions and <0.5% CVR
  - Flag pages with high CVR but low traffic (scaling opportunities)
- 1-2 recommended tests

### 6. Channel Performance Deep-Dive
- Table: Channel, Users, Share, CVR, Purchases, AOV, ARPU
- Sort by ARPU descending to show true channel efficiency
- Calculate multiplier: how much better the best channel converts vs the worst
- Callout boxes:
  - Flag channels with high CVR but low traffic share (scaling opportunities, especially email)
  - Flag channels with high traffic but low CVR (optimization priorities, usually paid social)
- Cross-reference with Shopify analytics acquisition data if available

### 7. Device Analysis + Screen Resolution
- **Device Summary**: table with Device, Users, Share, full funnel rates (Land-to-PDP, PDP-to-ATC, Cart-to-Checkout, Checkout-to-Purchase), CVR
  - Calculate the mobile-desktop CVR gap and dollar impact of closing it
- **Screen Resolution Breakdown**: table with Resolution, Device Name, Users, Purchases, CVR, AOV, ARPU
  - Sort by users descending, show top 12-15 resolutions
  - Flag resolutions with CVR < 0.6% as potentially broken viewports
  - Flag resolutions that outperform desktop (shows where responsive design works well)
  - Callout: identify the #1 resolution by traffic and calculate revenue impact of fixing it
- Recommended tests:
  - Sticky mobile CTA bar (addresses universal mobile ATC gap)
  - QA fix for broken viewports (specific resolution callouts)
  - Small screen optimization (320px and below)

### 8. New vs Returning Users
- Table: Segment, Users, full funnel rates, CVR, AOV
- Calculate the "trust gap" multiplier (returning CVR / new CVR)
- Callout: frame this as the core CRO challenge for cold traffic
- Cross-reference with Shopify analytics new vs returning data

### 9. Priority Action Matrix
- Table: #, Funnel Leak, GA4 Metric, Recommended Test, Source (cross-references), Dollar Impact
- Rank by estimated dollar impact descending
- Color-code top 3 rows (highest priority)
- Every row MUST have:
  - The specific GA4 metric that justifies it
  - A cross-reference to Visual Audit test and/or Competitor pattern
  - A dollar estimate (even if rough)

### 10. Summary -- 3 Actions That Move the Needle
- Styled summary box (gradient background, numbered list)
- 3 and only 3 top-priority actions
- Each includes: what to do, why (data), and combined dollar impact
- Frame around funnel stages, not individual tests

## Output Rules

### Styling
- Use client's brand fonts and colors from brand-dna.md or CLAUDE.md
- Validare logo: `https://framerusercontent.com/images/9JLB1g4I28JoADbhY2CFdXt2P0.png`
- Color classes: .good (green), .bad (red), .warn (amber)
- Monospace numbers (font-family for data values)
- Callout boxes with colored left borders (red/green/amber)
- Wireframe mockups: side-by-side current vs proposed using simple HTML/CSS
- Screenshots: reference from `research/visual-audit-screenshots/` and `research/competitor-screenshots/` folders
- Print-ready: page breaks between major sections, avoid breaking cards/tables across pages

### Wireframe Requirements
Each recommended test MUST include a wireframe mockup:
- Current state on left (slightly dimmed, labeled "Current")
- Proposed state on right (highlighted, labeled "Proposed")
- Use simple styled divs, not images
- Include realistic content from the client's actual products/prices
- Keep wireframes compact (max 200px height each)

### Dollar Impact Estimates
For every recommendation, estimate monthly revenue impact:
- Use formula: users_affected x expected_CVR_improvement x AOV
- Be conservative -- use the lower end of improvement ranges
- Show the math in the test recommendation card
- Example: "If mobile ATC improves from 6.73% to 9% on 130K mobile users: +2,951 carts x 33.89% checkout x $88 AOV = +$88K/month"

### Files to Generate
- Styled HTML report: `clients/{slug}/research/ga4-analysis-report.html`
- Save markdown: `clients/{slug}/research/ga4-audit.md`
- Publish HTML to here.now
- Generate PDF: `{Brand}-GA4-Analysis-Validare.pdf` (portrait, A4, 20mm margins)
- Create Notion research page with FULL content
- Generate 5-8 insights in the Notion Insights database

## What NOT To Do
- Never show funnel data without benchmarks/targets
- Never make a recommendation without citing GA4 data AND cross-referencing another research source
- Never estimate dollar impact without showing the math
- Never skip the wireframe mockups -- they make recommendations actionable
- Never present channel data without ARPU -- it's the true efficiency metric
- Never ignore screen resolution data -- it reveals broken viewports that are invisible in device-level analysis
