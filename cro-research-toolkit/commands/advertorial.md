Build high-converting advertorial/listicle pages for a DTC brand by scraping their website and generating complete, ready-to-deploy HTML pages.

Usage: /advertorial $ARGUMENTS

Arguments: URL of the product/brand website, optionally followed by number of variations (default: 3) and format preference.

Examples:
- `/advertorial https://skynutrition-us.com`
- `/advertorial https://skynutrition-us.com 3`
- `/advertorial https://skynutrition-us.com 2 listicle`
- `/advertorial https://fleava.shop 3 editorial`

## STEP 1: SCRAPE & RESEARCH

Use firecrawl or web scraping tools to extract from the provided URL:
- **Brand name** and product name(s)
- **Price** and pricing tiers (bundles, subscriptions)
- **Product description** and key claims
- **Ingredients / key features** with benefits
- **Reviews** — star rating, review count, actual review text (grab 5-10 real reviews)
- **Product images** — hero images, product shots, lifestyle images (save URLs)
- **Target audience** — infer from copy, imagery, reviews
- **Mechanism / unique angle** — what makes this product different (the "why this works" story)
- **Social proof** — customer count, press mentions, certifications, expert endorsements
- **Guarantee** — money-back guarantee details
- **Shipping info** — free shipping thresholds

Also scrape competitor pages and the brand's Meta ad library to understand positioning.

Present a summary of findings to the user and ask them to confirm or adjust before proceeding.

## STEP 2: CHOOSE FORMAT & STYLE

Ask the user (if not specified in arguments):

**Format** (pick one):
1. **Listicle** — "9 Reasons [Authority] Are [Doing X]..." — Numbered reasons with images, each building the case. Works great for supplements, health, skincare. (Like skynutrition v1)
2. **Editorial / News Exposé** — "REVEALED: [Finding]..." — Investigative reporter tone, urgent, confrontational. Has a masthead, breaking tags, pull quotes. (Like skynutrition v2)
3. **Personal Story** — "I'm [Age]. I [Did Thing]. Here's What Happened." — First-person diary, week-by-week timeline, warm and relatable. (Like skynutrition v3)
4. **All three** — Generate one of each format as variations

**Style Preset** (pick one):
- **A — Clinical Editorial**: White bg, charcoal text, medical blue accents. Serif headlines. Authority = Doctor/specialist. Best for: health, supplements, skincare.
- **B — Lifestyle Magazine**: Off-white bg, warm rose/gold accents. Modern serif headlines. Authority = Editor/journalist. Best for: beauty, fashion, premium goods.
- **C — News Exposé**: White bg, black text, red urgency + yellow highlights. Bold sans-serif. Authority = Investigative journalist. Best for: supplements, weight loss, "hidden truth" angles.
- **D — Warm & Trustworthy**: Warm white bg, forest green accents, brown text. Rounded sans-serif. Authority = Real customer narrator. Best for: pet, family, food, hobby.
- **E — Brand Custom**: Extract the brand's own color palette from their website and build a custom design system around it.

## STEP 3: BUILD ADVERTORIAL PAGES

For each variation, create a complete self-contained `index.html` file following the proven 17-section structure. EVERY section must be fully written — no placeholders.

### The 17-Section Structure (NEVER change order):

1. **URGENCY BANNER** — Sticky top bar. Time-sensitive message. Small text, accent bg.
2. **EDITORIAL HEADLINE** — Must read like a real article headline, NOT an ad. Use proven patterns:
   - Listicle: "[Number] [Audience] Are [Doing Thing] to [Get Result] — [Authority] Says It Works"
   - Exposé: "REVEALED: [Finding] [Number]+ [Audience] Are [Doing] Instead of [Alternative]"
   - Personal: "I'm [Age]. I [Replaced/Switched]. Here's My [Timeframe] [Outcome]."
