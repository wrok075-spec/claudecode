---
name: visual-audit
description: Run a Visual CRO Audit using Playwright screenshots and the winning test database.
---

Run a Visual CRO Audit using Playwright screenshots and the winning test database.

Client store URL: $ARGUMENTS

## Step 1: Playwright Screenshot Capture

### Mobile (iPhone 14 Pro, 390x844, isMobile: true)
- **Homepage:** above fold, then scroll in 85% viewport increments capturing each stop (8-10 screenshots), plus full-page
- **Mobile menu:** click hamburger, screenshot open drawer, check sub-menus
- **Collection page:** above fold, scroll through product grid, capture filters/sort, full-page
- **PDP (top product):** above fold, scroll through pricing/variants, CTA area, description, FAQ, cross-sells, reviews, full-page
- **Cart:** add product to cart, screenshot cart drawer. Then visit /cart page and screenshot

### Desktop (1440x900)
- **Homepage:** above fold, scroll through, full-page
- **Desktop nav:** hover over each nav item, screenshot dropdowns/mega menus
- **Collection page:** above fold, full-page
- **PDP:** above fold, full-page
- **Cart page:** screenshot

### At every stop:
Run `page.evaluate()` to extract headings, CTAs, badges, prices, announcements as structured JSON.

Save to `clients/{slug}/research/visual-audit-screenshots/`

## Step 2: Cross-Reference Against Winning Test Database

Read `reference_winning_tests.md` from memory. For EVERY screenshot, check the full database — not just universal winners. Mark each pattern as PRESENT (green) or MISSING (red).

### Homepage Checklist
- [ ] Circle/icon navigation (+10.1% RPV, B2D)
- [ ] Search bar visible ATF (+11.3% RPV, TC — won 3 clients)
- [ ] Benefit sliding bar / USP strip ATF (+8.4% RPV, Pittie)
- [ ] "Why Choose Us" section (+6.4% RPV, MJA)
- [ ] UGC section with customer photos (+12.8% RPV, KL)
- [ ] Optimized header / 3rd header (+28.1% RPV, BOL)
- [ ] Navigation with collections (+10.1% RPV, CC)

### Collection Page Checklist
- [ ] 2x2 grid mobile (+10.4-26.6% RPV, TC/BOL)
- [ ] Infinite scroll or load more (+5.9% RPV, B2D)
- [ ] Image carousel on cards (+16.7% RPV, BOL)
- [ ] Add to Cart on collection card (+24.4% RPV, MJA)
- [ ] Star ratings/reviews on cards (+4.9-27.4% RPV, MJA/NWTN/TC — won 3 clients)
- [ ] Full product title shown (+15.5% RPV, PSD)
- [ ] USPs/brand policies inline in grid (+15.8-20.1% RPV, PSD/KL — won 2 clients)
- [ ] Best Seller / Most Liked labels (+10.3% RPV, NWTN)
- [ ] Mini USP strip above grid (+5.0% RPV, WM)
- [ ] Filters visible, not hidden (+4.4% RPV, Pittie)
- [ ] Quick ATC in product card (+8.3% RPV, Pittie)
- [ ] Savings anchor / per-unit price on cards (+9.7% RPV, PSD — $122K/mo)

### PDP Checklist
- [ ] USPs above the fold (+23.1% RPV, B2D — won 5 clients)
- [ ] Estimated delivery date (+13.7-19.4% RPV — won 4 clients)
- [ ] Price anchoring / compare price / savings in % and $ (+14.2-18.2% RPV, TC/PSD — $157K/mo)
- [ ] Customer photos in gallery ATF (+6.2% RPV, TC)
- [ ] Variant selector with images (+17.4% RPV, TC — $97K/mo)
- [ ] Sticky CTA on scroll (+8.0% RPV, PSD — $62K/mo)
- [ ] Free shipping shown with price (+6.1% RPV, PSD — $91K/mo)
- [ ] Thumbnails on PDP (+4.3% RPV, PSD)
- [ ] Stock urgency indicator (+7.0-11.8% RPV — won 4 clients)
- [ ] Us vs Them comparison table (+10.5% RPV, Pittie)
- [ ] Upsells above ATC (+5.2-18.1% RPV, MJA/BOL)
- [ ] Prebuilt bundle selector (+4.9% RPV, NWTN)
- [ ] Product USP infographics (+6.0% RPV, Pittie)
- [ ] Search bar visible on PDP (+5.6% RPV, TC)
- [ ] Free gifts with purchase (+31.4% RPV, PD — $101K/mo)
- [ ] Microcopy near CTA (+1.6% RPV, WM)
- [ ] TrustPilot/review photos in gallery (+4.5% RPV, TC)

