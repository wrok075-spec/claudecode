---
name: fbt-analysis
description: Run a Frequently Bought Together analysis on a Shopify store. Pulls real order data via Admin GraphQL, calculates co-purchase pairs, attach rates, basket sizes, free gift cannibalization, and generates data-backed bundle recommendations.
---

Run a Frequently Bought Together (FBT) analysis on a Shopify store.

Store slug and date range: $ARGUMENTS (e.g., "tongue-tang 2025-10-25 2026-04-25")

## Pre-requisite
Shopify CLI must be authenticated:
```
shopify store auth --store {store-id}.myshopify.com --scopes read_orders,read_products
```

## Data Collection

Pull 5,000+ orders via Admin GraphQL using `shopify store execute`. Paginate with cursor.

GraphQL query:
```graphql
{
  orders(first: 250, sortKey: CREATED_AT, reverse: true, query: "created_at:>{start_date}") {
    pageInfo { hasNextPage endCursor }
    edges {
      node {
        id
        lineItems(first: 20) {
          edges {
            node {
              title
              quantity
              originalUnitPriceSet { shopMoney { amount } }
            }
          }
        }
      }
    }
  }
}
```

Paginate using `after: "{endCursor}"` until 5,000+ orders or no more pages.

## Product Title Normalization (CRITICAL)

Before analyzing, normalize product titles to group variants:
- Combine product name variations (e.g., "Advanced Copper Peptide Hair Growth Formula" and "Advanced Copper Peptide Hair Regrowth Formula" = same product)
- Keep FREE items prefixed with "FREE " for separate tracking
- Normalize guarantee/warranty variants (e.g., "90 Day Money Back Guarantee" and "90 Day Money back Guarantee" = same)
- Group by product family, not exact title

## Analysis to Run

### 1. Product Frequency
Count how many orders each product appears in. Show:
- Product name, order count, % of total orders
- Sort by order count descending
- Separate paid products from free items

### 2. Basket Size Distribution
Count paid products per order (exclude free items):
- 1 paid product, 2, 3, 4+ with order count and %
- Flag single-product basket % -- this is the cross-sell opportunity ceiling

### 3. Co-Purchase Pairs (Paid Products Only)
For every order with 2+ paid products, count each product pair:
- Pair name, co-order count, attach rate
- Attach rate = co-orders / min(productA_total_orders, productB_total_orders)
- Sort by co-order count descending, show top 15-20
- Flag pairs with high attach rate (>50%) but low volume = hidden opportunity

### 4. Free Gift Co-Occurrence
Count how often each free item appears with each paid product:
- Free item, times included, % of hero product orders
- Flag cannibalization: free item vs paid version of same product

### 5. Key Findings (auto-generated from data)
Identify and write up:
- **Cross-sell opportunities**: high attach rate + low penetration (product is loved when discovered but rarely surfaced)
- **Cannibalization**: free items eating paid product sales
- **Hidden gems**: products with 50%+ attach rate but <5% overall penetration
- **Single-basket problem**: if >60% of orders have 1 paid product, this is the #1 AOV lever

### 6. Data-Backed Bundle Recommendations
3-5 bundle concepts based on co-purchase data:
- Bundle name, components, separate price, bundle price, savings %
- The co-purchase signal that justifies each bundle
- Estimated AOV impact

### 7. Cart Drawer Cross-Sell Recommendations
Based on what products co-purchase most with the hero product:
- Which products to show as cart drawer add-ons
- Recommended order/priority
- Expected attach rate based on data

## Report Structure

### Report Header
- Store name, date range, total orders analyzed
- 4 metric cards: Total Orders, Unique Products, Avg Basket Size, Single-Product Order %

### Tables
All tables should include:
- Rank numbers
- Color coding: green for high attach rates (>50%), amber for moderate (20-50%), red for low (<20%)
- Monospace for numbers

### Callout Boxes
Auto-generate callouts for:
- Biggest cross-sell opportunity (red callout -- revenue being left on table)
- Cannibalization warning if detected (amber callout)
- Best performing product pair (green callout)

## Output
- Styled HTML report: `clients/{slug}/research/fbt-analysis-report.html`
- Save markdown: `clients/{slug}/research/fbt-analysis.md`
- Publish HTML to here.now
- Generate PDF: `{Brand}-FBT-Analysis-Validare.pdf` (portrait, A4, `@page{margin:40px 24px 24px 24px}`)
- Create Notion research page with FULL content
- Generate 3-5 insights in the Notion Insights database

## Styling
- Use client's brand fonts and colors from brand-dna.md or CLAUDE.md
- Validare logo: `https://framerusercontent.com/images/9JLB1g4I28JoADbhY2CFdXt2P0.png`
- Print-ready: `@page{margin:40px 24px 24px 24px}`, font-size 11px min, `break-inside:avoid` on all cards/tables

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
