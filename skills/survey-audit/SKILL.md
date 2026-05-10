---
name: survey-audit
description: Analyze on-site and post-purchase survey responses. Categorize themes, cross-reference with existing CRO research (visual audit, GA4, competitor analysis, Shopify analytics), and generate actionable insights with test recommendations.
---

Analyze on-site and post-purchase survey data for a client.

CSV file paths: $ARGUMENTS (e.g., "/path/to/onsite-survey.csv /path/to/pps-survey.csv")

## Pre-requisite
- On-site survey CSV and/or post-purchase survey CSV exported from survey tool (Hotjar, Zigpoll, etc.)
- Read the client's existing research files BEFORE analyzing surveys

## Cross-Reference Rule (CRITICAL)
Before generating insights, read ALL of these from the client folder if they exist:
- `research/shopify-analytics.md` -- revenue data, product performance, discount patterns
- `research/visual-audit-report.html` -- existing test recommendations
- `research/competitor-analysis.md` -- competitor patterns
- `research/ga4-analysis-report.html` or `ga4-audit.md` -- funnel leaks
- `research/fbt-analysis-report.html` -- co-purchase patterns
- `research/rapid-research.md` -- product and customer insights
- `research/review-mining.md` -- customer voice data
- `research/clarity-audit.md` -- heatmap and session recording findings
- `brand/icp-cards.md` -- ideal customer profiles and objections

Every insight MUST cite the survey response(s) that triggered it AND cross-reference at least one other research source when a connection exists.

## Process

### Step 1: Read and Parse CSVs
- Read both CSV files
- Identify column headers (question text is usually in the header)
- Count total responses per survey
- Note: responses may have line breaks, quotes, and special characters -- handle gracefully

### Step 2: Categorize Every Response
Read EVERY response and assign it to a theme category. Don't skip any.

Standard theme categories (adapt based on what emerges):
- **UX/Navigation Issues** -- site doesn't work, can't find things, confusing layout
- **Pricing/Value Concerns** -- too expensive, want discounts, unclear value
- **Trust/Credibility** -- skeptical, want more proof, worried about scams
- **Subscription Complaints** -- didn't want auto-ship, confused about recurring billing
- **Product Information Gaps** -- want more details on ingredients, how-to-use, side effects
- **Shipping/Delivery** -- shipping cost, speed, international availability
- **Product Requests** -- want new products, bundles, sizes
- **Positive Feedback** -- what's working well, why they chose this brand
- **Competitor Mentions** -- why they switched from competitor, comparisons
- **Returns/Guarantee** -- money-back guarantee questions, return process
- **Social Proof Needs** -- want more reviews, before/afters, testimonials
- **Technical Issues** -- broken pages, checkout errors, mobile bugs

### Step 3: Quantify Themes
For each theme:
- Count how many responses fall into it
- Calculate % of total responses
- Pull 3-5 verbatim quotes that best represent the theme
- Flag themes that appear in 10%+ of responses as HIGH PRIORITY

### Step 4: Cross-Reference with Existing Research
For each high-priority theme, check:
- Does the visual audit already have a test for this? If so, this survey data VALIDATES that test.
- Does GA4 data show a funnel leak related to this theme? (e.g., subscription complaints + checkout abandonment)
- Did competitors solve this problem? How?
- Does the FBT analysis reveal relevant co-purchase patterns?
- Does the Clarity audit show related behavioral patterns (rage clicks, dead zones)?

### Step 5: Generate Insights

## Report Structure (8 sections)

### 1. Executive Summary
- Total responses analyzed (on-site + PPS)
- Top 3 themes by volume with response counts
- 1 red callout: biggest problem customers are telling you about
- 1 green callout: biggest strength customers confirm

### 2. On-Site Survey Analysis
For each question in the on-site survey:
- Question text
- Total responses
- Theme breakdown table: Theme | Count | % | Key Quotes
- Top insight from this question

### 3. Post-Purchase Survey Analysis
Same structure as above, per question:
- Question text
- Total responses
- Theme breakdown table
- Top insight

### 4. Theme Deep-Dives (Top 5 themes)
For each of the top 5 themes by volume:
- **Theme name + response count + %**
- **Verbatim quotes** (5-8 best examples, cleaned up but faithful to original)
- **Cross-reference with existing research:**
  - Which visual audit test does this validate?
  - Which GA4 funnel leak does this explain?
  - Which competitor does this better?
  - What does the FBT/analytics data add?
- **Recommended action** -- specific, actionable, tied to data

### 5. Voice of Customer (VoC) Goldmine
Pull the most powerful verbatim quotes that could be used for:
- Ad copy angles (frustrations, desires, language patterns)
- Landing page headlines
- Objection-handling copy
- Testimonial-style social proof
- Email subject lines

Format as a table: Quote | Use Case | Where to Deploy

### 6. Subscription Analysis (if relevant)
If subscription complaints appear:
- Count and categorize subscription-related responses
- Identify the root cause (confusion at checkout? unexpected charges? hard to cancel?)
- Cross-reference with checkout funnel data
- Specific recommendations for subscription UX

### 7. New Test Ideas from Survey Data
Tests that emerge from survey responses but weren't in existing research:
- Test name, hypothesis, data source (survey quotes), expected impact
- These are NEW insights the survey revealed that other research missed

### 8. Priority Matrix
Table: # | Theme | Survey Volume | Validates Existing Test? | New Insight? | Priority | Recommended Action

## Output
- Styled HTML report: `clients/{slug}/research/survey-audit-report.html`
- Save markdown: `clients/{slug}/research/survey-audit.md`
- Publish HTML to here.now
- Generate PDF: `{Brand}-Survey-Audit-Validare.pdf` (portrait, A4, `@page{margin:40px 24px 24px 24px}`)
- Create Notion research page with FULL content
- Generate 5-8 insights in the Notion Insights database

## Styling
- Use client's brand fonts and colors from brand-dna.md or CLAUDE.md
- Validare logo: `https://framerusercontent.com/images/9JLB1g4I28JoADbhY2CFdXt2P0.png`
- Print-ready: `@page{margin:40px 24px 24px 24px}`, font-size 11px min, `break-inside:avoid` on all cards/tables
- Color classes: .good (green), .bad (red), .warn (amber)
- Verbatim quotes should be styled as blockquotes with a left border

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
