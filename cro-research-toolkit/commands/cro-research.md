Run the complete CRO research workflow for a client. Executes all research phases in the optimal order, using the right tool for each job.

Client URL or brand name: $ARGUMENTS

## Tool Selection

| Tool | Best For | Auth |
|------|----------|------|
| **Firecrawl** (MCP) | Shopify page content, brand identity, structured data extraction | Connected via MCP |
| **Apify** (CLI) | Amazon reviews, Reddit, TikTok, Instagram, Google Maps reviews | `~/.apify/auth.json` |
| **Playwright** (Bash) | Screenshots, scroll-through, interactive elements, Meta Ad Library | Local install |
| **Shopify CLI** | Store data, products, orders, analytics | `shopify store auth` |
| **Meta API** | Ad campaign performance, ad library | `.env` META_ACCESS_TOKEN |
| **WebSearch** | General research, competitor discovery, press mentions | Built-in |

## Phase 1: Brand Foundation (Day 1)

### 1a. Brand DNA — `/research-client`
**Tool:** Firecrawl (branding + JSON modes) + WebSearch
- Scrape client website for colors, fonts, tone, USPs, trust signals
- Web search for brand guidelines, press mentions, founding story
- Extract product catalog with pricing
- Output: `brand-dna.md`

### 1b. Shopify Store Audit
**Tool:** Shopify CLI + Shopify Admin GraphQL
- `/shopify-analytics` — ShopifyQL revenue, orders, AOV trends
- `/shopify-admin-skills:shopify-admin-top-product-performance` — best/worst products
- `/shopify-admin-skills:shopify-admin-average-order-value-trends` — AOV by period
- `/shopify-admin-skills:shopify-admin-checkout-abandonment-report` — where people drop off
- `/shopify-admin-skills:shopify-admin-repeat-purchase-rate` — how many come back
- Output: Store performance baseline with key metrics

### 1c. Google Analytics Audit — `/ga-audit`
**Tool:** GA4 API or client-provided access
- Full funnel visualization (session → product view → ATC → checkout → purchase)
- Per-channel breakdown (Meta, Google, Direct, Organic)
- Per-device breakdown (mobile vs desktop)
- Per-resolution breakdown (identifies layout issues)
- Output: Funnel leak identification + dollar impact estimates

---

## Phase 2: Customer Research (Day 1-2)

### 2a. Review Mining — `/review-mining`
**Tool:** Apify (primary) + Firecrawl (fallback)

**Client's own reviews:**
- Firecrawl scrape product pages with `waitFor: 8000` for JS review widgets
- Extract: rating, text, date, reviewer name, verified status

**Competitor Amazon reviews:**
- `apify call apify/amazon-reviews-scraper --input='{"productUrls":["COMPETITOR_ASIN_URL"],"maxReviews":200}'`
- Sort 1-3 star for pain points, 4-5 star for delight moments
- Extract exact customer language — this is ad copy gold

**Trustpilot/Google reviews:**
- `apify call apify/trustpilot-reviews-scraper` for competitor Trustpilot
- `apify call apify/google-maps-reviews-scraper` for local/physical competitors

**Output:** 10-section review mining report with exact customer quotes, pain points, objections, delight moments, VOC language patterns

### 2b. Pain Point Analysis — `/pain-points`
**Tool:** Analysis of review mining data + WebSearch
- Scott Pain Point framework applied to target market
- Map pain points to emotional triggers (fear, vanity, frustration, embarrassment)
- Rank by intensity and frequency
- Connect to ad angles
- Output: Pain point matrix with ad angle recommendations

### 2c. Reddit & Forum Research
**Tool:** Apify
- `apify call apify/reddit-scraper --input='{"startUrls":[{"url":"https://www.reddit.com/r/RELEVANT_SUBREDDIT/search?q=PRODUCT_CATEGORY"}],"maxItems":100}'`
- Relevant subreddits by category:
  - Hair care: r/malegrooming, r/AskMenOver30, r/HaircareScience
  - Supplements: r/Supplements, r/Nootropics, r/Fitness
  - Skincare: r/SkincareAddiction, r/30PlusSkinCare
  - General: r/BuyItForLife, r/InternetParents
- Extract: questions people ask, frustrations, product recommendations, objection patterns
- Output: Reddit insights report with verbatim quotes

### 2d. Rapid Research — `/rapid-research`
**Tool:** WebSearch + Firecrawl
- Deep product and customer analysis
- Market size and growth trends
- Customer acquisition channels
- Pricing comparison across market
- Output: Market research document

