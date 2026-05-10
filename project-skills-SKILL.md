# Static Ad System — Full Pipeline

Generate production-ready static ad images for any brand, from research to Meta upload, entirely inside Claude Code.

## Overview

This system has 6 phases. Each can run independently or as a full pipeline:

```
Phase 1: Brand Research → Brand DNA document
Phase 2: Competitor & Review Mining → Pain points + ad scripts
Phase 3: Prompt Generation → Fill templates with brand-specific details
Phase 4: Image Generation → FAL (Nano Banana 2) or OpenAI (GPT Image)
Phase 5: Winner Variation → Generate variations of proven winners
Phase 6: Meta Upload → Upload creatives to ad account + create campaigns
```

## Prerequisites

- `.env` file at project root with:
  ```
  FAL_KEY=your-fal-key
  OPENAI_API_KEY=your-openai-key  # optional, for GPT image generation
  META_ACCESS_TOKEN=your-meta-token
  META_AD_ACCOUNT_ID=act_XXXXXXXX
  ```
- Python packages: `requests`, `openai` (optional)
- Product images in the brand folder before running Phase 4

## Folder Structure

```
~/brands/{brand-name}/
├── product-images/          # Drop product PNGs/JPGs here
│   ├── product-front.png
│   └── ...
├── brand-dna.md             # Phase 1 output
├── competitor-research.md   # Phase 2a output
├── review-mining.md         # Phase 2b output
├── ad-scripts.md            # Phase 2c output
├── prompts.json             # Phase 3 output
├── variation_prompts.json   # Phase 5 output
├── generate_ads.py          # Phase 4 script
└── outputs/                 # Generated images
    ├── 01-headline/
    └── ...

~/all-ads/
├── {product-line}/          # Organized by product
│   ├── 01-headline_v1.png
│   └── ...
└── variations/              # Winner variations
    ├── social-comment/
    ├── proof-grid/
    └── competitor-scripts/
```

---

## Phase 1: Brand Research & DNA Generation

**When to run:** First time working with a new brand.
**Input:** Brand name + URL
**Output:** `brand-dna.md`

Use web search extensively to gather real data:

### Research Steps

1. **EXTERNAL RESEARCH** (web search each):
   - Design credits: "[Brand] design agency", "[Brand] rebrand"
   - Brand assets: "[Brand] brand guidelines pdf", "[Brand] press kit"
   - Typography: "[Brand] font", "[Brand] typeface"
   - Colors: "[Brand] brand colors", "[Brand] hex codes"
   - Packaging: "[Brand] packaging design", "[Brand] unboxing"
   - Advertising: "[Brand] Meta Ad Library" for ad creative styles
   - Positioning: "[Brand] brand story", "[Brand] mission"

2. **ON-SITE ANALYSIS** (fetch and analyze brand URL):
   - Voice/Tone: 5 distinct adjectives from hero copy and product descriptions
   - Photography Style: lighting, color grading, composition
   - Typography: headline weight, body weight, letter-spacing
   - Color application: primary vs accent, background colors, CTA color
   - Packaging details: materials, colors, shape, label placement, textures

3. **COMPETITIVE CONTEXT:**
   - 2-3 direct competitors and visual differentiation

### Output Format

```
BRAND DNA DOCUMENT
==================
BRAND OVERVIEW
Name / Tagline / Voice Adjectives [5] / Positioning

VISUAL SYSTEM
Primary Font / Secondary Font / Colors [hex] / CTA Style

PHOTOGRAPHY DIRECTION
Lighting / Color Grading / Composition / Mood

PRODUCT DETAILS
Physical Description / Label-Logo Placement / Distinctive Features

AD CREATIVE STYLE
Formats / Text overlay style / UGC usage / Offer presentation

IMAGE GENERATION PROMPT MODIFIER
50-75 word paragraph to prepend to any image prompt to match brand identity.
```

Save as: `~/brands/{brand-name}/brand-dna.md`

---

