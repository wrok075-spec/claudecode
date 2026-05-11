Set up a new Shopify client project from scratch.

Client URL or brand name: $ARGUMENTS

## Step 1: Collect Client Info

If not provided in $ARGUMENTS, ask for:
- Client/brand name
- Store URL (e.g. storename.myshopify.com)
- Is this a new build (Type A) or optimization client (Type B)?
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
- Client type: {Type A (new build) / Type B (optimization)}
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

## Step 6: Run Full Research Workflow

After folder setup and brand scrape, execute the full `/cro-research` workflow automatically. Don't stop at brand DNA — run everything:

### Research Phase (execute in this order):

**1. Store Data (Shopify CLI)**
- `/shopify-analytics` — revenue, orders, AOV, conversion rate trends
- `/shopify-admin-skills:shopify-admin-top-product-performance` — best/worst products
- `/shopify-admin-skills:shopify-admin-average-order-value-trends` — AOV trends
- `/shopify-admin-skills:shopify-admin-checkout-abandonment-report` — checkout drop-off
- `/shopify-admin-skills:shopify-admin-repeat-purchase-rate` — retention rate
- Get COGS per unit from client → calculate true break-even CPA/ROAS

**2. Customer Research (Apify + Firecrawl)**
- `/review-mining` — client reviews (Firecrawl) + competitor Amazon reviews (Apify)
- Reddit/forum scrape (Apify) — pain points, questions, language patterns
- `/pain-points` — Scott Pain Point framework, emotional triggers
- `/rapid-research` — deep product + market analysis

**3. Competitor Intelligence (Firecrawl + Playwright + Apify)**
- `/competitor-audit` — website scrape + mobile/desktop screenshots
- `/meta-ads` — Meta Ad Library analysis for client + competitors
- Social media intelligence (Apify) — TikTok/Instagram content analysis
- Generate competitor ad scripts from review mining data

**4. CRO Audit (Playwright + GA4)**
- `/visual-audit` — full scroll-through screenshots vs winning test patterns
- `/ga-audit` — GA4 funnel analysis (if access provided)
- `/clarity-audit` — heatmaps + session recordings (if access provided)
- `/fs-test-research` — synthesize everything into prioritized test roadmap

**5. Design & Creative**
- `/design-brief` — combine GA + brand research into design direction
- `/winning-tests-design` — adapt proven patterns to client's brand
- Static ad generation (FAL/OpenAI) from ad scripts
- `/ugc-prompt-builder` — UGC video scripts if video ads needed
- Landing pages (`/advertorial` or `/listicle`) for ad traffic

**6. Launch**
- Upload creatives to Meta via API
- Create Cost Cap CBO (scaling) + Lowest Cost CBO (testing)
- Set up LP A/B tests
- Set up daily email report via `/schedule`
- `/meta-campaign-analysis` for ongoing optimization

### Key Data to Collect from Client

Before starting, get these from the client (don't proceed without them):
- Store URL (myshopify.com domain)
- COGS per unit (for profit per visitor calculations)
- Current monthly revenue and ad spend
- GA4 access (property ID or viewer access)
- Clarity access (if available)
- Competitor URLs (or we find them)
- Target market/country
- Current pain points ("what's not working?")

## Step 7: Confirm Setup

Output:
```
{Brand Name} project set up. Full research initiated.

Folder: clients/{slug}/
Brand files: brand-dna.md, brand-voice.md, icp-cards.md ← auto-generated
Images: assets/images/ ← {X} product images scraped
Logo: assets/logo/ ← saved
Shopify CLI: {authenticated / needs auth}

Research running:
✓ Brand DNA complete
→ Shopify analytics next
→ Then review mining, competitor audit, visual audit...
→ Full workflow: /cro-research
```