---

## Phase 3: Competitor Intelligence (Day 2-3)

### 3a. Competitor Audit — `/competitor-audit`
**Tool:** Firecrawl (content) + Playwright (screenshots) + Apify (reviews/social)

**Content extraction (Firecrawl JSON mode):**
- Homepage: hero, USPs, trust signals, pricing, offers
- PDP: bundle tiers, subscription, reviews count, CTA strategy
- Run all competitors in parallel

**Screenshots (Playwright):**
- Mobile (390x844): homepage scroll, PDP scroll, cart drawer, mobile menu
- Desktop (1440x900): homepage, PDP, mega menus, cart
- Set `locale: 'en-US'`, `timezoneId: 'America/New_York'`

**Competitor reviews (Apify):**
- Amazon reviews for each competitor product
- Instagram/TikTok follower counts and engagement

**Output:** Side-by-side competitor comparison with screenshots, strengths/weaknesses, opportunities

### 3b. Meta Ad Library Analysis — `/meta-ads`
**Tool:** Playwright + Firecrawl
- Scrape Meta Ad Library for client + 2-3 competitors
- Extract: creative format split, copy angles, landing page strategy, CTA analysis
- Identify longest-running ads (likely winners)
- Flag recently launched ads (testing phase)
- Cross-reference with CRO research
- Output: Ad strategy report with winning patterns

### 3c. Social Media Intelligence
**Tool:** Apify
- `apify call apify/instagram-scraper` — competitor profiles, top posts, engagement
- `apify call apify/tiktok-scraper` — viral videos in the product category
- Identify: content formats that get engagement, hooks that work, UGC patterns
- Output: Social intel report

### 3d. Competitor Ad Scripts
**Tool:** Analysis of review mining + competitor audit data
- Transform competitor weaknesses into ad angles
- Map review pain points to ad scripts
- Generate 8-10 ad scripts with:
  - Primary text, headline, description, CTA
  - Image concept description
  - Angle category (fear, value, social proof, authority, etc.)
- Output: `static-ad-scripts.md`

---

## Phase 4: CRO Audit (Day 3-4)

### 4a. Visual CRO Audit — `/visual-audit`
**Tool:** Playwright + winning test database
- Full scroll-through screenshots of client's site (mobile + desktop)
- Compare against proven CRO patterns from winning test database
- Identify: missing trust signals, weak CTAs, poor hierarchy, friction points
- Output: Visual audit with annotated screenshots + test recommendations

### 4b. Microsoft Clarity Audit — `/clarity-audit`
**Tool:** Clarity dashboard access (client provides)
- Heatmap analysis: where people click, how far they scroll
- Session recordings: watch real users navigate
- Rage clicks, dead clicks, quick-backs
- Funnel drop-off visualization
- Output: UX issues report with session recording evidence

### 4c. Full-Stack Test Research — `/fs-test-research`
**Tool:** Analysis of all previous research
- Synthesize findings from GA audit, visual audit, competitor audit, review mining
- Generate A/B test hypotheses ranked by impact
- Each hypothesis includes: what to change, why, expected impact, confidence level
- Output: Prioritized test roadmap

---

## Phase 5: Design & Implementation (Day 4-5)

### 5a. Design Brief — `/design-brief`
**Tool:** Compilation of GA data + brand research
- Combine brand DNA, GA insights, competitor patterns
- Specify: hero section design, PDP layout, bundle selector, cart drawer
- Include wireframes from winning test database
- Output: Design brief for implementation

### 5b. Winning Tests Design — `/winning-tests-design`
**Tool:** Winning test database + brand guidelines
- Adapt proven A/B test patterns to client's brand
- Design test variants with brand colors, fonts, imagery
- Include HTML/CSS mockups where possible
- Output: Ready-to-implement test designs

---

## Phase 6: Creative Production (Day 5-7)

### 6a. Static Ad Generation
**Tool:** FAL (Nano Banana 2) or OpenAI (GPT Image)
- Generate images from ad scripts (Phase 3d)
- Use product reference images with FAL edit endpoint
- FAL for product shots, OpenAI for text-heavy ads
- Output: 20-40 static ad images

### 6b. UGC Video Scripts — `/ugc-prompt-builder`
**Tool:** Seedance 2.0 prompts + ChatGPT Images for creators
- Generate creator character prompts
- Write scene-by-scene video scripts
- Match format to winning angles (demo, problem-solution, testimonial)
- Output: 6+ video scripts ready for production

