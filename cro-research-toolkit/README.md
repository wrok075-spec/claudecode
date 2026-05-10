# CRO Research Toolkit for Claude Code

A complete 7-phase CRO (Conversion Rate Optimization) research workflow for DTC eCommerce brands. Built to run inside [Claude Code](https://claude.ai/claude-code).

## What This Does

Takes a brand URL and runs the entire CRO research pipeline — from brand analysis to live Meta ad campaigns. Each phase builds on the previous one.

| Phase | What Happens | Time |
|-------|-------------|------|
| 1. Brand Foundation | Brand DNA, Shopify audit, GA4 audit | Day 1 |
| 2. Customer Research | Review mining, pain points, Reddit research | Day 1-2 |
| 3. Competitor Intelligence | Competitor audit, Meta Ad Library, social intel | Day 2-3 |
| 4. CRO Audit | Visual audit, Clarity audit, test hypotheses | Day 3-4 |
| 5. Design & Implementation | Design briefs, winning test designs | Day 4-5 |
| 6. Creative Production | Static ads, UGC scripts, landing pages | Day 5-7 |
| 7. Launch & Optimize | Meta campaigns, daily analysis, email reports | Day 7+ |

## Setup

### 1. Install Claude Code
```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Copy commands to your Claude config
```bash
cp -r commands/ ~/.claude/commands/
cp -r skills/ ~/.claude/skills/
```

### 3. Required tools (install as needed)
- **Firecrawl** — connected via MCP in Claude settings ([firecrawl.dev](https://firecrawl.dev))
- **Apify CLI** — `npm install -g apify-cli && apify login` (for review mining, Reddit, social scraping)
- **Playwright** — `npm install -g playwright && npx playwright install` (for screenshots)
- **Shopify CLI** — `npm install -g @shopify/cli` (for store data)
- **Meta API** — add `META_ACCESS_TOKEN` and `META_AD_ACCOUNT_ID` to `.env` in your project

### 4. Optional tools
- **FAL API** — for static ad image generation (`FAL_KEY` in `.env`)
- **Microsoft Clarity** — client provides access for heatmap/session data
- **GA4** — client provides access for funnel analysis

## Usage

### Run the full workflow
```
/cro-research https://example-brand.com
```

### Run individual phases
```
/research-client https://example-brand.com     # Brand DNA
/review-mining https://amazon.com/dp/BXXXXXXX  # Review mining
/competitor-audit https://competitor.com        # Competitor audit
/visual-audit https://example-brand.com         # Visual CRO audit
/meta-campaign-analysis                         # Meta ads analysis
```

### Start a new client
```
/new-client BrandName
```
This creates the folder structure and chains the full CRO workflow.

## Commands Reference

### Research Phase
| Command | Description |
|---------|-------------|
| `/cro-research` | Full 7-phase workflow (runs everything below) |
| `/new-client` | New client onboarding + folder setup |
| `/research-client` | Brand DNA extraction (website, press, social) |
| `/review-mining` | Scrape reviews from Amazon, Trustpilot, Google, Shopify |
| `/pain-points` | Pain point analysis with emotional triggers |
| `/rapid-research` | Quick market research |
| `/competitor-audit` | Competitor analysis with screenshots |
| `/survey-audit` | Post-purchase survey analysis |

### Analytics Phase
| Command | Description |
|---------|-------------|
| `/shopify-analytics` | ShopifyQL revenue, orders, AOV trends |
| `/ga-audit` | GA4 funnel visualization + per-channel breakdown |
| `/fbt-analysis` | Frequently bought together analysis |

### CRO Phase
| Command | Description |
|---------|-------------|
| `/visual-audit` | Screenshot-based CRO audit |
| `/fs-test-research` | A/B test hypothesis generation |
| `/design-brief` | Design brief from research data |
| `/winning-tests-design` | Adapt proven test patterns to brand |

### Creative Phase
| Command | Description |
|---------|-------------|
| `/advertorial` | Build advertorial landing pages |
| `/meta-ads` | Create Meta ad campaigns via API |
| `/meta-campaign-analysis` | Pull live campaign data + analysis |
| `/meta-ads-playbook` | Living knowledge base of Meta ads strategies |

## Key Frameworks

### Profit Per Visitor
```
COGS per unit = $X (get from client)
True Break-even CPA = AOV - COGS
True Break-even ROAS = AOV / (AOV - COGS)
Gross Profit = Revenue - (COGS x Purchases) - Ad Spend
Profit per Visitor = Gross Profit / Landing Page Views
```

### Waterfall Rule (Meta Ads)
Don't kill ad sets based on CPA alone. Check frequency first:
- Frequency < 1.5 = Hunter (top of funnel) — KEEP IT
- Frequency > 2.5 + high CPA = Fatiguing — consider pausing

### Tool Selection
| Tool | Use For |
|------|---------|
| Firecrawl | Website content, brand identity, structured data |
| Apify | Amazon reviews, Reddit, TikTok, Instagram, Google reviews |
| Playwright | Screenshots, scroll-throughs, interactive testing |
| Shopify CLI | Store data, products, orders, analytics |
| Meta API | Ad campaigns, performance data |

## License

Internal use. Not for redistribution.
