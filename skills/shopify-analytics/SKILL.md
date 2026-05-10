---
name: shopify-analytics
description: Run a full Shopify analytics report using ShopifyQL.
---

Run a full Shopify analytics report using ShopifyQL.

Store slug and date range (e.g., "tongue-tang 2026-01-01 2026-04-22"): $ARGUMENTS

## Pre-requisite
Shopify CLI must be authenticated with `read_reports` scope:
```
shopify store auth --store {store-id}.myshopify.com --scopes read_orders,read_products,read_customers,read_inventory,read_reports
```

## ShopifyQL Syntax Rules (CRITICAL)
- No `sum()` function — use bare column names: `SHOW total_sales, orders`
- No aliases matching existing column names (no `AS total_sales`)
- Response uses `tableData.rows` (not `rowData`)
- For aggregates without GROUP BY, data comes as a single row dict
- Use `FROM sales` for revenue data, `FROM sessions` for traffic/device data
- Date format: `SINCE 2026-01-23 UNTIL 2026-04-22`
- The `sessions` table does NOT support: `billing_country`, `customer_type`, `new_vs_returning`, `visitor_type`, or any country/customer segmentation — those dimensions only exist in `sales`
- The `sessions` table does NOT have a `shipping` column — calculate shipping as `total_sales - net_sales - taxes`
- `conversion_rate` returns a decimal (0.0107 = 1.07%) — multiply by 100 for display

## ShopifyQL Queries to Run

```
Sales overview: FROM sales SHOW total_sales, net_sales, gross_sales, orders, discounts, returns, shipping_charges, taxes, average_order_value, returning_customer_rate SINCE {start} UNTIL {end}

Products: FROM sales SHOW total_sales, net_items_sold GROUP BY product_title SINCE {start} UNTIL {end} ORDER BY total_sales DESC

Returns by product: FROM sales SHOW total_sales, orders, returns GROUP BY product_title SINCE {start} UNTIL {end} ORDER BY total_sales DESC

Countries: FROM sales SHOW orders AS order_count, net_sales, gross_sales, total_sales, discounts, taxes GROUP BY billing_country SINCE {start} UNTIL {end} ORDER BY net_sales DESC LIMIT 15

Discounts by code: FROM sales SHOW orders AS order_count, discounts AS discount_total, net_sales, gross_sales GROUP BY discount_code SINCE {start} UNTIL {end} ORDER BY discount_total ASC LIMIT 50

Device funnel: FROM sessions SHOW sessions, conversion_rate, added_to_cart_rate, reached_checkout_rate, bounce_rate GROUP BY session_device_type SINCE {start} UNTIL {end}

Landing page funnel: FROM sessions SHOW sessions, conversion_rate, added_to_cart_rate, reached_checkout_rate, bounce_rate GROUP BY landing_page_path SINCE {start} UNTIL {end} ORDER BY sessions DESC

Referrer funnel: FROM sessions SHOW sessions, conversion_rate, added_to_cart_rate, reached_checkout_rate, bounce_rate GROUP BY referrer_source SINCE {start} UNTIL {end} ORDER BY sessions DESC

Overall funnel: FROM sessions SHOW sessions, conversion_rate, added_to_cart_rate, reached_checkout_rate, bounce_rate SINCE {start} UNTIL {end}
```

## Data Consistency Rule (CRITICAL)
All numbers in the report MUST come from the SAME set of queries. Never mix data from different query runs or time ranges. Specifically:
- The "Order Profitability" table sets the canonical numbers for total orders, gross sales, discounts, net sales
- The "Discount Deep-Dive" MUST use the same total discount number from the profitability table
- Calculate: Auto discounts = Total discounts (from profitability) - Code discounts (from discount_code query)
- Calculate: Full-price orders = Total orders (from profitability) - Code orders (from discount_code query)
- If numbers don't add up perfectly, adjust the derived values to match the profitability totals — NEVER show conflicting totals in different tables
- Run all queries in one batch and store results before building the report

## Report Structure (17 sections, exact order)