## Phase 2: Competitor & Review Mining → Ad Scripts

**When to run:** After Phase 1, or anytime you need fresh ad angles.
**Input:** Brand DNA + competitor URLs/names
**Output:** `competitor-research.md`, `review-mining.md`, `ad-scripts.md`

This phase has 3 sub-steps. Each produces ad scripts based on real data, not guesswork.

### Phase 2a: Competitor Research

Use `/competitor-audit` or `/meta-ads` skills to analyze:
- What competitors are running on Meta Ad Library
- Their creative formats (image vs video vs carousel)
- Their copy angles (pain, social proof, offer, authority, transformation)
- Their landing page strategy
- Longest-running ads (likely winners)

**Output:** Competitor strengths, weaknesses, and gaps to exploit.

### Phase 2b: Review Mining

Use `/review-mining` skill or manually scrape competitor reviews to extract:
- **Pain points** customers mention repeatedly (staining, ammonia smell, damage, fading)
- **Objections** people raise before buying (does it work? is it safe? will it stain?)
- **Delight moments** customers describe after using (wife noticed, barber asked, feels healthier)
- **Language patterns** — exact words and phrases customers use (not marketing speak)

**Sources to mine:**
- Amazon reviews of competitor products (sort by 1-3 star for pain points, 4-5 star for delight)
- Reddit threads about the product category (r/AskMenOver30, r/malegrooming, etc.)
- TikTok comments on competitor ads
- Trustpilot / product review sites

**Output:** Categorized list of pain points, objections, and delight moments with real customer quotes.

### Phase 2c: Ad Script Generation

Transform review mining data into ad scripts. Each script includes:
- **Primary Text** (the long-form ad copy)
- **Headline** (short, punchy)
- **Description** (one line)
- **CTA Button** (Shop Now, Try Risk-Free, etc.)
- **Image concept** (describes what the static ad should look like)
- **Angle category** (Fear/Education, Competitor Weakness, Value/Math, Social Proof, Authority, Risk Reversal, Unexpected Benefit)

**Recommended ad angles from review mining:**

| Angle | Hook Type | Example |
|-------|-----------|---------|
| Ingredient Exposer | Fear/Education | "Check the label — your dye has PPD" |
| Competitor Weakness | Pain exploitation | "It left my nails stained for a week" |
| Value Bomb | Math/Savings | "2.5x more product for $6 less" |
| Unexpected Benefit | Surprise | "Your hair feels BETTER after coloring" |
| Risk Reversal | Guarantee | "60 days vs 30 from competitors" |
| Skeptic Conversion | Social proof | "47,000 skeptics became believers" |
| Cost Comparison | Math | "Salon $150 vs Kiwinz $29" |
| Authority | Trust | "Barbers recommend it" |

Save scripts as: `~/brands/{brand-name}/ad-scripts.md` or project root `static-ad-scripts.md`

### Phase 2d: Pain Point Analysis (Optional)

Use `/pain-points` skill for deeper psychological analysis:
- Scott Pain Point framework
- Map pain points to ad angles
- Identify emotional triggers (fear, vanity, frustration, embarrassment)
- Rank by intensity and frequency

---

## Phase 3: Prompt Generation

**When to run:** After Phase 1 (and optionally Phase 2).
**Input:** Brand DNA + template library + ad scripts (if available)
**Output:** `prompts.json`

### Template Library

Three template sources are available:

1. **40 Core Templates** (`references/template-prompts.md`) — Standard ad formats:
   - Headline, Offer, Testimonials, Features, Bullet Points, Social Proof
   - Us vs Them, Before/After, Negative Marketing, Press Editorial
   - Pull Quote Review, Lifestyle, Stat Surround, Bundle Showcase
   - Social Comment Screenshot, Curiosity Gap, Verified Review Card
   - And 23 more formats

