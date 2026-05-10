Design proven winning A/B test patterns for a new client, adapted to their brand guidelines.

Client slug: $ARGUMENTS

## Overview
This skill takes the 80+ winning A/B tests from the database (proven across 10+ clients) and generates ready-to-implement HTML designs for each pattern — adapted to the client's brand colors, fonts, products, USPs, and copy voice. These designs become the starting point for every new client engagement.

## Pre-requisites (MUST exist before running)
- `clients/{slug}/brand/brand-dna.md` — colors, fonts, logo, USPs, button styles
- `clients/{slug}/brand/brand-voice.md` — tone, CTA language
- `clients/{slug}/brand/icp-cards.md` — customer profiles
- Product data (from `/research-client` scrape) — product names, prices, images, reviews

Read ALL brand files first. Set CSS variables from brand-dna.md before building anything.

## What to Design

Generate a self-contained HTML file for EACH page type below. Each file contains all the winning test patterns for that page, styled to the client's brand. Use real product data, real prices (in client's currency), real USPs from brand-dna.md, and real review data if available.

---

### File 1: `winning-tests-homepage.html`

**Patterns to implement:**
1. **Circle/icon navigation** — visual category nav with product images in circles (+10.1% RPV)
2. **Search bar visible ATF** — prominent search with trending searches dropdown (+11.3% RPV)
3. **Benefit sliding bar ATF** — scrolling USP strip below hero with brand USPs (+8.4% RPV)
4. **"Why Choose Us" section** — 3-4 column grid with icons and brand differentiators (+6.4% RPV)
5. **UGC section** — customer photos grid with review quotes (+12.8% RPV)
6. **Optimized header** — announcement bar + nav with collections + search (+28.1% RPV)

---

### File 2: `winning-tests-collection.html`

**Patterns to implement:**
1. **2x2 grid mobile** — product cards in 2-column grid on mobile (+10.4-26.6% RPV)
2. **Infinite scroll** — load more products on scroll, no pagination (+5.9% RPV)
3. **Image carousel on cards** — swipeable product images on each card (+16.7% RPV)
4. **Add to Cart on collection** — ATC button directly on product card (+24.4% RPV)
5. **Ratings/reviews on cards** — star rating + review count on every card (+4.9-27.4% RPV)
6. **Full product title** — show complete title, not truncated (+15.5% RPV)
7. **Brand policies/USPs inline** — USP cards mixed into the product grid (+15.8-20.1% RPV)
8. **Best Seller / Most Liked labels** — badges on top-performing products (+10.3% RPV)
9. **Mini USP strip** — compact trust bar above the grid (+5.0% RPV)
10. **Filters outside** — visible filter pills, not hidden in a drawer (+4.4% RPV)
11. **Quick ATC in card** — mini add-to-cart button on hover/tap (+8.3% RPV)
12. **Savings anchor on card** — "Save X%" or per-unit price on bundle cards (+9.7% RPV)

---

### File 3: `winning-tests-pdp.html`

**Patterns to implement:**
1. **USPs above the fold** — trust badges/benefits strip above ATC (+23.1% RPV)
2. **Estimated delivery date** — dynamic "Arrives by [date]" with shipping tracker (+13.7-19.4% RPV)
3. **Price anchoring** — compare price + savings in both % and $ (+14.2-18.2% RPV)
4. **Customer photos ATF** — real customer images in the product gallery (+6.2% RPV)
5. **Variant selector with images** — visual swatches, not text dropdowns (+17.4% RPV)
6. **Sticky CTA** — floating Add to Cart bar on scroll (+8.0% RPV)
7. **Free shipping with price** — "Free shipping" badge next to price (+6.1% RPV)
8. **Thumbnails on PDP** — thumbnail strip below main image (+4.3% RPV)
9. **Stock urgency** — "Only X left in stock" indicator (+7.0-11.8% RPV)
10. **Us vs Them comparison** — side-by-side table: client vs competitors (+10.5% RPV)
11. **Upsells above ATC** — cross-sell products above the Add to Cart button (+5.2-18.1% RPV)
12. **Prebuilt bundles** — bundle selector cards with save % badges (+4.9% RPV)
13. **Product USP infographics** — visual icons for key product benefits (+6.0% RPV)
14. **Search bar visible on PDP** — search accessible from product page (+5.6% RPV)
15. **"2 Free Gifts" offer** — gift-with-purchase callout (+31.4% RPV)
16. **Microcopy near CTA** — "This takes 30 seconds" or similar reassurance (+1.6% RPV)