1. **Key Metrics** — 6-card grid: Total Sales, Orders, AOV, Returning Rate, Sessions, CVR
2. **Top Products by Revenue** — TWO tables:
   - **Revenue & Conversion Performance**: #, Product, Revenue, Units, PDP Views, CVR, ATC %, RPPV (Revenue Per PDP View), Share
     - PDP Views: from sessions table grouped by landing_page_path (filter /products/ paths, combine variants of same product)
     - CVR: weighted average across all PDP URLs for that product
     - ATC %: weighted average add-to-cart rate
     - RPPV: Net Revenue / PDP Views — the true product-level efficiency metric
     - Show dash (—) for products without dedicated PDPs (guarantee, shipping protection)
   - **Profitability & Discount Dependency**: #, Product, Gross, Disc %, Return %, Margin (net/gross), Net Revenue
     - Source from: `FROM sales GROUP BY product_title SHOW orders, gross_sales, net_sales, discounts, returns`
     - Color-code: red for high discount % (>20%) and low margin (<70%), green for low discount and high margin
   - Flag "false hero" products: high revenue but low margin due to discount dependency
   - Flag broken PDPs: high PDP views but very low CVR (<0.5%) = UX or pricing issue
   - Flag return risk products: return rate >8%
3. **Category Revenue Split** — group products into categories, show which category drives the business
4. **New vs Returning Customers** — TWO tables:
   - **Order & Revenue Breakdown**: Revenue, Orders, AOV, Share per segment
   - **Session & Conversion Breakdown**: Sessions, CVR, ATC Rate, RPS per segment (source from GA4 if available, note if estimated)
   - Flag the trust gap between new and returning visitor CVR
5. **Order Profitability** — gross sales, discounts, returns, net sales, shipping, taxes, total sales. Show amount + % of gross for each line. Then:
   - **Discount Deep-Dive** subsection with 3 tables:
     a. **Discounted vs Full-Price Orders**: % of orders, AOV, Contribution Margin, Delta
     b. **Discount Type Split**: Automatic (compare-at/auto) vs Discount Codes (manual), Amount, Share of Total — totals MUST match the profitability table discount number
     c. **Top Discount Codes**: Code name, Orders, Total Discount, Avg/Order, Avg % Off (top 8-10 codes)
   - **CRO Recommendations — Discount Strategy** (5 actionable experiments):
     1. Remove discount codes for returning customers
     2. Replace % discounts with bundle/BOGO framing
     3. Introduce threshold-based free gift incentives
     4. A/B test removing abandoned cart discount codes
     5. Audit automatic discounts (compare-at credibility)
6. **Top Locations by Country** — Enhanced table with columns: #, Country, Revenue, Orders, AOV, Ship/Order, Margin, Share
   - Calculate Ship/Order as: (total_sales - net_sales - taxes) / orders
   - Calculate Margin as: net_sales / gross_sales * 100
   - Color-code: green for high AOV/margin, red for low AOV/margin and high shipping
   - **CRO / Growth Plays — Geo Strategy** (5 actionable experiments):
     1. Geo-based pricing tests for high-AOV countries
     2. Shipping threshold optimization by country
     3. Localized PDP/landing pages for top non-US markets
     4. Country-specific bundles for low-AOV regions
     5. Kill/reduce spend in low-margin regions
7. **Order Value Distribution** — bucket orders into price ranges, identify concentration points and pricing gaps for bundles
8. **Product Affinity (Products Bought Together)** — co-purchase pairs, signal strength, revenue impact. For deep order-level analysis, run `/fbt-analysis` separately.
9. **Top Landing Pages** — sessions, bounce rate, ATC rate, CVR per landing page. Flag high-converting pages AND high-traffic/low-CVR pages (revenue leaks)
10. **Acquisition Sources** — sessions, share, bounce, ATC rate, CVR per channel. Flag underutilized high-CVR channels (especially email)
11. **Device Analysis** — sessions, share, bounce, ATC rate, checkout rate, CVR per device. Flag mobile vs desktop gap
12. **Overall Conversion Funnel** — visual funnel: Sessions -> After Bounce -> ATC -> Checkout -> Converted. Show drop-off % at each stage
13. **Return Analysis by Product** — revenue, return amount, return rate per product. Flag products above 8% return rate
14. **Frequently Bought Together** — top product combinations with signal strength and revenue impact
15. **Bundling Opportunities** — 3-5 bundle concepts with suggested price and data-backed rationale
16. **Key Insights Summary** — top 5-7 findings ranked by revenue impact
17. **Next Steps** — prioritized action items tied to findings

## Output
- Generate styled HTML report and publish to here.now
- Save markdown to `clients/{slug}/research/shopify-analytics.md`
- Generate PDF: `{Brand}-Analytics-Report-Validare.pdf` (portrait, A4, 20mm margins)
- Create Notion research page with FULL content (not just a link), using proper Notion markdown
- Link the here.now URL in the Notion Research database "Link to Doc" field
- Generate 8-10 insights in the Notion Insights database

## Notion Formatting Rules
- Use actual line breaks, never escaped `\n`
- Tables must have real pipe characters `|`, never `\\|`
- No em dashes anywhere
- Verify the page renders properly after writing

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