### 6c. Landing Page / Advertorial — `/advertorial` or `/listicle`
**Tool:** Shopify Liquid theme development
- Build dedicated landing pages for ad traffic
- Listicle format for educational/authority angles
- Advertorial format for native/editorial angles
- Output: Published landing pages on Shopify

---

## Phase 7: Launch & Optimize (Day 7+)

### 7a. Meta Campaign Setup
**Tool:** Meta Marketing API via curl
- Upload creatives to ad account
- Create campaign structure:
  - Cost Cap CBO for scaling (proven creatives)
  - Lowest Cost CBO for testing (new creatives)
- Set up LP A/B tests (same creatives, different landing pages)
- Output: Live Meta campaigns

### 7b. Daily Campaign Analysis — `/meta-campaign-analysis`
**Tool:** Meta Marketing API
- Pull performance data daily
- Track: ROAS, CPA, AOV, frequency, profit per visitor
- Waterfall rule: don't kill low-frequency hunters
- 7-day click attribution check
- Output: Daily performance report with actions

### 7c. Automated Daily Email Report
**Tool:** Scheduled remote agent + Gmail MCP
- Set up via `/schedule` skill
- Runs daily at 9am, emails performance summary
- Includes: yesterday snapshot, 7-day trend, ad-level winners/losers, action items

---

## Full Research Checklist

### Research Phase
- [ ] Brand DNA (`/research-client`)
- [ ] Shopify analytics (`/shopify-analytics`)
- [ ] GA4 audit (`/ga-audit`)
- [ ] Review mining — client reviews (`/review-mining`)
- [ ] Review mining — competitor Amazon reviews (Apify)
- [ ] Reddit/forum research (Apify)
- [ ] Pain point analysis (`/pain-points`)
- [ ] Rapid research (`/rapid-research`)
- [ ] Competitor audit with screenshots (`/competitor-audit`)
- [ ] Meta Ad Library analysis (`/meta-ads`)
- [ ] Social media intelligence (Apify)
- [ ] Competitor ad scripts generation

### CRO Audit Phase
- [ ] Visual CRO audit (`/visual-audit`)
- [ ] Clarity audit (`/clarity-audit`) — if access provided
- [ ] Full-stack test research (`/fs-test-research`)
- [ ] Design brief (`/design-brief`)
- [ ] Winning tests design (`/winning-tests-design`)

### Creative Phase
- [ ] Static ad generation (FAL/OpenAI)
- [ ] UGC video scripts (`/ugc-prompt-builder`)
- [ ] Landing pages (`/advertorial` or `/listicle`)
- [ ] Ad copy from review mining data

### Launch Phase
- [ ] Meta campaign creation (Cost Cap + Testing)
- [ ] LP A/B test setup
- [ ] Daily analysis (`/meta-campaign-analysis`)
- [ ] Automated email reports (`/schedule`)

### Optimization Phase (Ongoing)
- [ ] Kill/scale based on frequency + CPA (waterfall rule)
- [ ] Winner variation generation (same format, new hooks)
- [ ] Hook iteration on top spender
- [ ] AOV optimization (bundles, shipping threshold, subscription)
- [ ] Subscription setup and monitoring
- [ ] Checkout abandonment flows (email/SMS)
- [ ] New creative batches every 2-3 weeks

---

## Profit Per Visitor Framework

Track this for every client:

```
COGS per unit = $X (get from client)
True Break-even CPA = AOV - COGS
True Break-even ROAS = AOV / (AOV - COGS)
Gross Profit = Revenue - (COGS × Purchases) - Ad Spend
Profit per Visitor = Gross Profit / Landing Page Views
```

A negative profit per visitor means losing money even if ROAS looks "good."

The two levers:
1. **Lower CPA** → better creatives, cost cap discipline
2. **Higher AOV** → bundles, shipping threshold, subscription

With subscription:
- LTV matters more than first-purchase profit
- Can afford higher CPA if subscriber rate is >15%
- Track: subscriber rate, churn rate, 3-month LTV, 6-month LTV

---

## Rules

- Use Apify for external platform scraping (Amazon, Reddit, TikTok, Instagram)
- Use Firecrawl for Shopify/website content extraction
- Use Playwright for screenshots and interactive page testing
- Never fabricate data — only report what tools return
- Use exact customer quotes from reviews, never paraphrase
- Every recommendation must tie back to data from research
- Execute actions immediately — don't ask for confirmation
- Track profit per visitor, not just ROAS
