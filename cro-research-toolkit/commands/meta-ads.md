Run a Meta Ad Library analysis for a brand and its competitors.

Meta Ad Library URL(s) — comma-separated (e.g. https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=fleava): $ARGUMENTS

## Pre-requisites
- Client brand files must exist (`clients/{slug}/brand/brand-dna.md`)
- Shopify analytics and/or visual audit should be done first (for cross-referencing)

## Step 1: Parse Input URLs

- Extract the brand name and search query from each Meta Ad Library URL
- If only one URL is provided, that's the client. Ask if they want competitor ad analysis too.
- If multiple URLs, first = client, rest = competitors

## Step 2: Scrape Meta Ad Library Pages

Use Playwright (from `clients/{slug}/research/node_modules/`) to scrape each Meta Ad Library URL.

### Browser Setup (CRITICAL)
- Set `locale: 'en-US'` and `timezoneId: 'America/New_York'` — prevents non-English UI rendering
- Desktop viewport: 1440x900
- Use `domcontentloaded`, waitFor 8000ms
- Dismiss cookie/consent banners via `page.evaluate()`

### For each URL:
1. Navigate to the Meta Ad Library URL
2. Wait for ads to load (check for `.x1lliihq` or ad card elements)
3. Scroll through to load more ads (3-5 scroll cycles with 3s waits)
4. Use `page.evaluate()` to extract from each visible ad card:
   - Ad status (Active/Inactive)
   - Start date (launched date)
   - Ad creative type (Image/Video/Carousel)
   - Ad copy (primary text, headline, description, CTA)
   - Landing page URL
   - Platforms (Facebook, Instagram, Messenger, Audience Network)
5. Screenshot the full library page — save to `clients/{slug}/research/meta-ads-screenshots/`
6. Also dump the full page text via `page.evaluate(() => document.body.innerText)` for parsing

### Save raw data to:
```
clients/{slug}/research/
  fleava-meta-ads-raw.json      (raw extracted data)
  meta-ads-page-text.txt        (full page text dump)
  meta-ads-screenshots/
    {brand}-ad-library-1.png
    {brand}-ad-library-2.png
    ...
```

## Step 3: Parse & Analyze Ad Data

From the raw data, build analysis across these dimensions:

### 3a. Creative Format Split
- Count: Image ads vs Video ads vs Carousel ads
- Percentage breakdown
- Which format has the longest-running ads (longevity = likely winners)

### 3b. Copy Angle Analysis
- Categorize each ad's primary text into angles:
  - Problem/Pain (e.g., "Tired of hair loss?")
  - Social Proof (e.g., "Join 60,000+ customers")
  - Offer/Deal (e.g., "40% off today")
  - Authority/Science (e.g., "Clinically proven")
  - Transformation/Results (e.g., "See results in 90 days")
  - UGC/Testimonial (e.g., "I tried this and...")
  - Education (e.g., "Did you know copper peptides...")
- Count and rank by frequency

### 3c. Landing Page Strategy
- Which URLs do ads point to? (PDP, collection, landing page, advertorial)
- Cross-reference with Shopify analytics if available (which landing pages convert best)

### 3d. CTA Analysis
- Most common CTAs (Shop Now, Learn More, Get Offer, etc.)
- CTA by ad format (do video ads use different CTAs than image ads?)

### 3e. Ad Longevity
- Sort ads by start date (oldest = longest running = likely best performers)
- Flag "evergreen" ads running 60+ days — these are proven winners
- Flag recently launched ads (last 14 days) — testing phase

### 3f. Competitor Comparison (if multiple URLs)
- Side-by-side: format split, copy angles, CTAs, landing pages
- What competitors do that the client doesn't
- What the client does that competitors don't

## Step 4: Cross-Reference with CRO Research

Connect ad findings to existing research:
- If visual audit exists: Do landing pages match what we recommended fixing?
- If Shopify analytics exists: Do ad landing pages match high-traffic/low-CVR pages?
- If competitor analysis exists: Do competitor ads use patterns we flagged?
- If FS test research exists: Do ad angles align with test hypotheses?

For every connection found, note it explicitly: "The Meta Ad Library shows [finding]. We recommended [TEST X] in the [report] to address this."

## Step 5: Build HTML Report

### Report Structure:
1. **Cover** — Validare x [Brand], "Meta Ad Library Analysis", date, total ads analyzed
2. **Executive Summary** — 3 red callout boxes for critical findings + key metrics grid (total ads, format split, avg age, top angle)
3. **Creative Format Split** — visual cards showing Image vs Video vs Carousel counts + percentages
4. **Ad Longevity Timeline** — bar chart showing ads by age bucket (0-7d, 7-30d, 30-60d, 60-90d, 90d+)
5. **Copy Angle Breakdown** — ranked table of angles with count, percentage, example ad copy
6. **Landing Page Strategy** — table of destination URLs with ad count per URL, cross-referenced with CVR data if available
7. **CTA Analysis** — distribution of CTAs across all ads
8. **Top Performing Ads** — the 5-8 longest-running ads (likely winners) with full copy, format, CTA, landing page, and days active
9. **Competitor Comparison** (if applicable) — side-by-side format split, angle strategy, landing pages
10. **CRO Opportunities** — specific recommendations derived from ad analysis, each cross-referenced with existing CRO research
11. **Priority Action Matrix** — ranked table of recommended actions with source reference

### Styling:
- Match existing report CSS (use client's brand colors from brand-dna.md)
- Validare logo in cover: `https://framerusercontent.com/images/9JLB1g4I28JoADbhY2CFdXt2P0.png`
- Footer: "Validare x [Brand] | Meta Ad Library Analysis | [Month Year]"
- Use `filter:brightness(10)` on logo for dark/gradient backgrounds
- Branded as "Validare x [Brand]" collaboration framing

### Save to:
```
clients/{slug}/research/meta-ads-report.html
```

## Step 6: Generate PDF

Use Playwright to generate PDF:
```javascript
await page.pdf({
  path: '{Brand}-Meta-Ads-Analysis-Validare.pdf',
  format: 'A4',
  printBackground: true,
  displayHeaderFooter: false,
  margin: { top: '20mm', bottom: '20mm', left: '15mm', right: '15mm' }
});
```

Save to `clients/{slug}/research/{Brand}-Meta-Ads-Analysis-Validare.pdf`

## Step 7: Publish

Create a clean publish directory with ONLY the HTML report + referenced screenshots. Publish to here.now.

## Rules

### Language Rules (client-facing output)
- NEVER mention: Playwright, Firecrawl, scraping, crawling, AI, Claude, automation, bot, script
- NEVER mention: "Data source", "Method", "Methodology"
- Present findings as expert analysis, not database lookups
- Use "Observed" instead of "scraped" or "extracted"

### Data Rules
- Only analyze ads that are actually visible and extractable
- If the Ad Library page is blocked or shows no results, note this and suggest the user check manually
- Never fabricate ad data — only report what was actually captured
- If Firecrawl can supplement Playwright data (e.g., landing page scrapes), use it but watch credit limits on infinite-scroll pages

### Screenshot Rules
- Set `locale: 'en-US'` — never include non-English UI in reports
- Dismiss all popups/banners before capturing
- Verify screenshots show actual ad content, not error pages or captchas
- If screenshots can't be captured, omit silently

### Cross-Reference Rules
- Every finding MUST reference existing CRO research if it connects
- Format: "The data shows [metric]. We recommended [TEST X] in the [report] to address this."
- If a finding has no matching prior research, label it "Meta Ads Insight"

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