2. **60 Psychology Templates** (`references/psychology_templates.py`) — Advanced formats:
   - Value Proposition (salon math, cost-per-use, yearly comparison)
   - Social Proof (wife/partner texts, barber shocked, transformation reveal)
   - Proof Grid (grey coverage, hair types, age groups, first wash)
   - Fear/Urgency (ingredient exposer, damage trade-off)
   - Identity (confidence, nostalgia, self-care)
   - Practical (how-it-works, application tutorial, speed comparison)

3. **Ad Script Templates** (from Phase 2c) — Custom angles from competitor research

### Prompt Generation Process

For each template:
1. Prepend the IMAGE GENERATION PROMPT MODIFIER from Brand DNA
2. Replace all `{PLACEHOLDERS}` with brand-specific details
3. Set aspect_ratio (1:1 for feed, 4:5 for more real estate, 9:16 for stories)
4. Mark `needs_product_images: true/false`
5. Include the full product description for bottle/packaging accuracy

Save as: `~/brands/{brand-name}/prompts.json`

---

## Phase 4: Image Generation

**When to run:** After Phase 3.
**Input:** `prompts.json` + product images
**Output:** Generated ad images in `outputs/` or `all-ads/`

### Option A: FAL / Nano Banana 2 (recommended for product shots)

Best for: Photorealistic product imagery, lifestyle shots, before/after grids.

**With product reference images (edit endpoint):**
```python
# Upload product image as base64 data URI
with open("product-images/product.png", "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")
product_uri = f"data:image/png;base64,{b64}"

# Submit to queue
POST https://queue.fal.run/fal-ai/nano-banana-2/edit
Headers: {"Authorization": "Key {FAL_KEY}", "Content-Type": "application/json"}
Body: {
    "prompt": "...",
    "image_urls": [product_uri],
    "aspect_ratio": "1:1",
    "num_images": 1,
    "output_format": "png",
    "resolution": "2K"
}

# Poll for status
GET https://queue.fal.run/fal-ai/nano-banana-2/requests/{request_id}/status

# Get result
GET https://queue.fal.run/fal-ai/nano-banana-2/requests/{request_id}
```

**Without product images (text-to-image):**
```
POST https://queue.fal.run/fal-ai/nano-banana-2
```

**Key settings:**
- Resolution: 2K for production, 1K for test runs
- Cost: ~$0.12/image at 2K
- Use base64 data URI for product images (FAL file upload endpoint can be unreliable)

### Option B: OpenAI / GPT Image (better for text-heavy ads)

Best for: Ads with lots of text overlays, math comparisons, ingredient lists.

```python
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

result = client.images.generate(
    model="gpt-image-1",  # or "dall-e-3" as fallback
    prompt="...",
    n=1,
    size="1024x1024",
    quality="high",
)
```

**When to use which:**
| Use Case | FAL (Nano Banana 2) | OpenAI (GPT Image) |
|----------|--------------------|--------------------|
| Product bottle accuracy | ✓ (with reference image) | ✗ (guesses) |
| Before/after grids | ✓ | ✓ |
| Text-heavy ads | ✗ (text rendering weaker) | ✓ (better text) |
| Social comment mockups | ✓ | ✓ |
| UGC/lifestyle | ✓ | ✓ |
| Cost comparison layouts | ✗ | ✓ |

### Running the Generation Script

```bash
cd ~/brands/{brand-name}
python generate_ads.py                        # All templates
python generate_ads.py --templates 1,7,13,15  # Specific templates
python generate_ads.py --resolution 1K        # Quick test
python generate_ads.py --variations 3         # Multiple versions per template
```

---

## Phase 5: Winner Variation Generation

**When to run:** After running ads for 3-7 days and identifying winners via `/meta-campaign-analysis`.
**Input:** Winning ad formats + Brand DNA + product images
**Output:** Variation images in `all-ads/variations/`

### Process

1. **Identify winners** from Meta campaign data:
   - Ads with ROAS > 1.5x
   - Ads with CPA below target
   - Ads with strong CTR and funnel conversion rates

