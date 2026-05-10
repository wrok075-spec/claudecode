Run a review mining analysis for a client.

Input (JudgeMe CSV path, PDF path, or product URL to scrape): $ARGUMENTS

## Sourcing Reviews (check in order)
1. **JudgeMe CSV export** — client provides from JudgeMe dashboard (most complete: name, rating, text, date, product, photos, location)
2. **PDF export** — from any review platform (JudgeMe, Yotpo, Loox, etc.)
3. **Apify scrape (PREFERRED for Amazon/external reviews)** — use Apify actors for structured review data:
   - Amazon reviews: `apify/amazon-reviews-scraper` — pass product ASIN, returns structured review data (rating, text, date, verified, helpful votes)
   - Google Maps reviews: `apify/google-maps-reviews-scraper`
   - Trustpilot: `apify/trustpilot-reviews-scraper`
   - Yelp: `apify/yelp-scraper`
   - Any website: `apify/web-scraper` with custom page function
   - Run via CLI: `apify call <actor-name> --input='{"productUrls":["..."]}'` or via API
   - Apify returns clean JSON — no parsing needed
4. **Firecrawl scrape** — scrape product pages with `waitFor: 8000` to let review widgets load, extract via JSON schema. Best for Shopify review widgets (JudgeMe, Loox, Yotpo) on client's own site.
5. **Playwright scrape** — for JavaScript-heavy review sections that Firecrawl can't handle. Use `page.evaluate()` to extract review data after scrolling.

## 10 Sections to Cover

### 1. Review Volume and Rating Distribution
Total reviews, star breakdown (5/4/3/2/1 count and %), average rating, verified purchase rate.

### 2. Product-Level Breakdown
Reviews per product, average rating per product. Which products get the most love/hate?

### 3. Positive Sentiment Themes
Top 5-6 recurring praise themes with **exact customer quotes**. What words do happy customers use over and over?

### 4. Negative/Constructive Themes
Top 5-6 complaints with **exact quotes** (quantity issues, taste/quality, delivery delays, packaging, price concerns).

### 5. Reviewer Demographics
Top cities from location field, geographic spread. Where are the customers?

### 6. Photo Reviews
Count, photo rate, which products get the most photos. These are the most Instagrammable products.

### 7. Voice of Customer Language
Roman Urdu phrases, religious expressions ("MashaAllah", "Alhamdulillah"), emotional language, slang. This is ad-copy gold.

### 8. Repeat Buyer Signals
Reviewers mentioning multiple orders, loyalty language ("ordering again", "third time", "always buy from here").

### 9. Objection Patterns
Purchase barriers surfaced in reviews — what almost stopped them from buying? What do negative reviewers complain about?

### 10. Review Response Rate
How many reviews got a brand reply? (Usually 0% — flag this as a quick win.)

## Additional Extractions
- Top 5-star reviews with short punchy text (for slider cards on PDP/collection)
- Reviews with customer photos (for social proof sections)
- Reviewer name + city for attribution
- Common praise themes → USP copy
- Complaint themes → objection-busting copy
- Overall rating + total review count per product

## Output
- Create Notion research page: "Review Mining Research - {Client}" with full content
- Generate 8-10 insights in Notion Insights database
- Save to `clients/{slug}/research/review-mining.md`

## Rules
- DO NOT mention the review platform name (JudgeMe, Yotpo, etc.) in the output
- Use actual customer quotes, never paraphrase
- Adapt demographic/cultural analysis to the actual market (Pakistani, US, UK, etc.)