---

### File 4: `winning-tests-cart.html`

**Patterns to implement:**
1. **Cart drawer** (not cart page) — slide-out drawer on ATC (+10.4% RPV)
2. **Free shipping progress bar** — "Add Rs.X more for free shipping" (+1.3-8.2% RPV)
3. **Cart USPs/trust badges** — trust elements in the cart (+3.8-14.9% RPV)
4. **"Save $xx" display** — show total savings in cart (+11.9% RPV)
5. **Cart add-ons** — cross-sell products with mini ATC buttons (+34.7% RPV)
6. **Expected delivery in cart** — delivery date estimate in cart (+2.1% RPV)
7. **Urgency in cart** — "Items reserved for 15:00" timer (+7.3% RPV)
8. **Free gift progress bar** — "Add X more to unlock free gift" (+10.1% RPV)
9. **TrustPilot/review ratings** — star rating in cart (+3.8% RPV)

---

### File 5: `winning-tests-mobile-menu.html`

**Patterns to implement:**
1. **Best seller tabs** — horizontal scrollable product carousel at top (+6.4-11.3% RPV)
2. **Best seller slider** — swipeable cards with image, title, price, mini ATC (+11.3% RPV)
3. **Offer banner in menu** — promotional banner between nav items (+6.5% RPV)
4. **Brand link optimization** — brand story/about link with visual treatment (+1.0% RPV)

---

### File 6: `winning-tests-checkout.html`

**Patterns to implement:**
1. **Testimonial slider** — rotating customer quotes on checkout (+4.8% RPV)
2. **Upsell at checkout** — last-chance add-on offer (+11.4% RPV)
3. **Stock urgency** — "Only X left" on checkout items (+10.4% RPV)
4. **Checkout USPs** — trust badges below payment form (+2.1% RPV)
5. **Checkout urgency** — countdown timer for reservation (+2.8% RPV)

---

### File 7: `winning-tests-sitewide.html`

**Patterns to implement:**
1. **Trending searches on search bar** — popular searches dropdown (+10.4% RPV)
2. **USPs ATF sitewide** — persistent benefit bar across all pages (+4.5% RPV)
3. **Best seller on search** — product results in search dropdown (+6.6% RPV)
4. **USP announcement bar** — scrolling marquee with key benefits (+4.8% RPV)

---

## Design Rules
- **Read brand-dna.md FIRST** — set all CSS variables from it (primary, secondary, background, text, font, border-radius, logo URL)
- **Use brand font** via Google Fonts import
- **Currency in client's local format** (Rs. for PKR, $ for USD, etc.)
- **Use real product data** — actual product names, prices, images from the scrape
- **Use real USPs** from brand-dna.md, not generic placeholders
- **Use real review data** if available from review-mining
- **Each file must be self-contained** — embedded CSS and JS, no external dependencies
- **Mobile-first** — all patterns must work on 390px width
- **No emojis** unless the brand uses them
- **Match card styling** from the original site (border-radius, shadows, grid columns)
- **Each pattern gets a labeled section** with the test name, expected RPV lift, and number of clients it won for as a comment/header

## Annotations
Add a comment block above each pattern with:
```html
<!-- WINNING TEST: [Pattern Name]
     RPV Lift: +X.X% average
     Won for: [Client1, Client2, Client3]
     Revenue impact: $XX,XXX/mo average
     Priority: [Universal Winner / High Confidence / Worth Testing]
-->
```

## Output
Save all files to `clients/{slug}/designs/winning-tests/`
```
winning-tests/
  winning-tests-homepage.html
  winning-tests-collection.html
  winning-tests-pdp.html
  winning-tests-cart.html
  winning-tests-mobile-menu.html
  winning-tests-checkout.html
  winning-tests-sitewide.html
```

Publish the folder to here.now so the client can preview all patterns live.

## Why This Matters
These 80+ patterns have been proven across 10+ real stores with measured RPV/CVR lifts and monthly revenue impact. Instead of designing from scratch and guessing what works, every new client starts with a library of proven winners already adapted to their brand. This compresses the first round of A/B testing from "what should we try?" to "which proven winner do we launch first?"

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