2. **Categorize the winning FORMAT** (not just the creative):
   - Social Comment Screenshot format (headline + comment card + product)
   - Proof Grid format (headline + 2x2 before/after grid + product)
   - Value Calculator format (headline + math breakdown + savings number + product)
   - Review Card format (quote + stars + review card + product)
   - Us vs Them format (split comparison + product)

3. **Generate variations** using the same format but different:
   - **Copy angles** (different comment text, different math, different review)
   - **Headlines** (different emotional hooks)
   - **Social proof** (different customer names, different scenarios)

4. **Use the same brand preamble** from prompts.json to keep product/brand consistency

5. **Save variation prompts** as `variation_prompts.json` for reproducibility

### Example: Social Comment Variations

Keep the format (headline + comment card + product + stars), vary the story:
- Wife/partner reaction ("she said I look different")
- Coworker compliment ("you look refreshed")
- Barber shocked ("who did your color?")
- Dating confidence ("likes doubled")

### Example: Proof Grid Variations

Keep the format (headline + 2x2 grid + product), vary the angle:
- Grey coverage levels (25%, 50%, 75%, 100%)
- Hair types (thick, thin, curly, straight)
- Beard + hair (beard only, hair only, both, patchy)
- First wash results (instant, not week 3)
- Age groups (35, 45, 55, 65)

---

## Phase 6: Meta Upload & Campaign Creation

**When to run:** After generating images.
**Input:** Generated images + Meta API credentials from `.env`
**Output:** Live ads in Meta Ads Manager

### Upload Images

```python
# Upload image to Meta ad account
POST https://graph.facebook.com/v21.0/{ad_account_id}/adimages
Form data: filename=@image.png, access_token=TOKEN

# Returns: {"images": {"image.png": {"hash": "abc123..."}}}
```

### Campaign Structure

Two campaign types:

**Testing Campaign** ($40-100/day CBO):
- Purpose: Test new creatives cheaply
- 1 ad per ad set (or dynamic creative with multiple images)
- Same targeting across all ad sets
- Optimize for purchases
- Kill rule: pause at 2x target CPA with zero purchases

**Scaling Campaign** ($120+/day CBO):
- Purpose: Spend on proven winners
- Only ads with 5+ purchases at 1x+ ROAS
- Increase budget 20% every 3 days max

### Creating Ads via API

```python
# 1. Create campaign
POST /{account}/campaigns
  name, objective=OUTCOME_SALES, daily_budget (in cents), 
  buying_type=AUCTION, bid_strategy=LOWEST_COST_WITHOUT_CAP, status=PAUSED

# 2. Create ad set (dynamic creative for multi-image testing)
POST /{account}/adsets
  name, campaign_id, optimization_goal=OFFSITE_CONVERSIONS,
  billing_event=IMPRESSIONS, is_dynamic_creative=true,
  targeting={age_min, age_max, genders, geo_locations, publisher_platforms},
  promoted_object={pixel_id, custom_event_type=PURCHASE},
  attribution_spec=[{event_type=CLICK_THROUGH, window_days=7}]

# 3. Create ad creative (dynamic creative with multiple images)
POST /{account}/adcreatives
  name, object_story_spec={page_id},
  asset_feed_spec={
    images: [{hash: "..."}, ...],        # Multiple images
    bodies: [{text: "..."}, ...],         # Multiple body texts
    titles: [{text: "..."}, ...],         # Multiple headlines
    descriptions: [{text: "..."}, ...],   # Multiple descriptions
    call_to_action_types: ["SHOP_NOW"],
    link_urls: [{website_url: "...", display_url: "..."}],
    ad_formats: ["SINGLE_IMAGE"],
    optimization_type: "REGULAR"
  }

# 4. Create ad
POST /{account}/ads
  name, adset_id, creative={creative_id}, status=ACTIVE
```

### Landing Page A/B Testing

Create duplicate ad sets with the same creatives but different landing page URLs:
- Ad Set 1: Creatives → Landing Page A (e.g., `/pages/reverse-grey`)
- Ad Set 2: Same Creatives → Landing Page B (e.g., `/pages/salt-pepper`)

