---
name: competitor-audit
description: Run a full competitor analysis with screenshots and A/B test recommendations.
---

Run a full competitor analysis with screenshots and A/B test recommendations.

Competitor URLs (comma-separated) or "use onboarding form": $ARGUMENTS

## Pre-requisites
- Client brand files must exist (`clients/{slug}/brand/brand-dna.md`)
- GA4 audit or Shopify analytics should be done first (for data-backed test recs)

## Step 1: Firecrawl JSON Scrape (all competitors in parallel)

### Homepage scrape — extract:
- Brand name, hero headline/subheadline/CTA, announcement bar text
- Navigation items, USPs, trust badges, social proof (reviews count, rating, happy customers claim)
- Products shown with prices and compare prices
- Subscription offers, guarantee text, free shipping threshold
- Bundle offers, urgency/scarcity elements, media endorsements

### Top PDP scrape — extract:
- Product title, price, compare price, variant options
- Bundle tier pricing (tier name, price, per-unit, savings)
- Subscription details (available, discount %, details)
- Trust badges, guarantee text, shipping info
- Reviews count and rating, CTA button text
- Urgency elements, cross-sell products, FAQ (yes/no), ingredients shown

## Step 2: Playwright Deep Scrape — Mobile + Desktop Screenshots

### Pass A: Mobile (iPhone 14 Pro — 390x844, isMobile: true, hasTouch: true)

For each competitor, scroll through and screenshot every section:

**Homepage full scroll-through:**
- Announcement bar, hero above fold, trust bar/USP strip, featured products grid, social proof section, value props/"why us", footer, full-page screenshot

**PDP full scroll-through:**
- Above fold, pricing/variant/bundle selector, value stack, CTA area, product description/benefits, ingredients, FAQ/accordion, cross-sells, reviews section, trust/guarantee, full-page screenshot

**Mobile menu:**
- Click hamburger, screenshot drawer. Check sub-menus, screenshot those too.

**Cart drawer:**
- Add product to cart, screenshot. Check for: free shipping bar, upsells, trust badges, single vs dual CTA.

### Pass B: Desktop (1440x900)

**Homepage:** Above fold, hover nav items for mega menus (screenshot each), scroll through, full-page.
**PDP:** Above fold (gallery, sticky sidebar), desktop-specific elements, full-page.
**Desktop navigation:** Hover each nav item, screenshot dropdowns.
**Cart:** Screenshot desktop cart page/drawer.

### At every screenshot stop:
Run `page.evaluate()` to extract visible text content, headings, CTA text, badge text. Save as structured JSON alongside screenshots.

### Save screenshots to:
```
clients/{slug}/research/competitor-screenshots/
  {competitor-name}/
    mobile-homepage-hero.png
    mobile-homepage-trust-bar.png
    mobile-pdp-above-fold.png
    mobile-pdp-pricing-urgency.png
    mobile-menu.png
    mobile-cart-drawer.png
    desktop-homepage-hero.png
    desktop-nav-mega-menu.png
    desktop-pdp-above-fold.png
    ...
```

## Step 3: Build Comparison Tables (HTML Report)

Sections in order:
1. **Competitor Overview** — brand, domain, hero product, price range, reviews, rating, positioning
2. **Pricing & Bundle Strategy** — single unit price, best bundle, per-unit at best tier, subscription discount
3. **PDP Feature Comparison** — table: bundle selector, subscription, guarantee, free shipping, testing, endorsements, urgency, cross-sells, FAQ, ingredients, sticky ATC, compare price, payment icons
4. **Mobile PDP Deep Dive** — image count, sticky ATC, FAQ count, cross-sells, bundle subtitle style, CTA text
5. **Trust & Social Proof** — on-site reviews, Trustpilot, happy customers claim, certifications, medical authority
6. **Homepage & Brand Strategy** — hero headline, announcement bar, SKU count, target audience, nav depth
7. **What Competitors Do Better** — steal-worthy patterns (green callout boxes)
8. **Client's Advantages to Protect** — what client already does well
9. **Competitive Gaps** — table: gap, current state, competitor evidence, opportunity

## Step 4: Cross-Reference with Winning Test Database

Read `reference_winning_tests.md` from memory. For every competitor pattern observed, check if it matches a winning test from the database. This adds a second layer of evidence beyond "competitor X does this":

**When a competitor pattern matches a winning test:**
- Flag it as **double-validated** — competitor evidence + winning test data
- Include both the competitor screenshot AND the winning test stats (RPV lift, clients won, revenue)
- This makes the recommendation near-bulletproof: "Competitor does it + it won for 3+ other clients"

**When the client is missing a universal winner that competitors also don't have:**
- Still recommend it — the winning test data alone is sufficient evidence
- Note: "Neither the client nor competitors have this — first-mover advantage opportunity"

**When a competitor does something NOT in the winning test database:**
- Still recommend testing it, but tag as "Competitor-inspired — no winning test data yet"
- Lower priority than database-backed recommendations

## Step 5: Screenshot-Backed A/B Test Recommendations

Each test is a self-contained card:
1. **Screenshot** — the actual competitor screenshot proving the pattern
2. **"What [Competitor] Does"** — what we see and why it works
3. **Winning Test Evidence** (if match found) — test name, RPV lift, clients won, monthly revenue from the database
4. **"What [Client] Should Test":**
   - **Control:** current state on client's site
   - **Variant:** exactly what to change, with specific copy/elements
   - **Why:** connect competitor evidence + winning test data to client's own analytics (bounce rate, ATC rate, CVR, AOV from GA4/ShopifyQL)
   - **Primary metric:** what to measure
   - **Estimated impact:** revenue estimate using client's traffic/conversion data
   - **Confidence level:** "Double-validated" (competitor + winning test) / "Winning test backed" / "Competitor-inspired"

Every test MUST reference specific numbers from client's analytics.

### Priority Ranking Rules
1. **Double-validated** tests (competitor does it + winning test data) = highest priority
2. **Universal winners** missing from both client AND competitors = high priority (first-mover)
3. **Winning test backed** (no competitor evidence, but won for 3+ clients) = medium-high priority
4. **Competitor-inspired** (no winning test data) = worth testing, lower priority

## Output
- Styled HTML report with embedded screenshots → publish to here.now
- PDF via Puppeteer (displayHeaderFooter: false, printBackground: true)
- Save to `clients/{slug}/research/competitor-analysis.md`

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