3. **BYLINE + DATE** — Realistic author with credentials. Recent date. Reading time.
4. **HERO IMAGE** — Full-width product/lifestyle image from scrape or Gemini-generated.
5. **OPENING HOOK** — 2-3 paragraphs. Start with relatable pain point (second person). Build emotional identification. Tease solution without naming product.
6. **STAR RATING INTERRUPTER** — Visual break with stars and review count from scrape.
7. **PAIN POINT ESCALATION** — Checklist format. Make the problem feel urgent and serious.
8. **ROOT CAUSE REFRAME** — "Here's what most people don't realize..." Introduce the mechanism. Position existing solutions as flawed.
9. **PRODUCT REVEAL** — Name the product. Origin story. 3-4 bullet differentiators. Product image.
10. **INGREDIENT / FEATURE CARDS** — 3-5 cards with icons, ingredient names, what they do, clinical proof.
11. **SOCIAL PROOF BLOCK** — 3-4 testimonial cards from real scraped reviews. Include name, rating, story-driven text, "Verified Buyer" badge.
12. **RESULTS TIMELINE** — Week-by-week expected results. Sets expectations and creates anticipation.
13. **COMPARISON TABLE** — "[Product] vs. The Rest" with checkmarks/X marks. Product wins every row.
14. **PACKAGE PRICING / OFFER** — 3-tier pricing from scraped data. Middle option highlighted. Show savings.
15. **GUARANTEE** — Money-back guarantee from scraped data. Shield icon. Risk removal.
16. **FINAL CTA** — Urgency restatement. Large CTA button. Final social proof line.
17. **FOOTER** — FDA/results disclaimers. Policy links. Minimal.

### Technical Requirements:
- Single self-contained `index.html` — ALL CSS inline in `<style>` block
- Google Fonts via `<link>` tags (1 serif + 1 sans-serif, or brand-appropriate)
- Mobile-first responsive design. Max-width 700-760px centered.
- No JavaScript required. Pure HTML + CSS.
- No placeholder text anywhere.
- Star ratings: HTML entities (★☆)
- CTA buttons: accent bg, white text, rounded corners, min 48px height, subtle hover state
- All CTA links point to the product page URL from the scraped website

### Copy Rules (CRITICAL — these separate converting pages from AI slop):
- Write like a journalist, NOT a marketer
- Specific > generic: "47,382 women" beats "thousands of women"
- One idea per paragraph. Short paragraphs. Scannable.
- NEVER use these words: delve, landscape, testament, showcase, foster, underscore, pivotal, crucial, realm, myriad, tapestry, multifaceted, commendable, intricate, comprehensive, game-changer, revolutionize
- No hype adjectives without proof
- Testimonials must sound real: include hesitation, specific details, timeframes
- The mechanism is the star — explain it with analogies, make the reader feel smarter
- Urgency must feel real — tie it to something specific (seasonal sale, production batch, media feature)

## STEP 4: IMAGE GENERATION (if needed)

If the scraped website doesn't have enough high-quality images, generate them using Google Gemini API.

Check for GEMINI_API_KEY in `/Users/eapple/advertorials-youtube/.env`

Create a `generate-images.mjs` script that generates:
1. Hero/Lifestyle Image (16:9)
2. Product Showcase (1:1)
3. Authority Headshot (1:1)
4. 3-5 Ingredient/Feature Visuals (1:1)
5. Before/After Transformation (16:9)

Use the `@google/genai` package with model `gemini-3-pro-image-preview`.

Image prompt guidelines:
- Be specific about lighting, angle, setting
- Match the style preset aesthetic
- Never prompt for text on images
- Product shots: "professional product photography, [product] on [surface], [lighting], editorial style"
- Lifestyle shots: "[person matching target] using [product], [setting], candid editorial photography"

## STEP 5: OUTPUT

Create a project folder structure:
```
/Users/eapple/advertorials-youtube/{brand-name}/
├── v1/
│   ├── index.html        # Variation 1 (e.g., Listicle)
│   └── images/           # Images for v1
├── v2/
│   ├── index.html        # Variation 2 (e.g., News Exposé)
│   └── images/           # Images for v2
├── v3/
│   ├── index.html        # Variation 3 (e.g., Personal Story)
│   └── images/           # Images for v3
├── generate-images.mjs   # Image generation script (if needed)
└── research/
    └── scrape-summary.md  # Research findings from scrape
```

After building, offer to:
- Preview locally or publish via /here-now
- Push to Shopify as draft page templates (using /store-switch to connect to the right store)
- Generate more variations

## EXECUTION DIRECTIVE
"You are not building a landing page. You are writing a magazine article that happens to sell a product. The reader should be 80% through the page before they realize they're being sold to. Every paragraph earns the next scroll."