Meta's CBO will allocate budget to whichever LP converts better.

### Important API Notes

- Daily budgets are in **cents** (e.g., `4000` = $40/day)
- `spend` and `action_values` in insights are in **dollars**
- Ad sets with `is_dynamic_creative=true` must be created with this flag — it can't be added later
- Use `LOWEST_COST_WITHOUT_CAP` bid strategy at campaign level for CBO
- Page ID is required in `object_story_spec`
- Pixel ID is required in `promoted_object`

---

## Full Pipeline: New Client Checklist

Run these in order for a new client:

### Research Phase
- [ ] `/research-client` — Full brand and competitor research
- [ ] Phase 1: Brand DNA generation (from research)
- [ ] `/review-mining` — Mine competitor Amazon/Trustpilot reviews
- [ ] `/pain-points` — Scott Pain Point Analysis on target market
- [ ] `/meta-ads` — Meta Ad Library analysis (client + competitors)
- [ ] `/competitor-audit` — Full competitor analysis with screenshots
- [ ] `/rapid-research` — Deep product and customer analysis

### Creative Phase
- [ ] Phase 2c: Generate ad scripts from review mining data
- [ ] Phase 3: Generate prompts from templates + scripts
- [ ] Phase 4: Generate images (FAL for product shots, OpenAI for text-heavy)
- [ ] Review and pick best images

### Launch Phase
- [ ] Phase 6: Upload to Meta, create Testing campaign
- [ ] Set up landing page A/B test (if multiple LPs exist)
- [ ] `/meta-campaign-analysis` — Monitor daily

### Optimization Phase (Day 3-7)
- [ ] `/meta-campaign-analysis` — Identify winners and losers
- [ ] Pause ads at 2x CPA with zero purchases
- [ ] Phase 5: Generate variations of winning formats
- [ ] Upload variations to Testing campaign
- [ ] Move proven winners (5+ purchases, 1x+ ROAS) to Scaling campaign

### Ongoing
- [ ] Daily email report via scheduled agent
- [ ] `/meta-campaign-analysis` weekly deep dive
- [ ] Generate new creative batches every 2-3 weeks to fight fatigue
- [ ] Test new landing pages with winning creatives

---

## Additional Research Skills Available

| Skill | What It Does | When to Use |
|-------|-------------|-------------|
| `/research-client` | Full brand + competitor research | New client onboarding |
| `/review-mining` | Extract pain points from reviews | Before writing ad scripts |
| `/pain-points` | Scott Pain Point Analysis | Deep psychological mapping |
| `/meta-ads` | Meta Ad Library scraping + analysis | Competitor ad intelligence |
| `/competitor-audit` | Full competitor analysis with screenshots | Competitive positioning |
| `/rapid-research` | Deep product + customer analysis | Quick market understanding |
| `/visual-audit` | CRO audit with Playwright screenshots | Landing page optimization |
| `/fs-test-research` | Full-Stack CRO test research | A/B test hypothesis generation |
| `/ga-audit` | Google Analytics CRO audit | Funnel leak identification |
| `/clarity-audit` | Microsoft Clarity heatmap analysis | UX/behavior analysis |
| `/design-brief` | Design brief from GA + brand research | Creative direction alignment |
| `/meta-campaign-analysis` | Live Meta Ads API campaign analysis | Daily performance tracking |
| `/shopify-analytics` | ShopifyQL analytics report | Store-level metrics |
| `/fbt-analysis` | Frequently Bought Together analysis | Bundle strategy + AOV |
| `/advertorial` | Build advertorial landing pages | Landing page creation |
| `/listicle` | Build listicle landing pages | Landing page creation |

---

## Research Tool Selection Guide

Three scraping/research tools are available. Use the right one for each job:

