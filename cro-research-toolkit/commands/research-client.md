Run a full brand and competitor research for a new Shopify client.

Client URL: $ARGUMENTS

## Step 1 — Brand Analysis
Fetch the client's website (Firecrawl with `waitFor: 8000`) and extract:
- Brand colors (primary, secondary, accent) — exact hex codes
- Fonts (headline, body) — check Google Fonts or font-family in CSS
- Tone of voice (luxury, fun, clinical, aggressive, minimal, playful, etc.)
- Target customer (who is this for? age, gender, location, lifestyle)
- Top products and their price points (with currency)
- Current CTA language ("Shop Now", "Add to Cart", "Get Yours", etc.)
- Trust signals used (reviews count, badges, guarantees, press mentions, certifications)
- USPs displayed (shipping, quality, ingredients, sourcing, etc.)
- What's missing or weak on the current site

## Step 2 — Scrape Branding Assets
Extract via Firecrawl branding format:
- Logo URL (header logo)
- Favicon
- Button styles (border-radius, colors, hover states)
- Card styles (border-radius, shadows, grid columns)
- Announcement bar (text, background color, style — static or marquee)
- Navigation structure (items, dropdowns, mega menu)

## Step 3 — Competitor Research
Find 3-5 direct competitors (from onboarding form, or search "[product type] [market] shop"). For each:
- Hero headline and CTA strategy
- What CRO elements they use (urgency, social proof, benefit-first copy, bundles, subscriptions)
- Above-the-fold strategy on product pages
- Bundle/pricing strategy (tiers, per-unit pricing, subscription discounts)
- Trust elements (reviews, certifications, guarantees, endorsements)
- What they do BETTER than the client
- What the client does better than them

## Step 3b — Competitor Review Mining (Apify)

For each competitor, scrape their Amazon/external reviews using Apify:
- `apify call apify/amazon-reviews-scraper` with competitor product ASINs
- Extract: top pain points, praise themes, objections, exact customer language
- Focus on 1-3 star reviews for pain points, 4-5 star for what customers love
- This feeds directly into ad script generation

For Reddit/forum discussions about the product category:
- `apify call apify/reddit-scraper` with relevant subreddits (e.g., r/malegrooming, r/AskMenOver30)
- Extract: common questions, frustrations, product recommendations

## Step 3c — Social Media Intelligence (Apify)

Scrape competitor social presence:
- `apify call apify/instagram-scraper` — follower count, top posts, engagement rate, content themes
- `apify call apify/tiktok-scraper` — viral videos about the product category, what hooks work
- Identify which content formats get the most engagement (demo, before/after, UGC, educational)

## Step 4 — Winning Ad Research
Search for "[brand name] ads" or "[product category] advertorial" and identify:
- What angles are working in paid traffic for this niche
- What copy hooks are being used (pain point, transformation, social proof, authority)
- What offers are common (bundles, BOGO, free gifts, subscriptions, first-order discounts)
- Landing page patterns (listicle, advertorial, quiz funnel, direct PDP)

## Step 5 — CRO Recommendations
Based on all research, output:
1. The 3 biggest opportunities on this client's site right now
2. The #1 page to redesign first and why
3. The offer structure that would likely convert best for their audience
4. Bundle strategy recommendation (tiers, pricing, per-unit framing)
5. Design direction: what should the redesign feel like vs current site
6. Quick wins that can be implemented without a full redesign

## Step 6 — Generate Brand Files
Auto-generate these files in `clients/{slug}/brand/`:
- `brand-dna.md` — colors, fonts, logo URL, USPs, button styles, card styles
- `brand-voice.md` — tone, register, CTA language, headline style, cultural context
- `icp-cards.md` — 2-3 ideal customer profiles with demographics, motivations, objections, desires

## Output Format
Write as a structured client research brief — clear sections, data-backed, no fluff. This feeds all downstream design and dev work.

Save to `clients/{slug}/research/brand-research.md`