### Mobile Menu Checklist
- [ ] Best seller tabs/slider (+6.4-11.3% RPV — won 3 clients)
- [ ] Offer banner in menu (+6.5% RPV, PSD)
- [ ] Brand link with visual treatment (+1.0% RPV, PSD)

### Cart Checklist
- [ ] Cart drawer (not cart page) (+10.4% RPV, B2D — $72K/mo)
- [ ] Free shipping progress bar (+1.3-8.2% RPV, B2D/KL)
- [ ] Cart USPs/trust badges (+3.8-14.9% RPV — won 3 clients)
- [ ] "Save $xx" total savings display (+11.9% RPV, B2D)
- [ ] Cart add-ons / cross-sells (+34.7% RPV, MJA)
- [ ] Expected delivery in cart (+2.1% RPV, MJA)
- [ ] Urgency timer in cart (+7.3% RPV, BOL)
- [ ] Free gift progress bar (+10.1% RPV, Pittie)
- [ ] Review ratings in cart (+3.8% RPV, TC — $46K/mo)

### Checkout Checklist
- [ ] Testimonial slider (+4.8% RPV, PD)
- [ ] Upsell at checkout (+11.4% RPV, PD — $53K/mo)
- [ ] Stock urgency (+10.4% RPV, NWTN — $73K/mo)
- [ ] Checkout USPs (+2.1% RPV, NWTN)
- [ ] Checkout urgency (+2.8% RPV, MJA)

### Sitewide Checklist
- [ ] Trending searches in search bar (+10.4% RPV, TC — $102K/mo)
- [ ] USPs ATF sitewide (+4.5% RPV, TC — $44K/mo)
- [ ] Best seller results in search (+6.6% RPV, PSD — $206K/mo)
- [ ] USP announcement bar (+4.8% RPV, PSD — $62K/mo)

### How to use this checklist
For every MISSING pattern:
1. **Flag it in the observation table** with the test name, RPV lift, and which clients it won for
2. **Write the A/B test recommendation** with exact control vs. variant, using the client's actual products/copy/brand
3. **Estimate revenue impact** using the client's own traffic data: (monthly sessions x current CVR x AOV x RPV lift %)
4. **Tag priority**: "Universal Winner" (won 3+ clients) > "High Confidence" (won 2 clients, >10% RPV) > "Worth Testing" (won 1 client or <5% RPV)

## Step 3: Build HTML Report

Structure by page type (Homepage, Collection, PDP, Mobile Menu, Cart). For each page:

1. **Screenshots** — embed Playwright screenshots. 2-column grid (mobile + desktop side by side). Italic captions describing what we see and what's missing.

2. **Observation table** — Element | Status (MISSING red / GOOD green) | Winning Test Evidence (test name, RPV lift %, client name, monthly revenue). Every row must cite specific test data.

3. **A/B Test recommendation** — green callout box:
   - **Control:** exact current state
   - **Variant:** exactly what to change with specific copy
   - **Evidence:** which clients this won for, RPV/CVR lifts, monthly revenue
   - **Primary metric:** what to measure

4. **Priority Test Queue** at end — ranked table: #, Test Name, Page, Avg RPV Lift, Clients Won. Top 3 highlighted in red callout.

## Step 4: Publish + PDF
- Publish full directory (HTML + screenshots folder) to here.now so screenshots render inline
- Generate PDF via Puppeteer (displayHeaderFooter: false, printBackground: true)

## Step 5: Create Notion Page in Research Database

Properties: Research Name = "Visual CRO Audit - {Client}", Link to Doc = here.now URL

Content structure:
- Header with store, currency, audit date, method, benchmarks
- Per page section: screenshots as images (here.now URLs), italic captions, observation table, A/B test callout
- Desktop Navigation section
- Priority Test Queue table
- Top 3 red callout

Screenshot embedding in Notion — use here.now URLs:
```
![Caption](https://{slug}.here.now/screenshots/{filename}.png)
```

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