### Apify (CLI: `apify call <actor>`)
**Best for:** Structured data extraction from major platforms. Returns clean JSON.
- Amazon reviews: `apify/amazon-reviews-scraper` — pass product ASINs, get ratings, text, dates, verified status
- Google Maps reviews: `apify/google-maps-reviews-scraper`
- Trustpilot reviews: `apify/trustpilot-reviews-scraper`
- Reddit threads: `apify/reddit-scraper` — product category discussions, pain points
- Instagram profiles: `apify/instagram-scraper` — follower count, posts, engagement
- TikTok profiles/videos: `apify/tiktok-scraper` — viral content about product category
- Facebook Pages: `apify/facebook-pages-scraper`
- Google Search: `apify/google-search-scraper`
- Any website: `apify/web-scraper` — custom page function for complex scraping
- **Auth:** Already logged in via `apify login`. Token at `~/.apify/auth.json`
- **Usage:** `apify call <actor-name> --input='{"startUrls":[{"url":"..."}]}'`

### Firecrawl (MCP tool: `mcp__claude_ai_firecrawl__firecrawl_scrape`)
**Best for:** Shopify stores, landing pages, structured content extraction.
- Homepage/PDP content extraction (JSON mode with schema)
- Brand identity extraction (branding mode)
- Review widgets on Shopify (with `waitFor: 8000` for JS rendering)
- Landing page copy/structure analysis
- **Faster than Apify for single-page extractions**
- **Use JSON format** when extracting specific data points (prices, reviews, features)
- **Use markdown format** when you need full page content

### Playwright (via Bash: `npx playwright`)
**Best for:** Screenshots, JavaScript-heavy pages, interactive elements.
- Mobile + desktop full-page screenshots at exact viewports
- Scroll-through section-by-section screenshots
- Cart drawer testing (add to cart → screenshot)
- Mega menu / navigation interaction screenshots
- Pages that need clicking/scrolling to reveal content
- Meta Ad Library scraping (with locale/timezone settings)

### When to Use What

| Research Task | Primary Tool | Fallback |
|---|---|---|
| Competitor Amazon reviews | **Apify** | Firecrawl |
| Competitor website content | **Firecrawl** | Apify web-scraper |
| Reddit/forum discussions | **Apify** | WebSearch |
| TikTok/Instagram intelligence | **Apify** | Manual |
| Mobile/desktop screenshots | **Playwright** | Firecrawl screenshot |
| Review widgets on Shopify | **Firecrawl** (waitFor) | Playwright |
| Meta Ad Library | **Playwright** | Firecrawl |
| Landing page copy extraction | **Firecrawl** (JSON) | Apify |
| Google search for competitors | **Apify** | WebSearch |
| Brand identity (colors/fonts) | **Firecrawl** (branding) | Playwright |

---

## Key Technical Notes

1. **Product images are critical.** The more reference images (front, back, angled), the better FAL matches the real product. 1-3 images is the sweet spot.

2. **FAL edit endpoint** uses `image_urls` with base64 data URIs. The file upload endpoint (`fal.run/fal-ai/file-storage/upload`) is unreliable — use base64 directly.

3. **Aspect ratios:** 1:1 for feed, 4:5 for feed (more real estate), 9:16 for stories/reels.

4. **Resolution:** 2K for production, 1K for test runs. Cost: ~$0.12/image at 2K.

5. **Dynamic creative** on Meta lets you put multiple images + copy variants in one ad set. Meta automatically tests combinations.

6. **Winner variation strategy:** Don't just create random new ads. Identify the winning FORMAT (layout + structure), then create variations with different copy/angles in that same format.

7. **Ad copy from review mining** outperforms generic marketing copy because it uses real customer language and addresses real objections.

8. **Landing page A/B testing** should always run alongside creative testing. Same creative, different LP = isolates the LP variable.

9. **Budget allocation:** Testing at $40-100/day, Scaling at $120+/day. Never increase more than 20-25% every 3 days.

10. **Kill rules:** Pause any ad at 2x target CPA with zero purchases. Promote any ad with 5+ purchases at 1x+ ROAS to scaling.
