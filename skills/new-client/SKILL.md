---
name: new-client
description: Set up a new Shopify client project from scratch.
---

Set up a new Shopify client project from scratch.

Client URL or brand name: $ARGUMENTS

## Step 1: Collect Client Info

If not provided in $ARGUMENTS, ask for:
- Client/brand name
- Store URL (e.g. storename.myshopify.com)
- Is this CROtactic or Validare?
- Is this a new build (Type A) or CRO client (Type B)?
- Live theme name or ID (if known)

Do NOT ask for fonts, colors, or design rules — we scrape those automatically in Step 3.

## Step 2: Create Folder Structure

Create the full project folder structure under the current working directory:

```
clients/{slug}/
  brand/
    brand-dna.md          ← colors, fonts, logo, USPs, button styles (auto-generated)
    brand-voice.md        ← tone, CTA language, headline style (auto-generated)
    icp-cards.md          ← ideal customer profiles (auto-generated)
  research/
    shopify-analytics.md
    visual-audit-screenshots/
    competitor-screenshots/
    competitor-analysis.md
    review-mining.md
    ga4-audit.md
    clarity-audit.md
    rapid-research.md
    pain-point-analysis.md
    fs-test-research.md
  designs/
    winning-tests/        ← 7 HTML files from /winning-tests-design
    hero-section.html
    collection-page.html
    product-page.html
    mobile-menu.html
    cart-drawer.html
  assets/
    images/               ← scraped product images
    logo/                 ← brand logo files
    fonts/                ← any custom font files
  theme/                  ← Shopify theme files (pulled via CLI)
```

Create ALL folders. Leave files empty — they get populated by the research skills.

## Step 3: Auto-Scrape Brand Assets

Run `/research-client {store-url}` immediately after folder setup. This:
1. Scrapes the live site for colors, fonts, logo, button styles, card styles
2. Extracts products, prices, images, nav items, USPs, trust badges
3. Generates `brand-dna.md`, `brand-voice.md`, `icp-cards.md`
4. Saves scraped product images to `assets/images/`
5. Saves logo to `assets/logo/`

## Step 4: Shopify CLI Auth

Run: `shopify store auth --store {store-id}.myshopify.com --scopes read_orders,read_products,read_customers,read_inventory,read_reports`

All on one line, no spaces in scopes. The `read_reports` scope is critical for ShopifyQL.

If collaborator access is denied, tell user to install the shopify-cli-connector-app or create a custom app with these scopes.

## Step 5: Create CLAUDE.md

Create `CLAUDE.md` in the client folder root (`clients/{slug}/CLAUDE.md`) with:

```
# {Brand Name} — Shopify Client

## Store
- Domain: {storename.myshopify.com}
- Agency: {CROtactic / Validare}
- Client type: {Type A (new build) / Type B (CRO)}
- Live theme: {theme name/ID}
- Draft theme: TBD

## Push Rules
- Always push to DRAFT first. Never push to live without asking.
- Confirm with client before any live push.

## Brand (from brand-dna.md)
- Primary: {hex from scrape}
- Secondary: {hex from scrape}
- Headline font: {from scrape}
- Body font: {from scrape}
- Button style: {border-radius, colors from scrape}
- Card style: {border-radius, shadows from scrape}

## Design Rules
- CTA buttons: full-width on mobile
- Arrival date = today + {delivery window} days (dynamic)
- Currency: {Rs. / $ / etc.}
- No emojis unless brand uses them
- Match original card styling exactly

## Every section/snippet must have 100% customizable schema settings.

## Folder Structure
- brand/     — brand-dna.md, brand-voice.md, icp-cards.md
- research/  — all research outputs
- designs/   — HTML prototypes + winning test designs
- assets/    — scraped images, logo, fonts
- theme/     — Shopify theme files

## Research Priority Order
1. /shopify-analytics  → WHERE to focus (data)
2. /visual-audit       → WHAT's broken (screenshots + winning tests)
3. /competitor-audit   → What others do better
4. /review-mining      → Voice of customer
5. /ga-audit           → Deeper traffic analysis
6. /rapid-research     → Deep product analysis
7. /pain-points        → 1,500 identity impacts
8. /fs-test-research   → Complete testing roadmap
```

## Step 6: Confirm Setup

Output:
```
{Brand Name} project set up.

Folder: clients/{slug}/
Brand files: brand-dna.md, brand-voice.md, icp-cards.md ← auto-generated
Images: assets/images/ ← {X} product images scraped
Logo: assets/logo/ ← saved
Shopify CLI: {authenticated / needs auth}

Next step: /shopify-analytics {slug} {start-date} {end-date}
```
