---
name: bundle-builder
description: Build a CRO-optimized "Build Your Own Bundle" page with tiered volume discounts, product selection grid, and sticky ATC bar.
---

Build a CRO-optimized "Build Your Own Bundle" page with tiered volume discounts.

Client slug or store URL: $ARGUMENTS

## Shopify Liquid Reference Template
When asked to use the TT/draft theme template, read: `/Users/eapple/tongue-tang-theme/sections/tt-bundle-builder.liquid` (~1290 lines)
Template JSON: `/Users/eapple/tongue-tang-theme/templates/page.tt-bundle.json`

This is a proven section with:
- Hero banner with 3-step wizard instructions
- Product grid from a configurable collection
- 3 configurable discount tiers (qty + percentage)
- Visual progress bar with animated tier circles
- Sticky bottom CTA bar with thumbnail stack of selected products
- Per-item cost display + green savings text
- Trust badges (Quality Guaranteed, Fast Delivery, Social proof count)
- AJAX ATC with Kalles cart drawer integration (adapt for other themes)

## Pre-requisites (MANDATORY)
1. **Scrape the live store** — products, prices, images, collections
2. **Read `clients/{slug}/brand/brand-dna.md`** — colors, fonts, USPs
3. **Identify bundle-worthy products** — which collection should be the source?
4. **Determine discount tiers** — e.g., 3 items = 10%, 4 = 15%, 5 = 20%
5. **Determine free shipping threshold** if applicable

## Bundle Page Structure

### 1. Hero Section
- "Build Your Own Bundle" headline with subtitle
- 3-step process: "1. Choose items → 2. Pick quantity → 3. Save more"
- Visual step indicators

### 2. Product Selection Grid
- Products from a configurable collection
- Each card: product image, title, subtitle (via metafield), price, +/- quantity selector
- Selected state: accent border + background highlight
- Badge system for featured products (configurable tag match)
- Min/max item limits

### 3. Tiered Discount Progress Bar
- Visual progress bar with tier circles at each threshold
- Dynamic messaging: "You are X item(s) away from Y% off!"
- Animated fill as items are added
- Green savings text when threshold hit: "You save Rs.X (Y% off)"
- Tier circles light up and get checkmarks when reached

### 4. Sticky Bottom CTA Bar
- Fixed bar at bottom of viewport
- Thumbnail stack of selected products (overlapping circles)
- Item count + per-item price
- Total price with savings
- "Add Bundle to Cart" button (disabled until min items reached)
- Different CTA text for disabled vs enabled state

### 5. Trust Badges
- 3 badges with SVG icons below the grid
- Adapt to client USPs

## Discount Logic

### IMPORTANT: Three mechanisms available

**Mechanism A: Client-side calculated (needs backend enforcement)**
- JS calculates price from base x (1 - tier%)
- Sends `_bundle_discount` as line item property
- REQUIRES Shopify Script, Function, or automatic discount to actually apply at checkout
- **Risk:** Without backend discount, customer pays full price

**Mechanism B: Pre-priced bundle variants (RECOMMENDED)**
- Create actual bundle products in Shopify admin at the discounted price
- Each tier points to a real variant ID
- Compare-at price shows original as strikethrough
- **Most reliable — no scripts needed**

**Mechanism C: Shopify automatic discount**
- Create an automatic "Buy X Get Y% Off" discount in Shopify admin
- JS sends items to cart normally, discount auto-applies
- **Good middle ground — no custom scripts, works at checkout**

### Always clarify with client which mechanism to use before building.

## Cart Integration
- AJAX POST to `/cart/add.js` with items array
- For Kalles: `T4SThemeJs.T4S_Jar._updateMiniCart()` + fallback `/?sections=mini_cart`
- For Dawn: dispatch `cart:updated` event + fetch section rendering
- Cart drawer auto-opens after adding
- Update cart count badges: `[data-cart-count]`

## Design Rules
- Section targets `page` templates (uses `{% schema %}` with `"templates": ["page"]`)
- All colors configurable via schema settings
- Currency must use client's format (not hardcoded Rs.)
- Use `Shopify.formatMoney()` or `shop.money_format` for currency
- Mobile-first responsive
- Product cards: equal height with flexbox
- Progress bar: CSS transitions for smooth fill animation

## Output
Create the Liquid section file in the client's theme directory.
Create a `page.bundle.json` template that references the section.
Remind client to create a Page in Shopify admin and assign the bundle template.
