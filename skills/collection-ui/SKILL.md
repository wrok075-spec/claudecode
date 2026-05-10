---
name: collection-ui
description: Build a redesigned collection page UI for a brand.
---

Build a redesigned collection page UI for a brand.

Brand URL or description: $ARGUMENTS

## Shopify Liquid Reference Template
When asked to use the TT/draft theme template, these proven references are available:
- `/Users/eapple/tongue-tang-theme/sections/tt-collection.liquid` (~1180 lines)
- Features: product grid with inline USP cards + review slider at configurable positions, working filters (checkbox + price range), sort, badge system (Bundle/Best Seller/% off), per-unit pricing via metafield, star ratings, direct ATC on single-variant products
- Template: `/Users/eapple/tongue-tang-theme/templates/collection.tt-redesign.json` — shows how USP cards and review slides are configured as blocks
- Rename `tt-col-` CSS prefix, adapt brand colors/copy

## Pre-requisites
Read these BEFORE building:
- `clients/{slug}/brand/brand-dna.md` — colors, fonts, logo, button styles, card styles
- `clients/{slug}/brand/brand-voice.md` — tone, CTA language
- Scrape the original collection page to match card styling exactly

## Process
1. If a URL is provided, scrape the page (Firecrawl with `waitFor: 8000`) and extract: products, prices, images, card styling, grid layout
2. Read brand files for colors, fonts, styling
3. Match original card styling EXACTLY (border-radius, shadows, grid columns) before adding CRO enhancements
4. Build the complete collection page

## Collection Page Structure

### 1. Scrolling Marquee Announcement Bar
- Brand secondary color background
- Scrolling text (CSS animation, not static)
- Match original site's announcement bar style

### 2. Full Navigation
- All nav items from original site
- Breadcrumbs below nav: Home > Collection Name

### 3. Collection Header
- Collection title in brand headline font
- Product count
- Optional collection description

### 4. Working Filter & Sort Bar
- **Availability filter:** checkboxes (In Stock, Out of Stock) — must actually filter the DOM
- **Price range filter:** min/max inputs in local currency with "Apply" button — must work
- **Sort dropdown:** Featured, Best Selling, Price Low-High, Price High-Low — must reorder DOM elements
- **Active filter tags:** removable pills with "Clear all" link
- All filters wired up with real JS, not just visual

### 5. Product Grid
- Responsive: 2-col mobile / 3-col desktop (match original if different)
- Product cards with:
  - Product image (hover swap if original has it)
  - Star rating with review count
  - Product title
  - Price in local currency
  - ATC button (brand primary color)
  - Bundle products get per-unit price pill: "Only Rs.483/jar"

### 6. USP Cards Inline in Grid (Z-Pattern)
Same size as product cards, placed at positions that create a Z-pattern across rows. NOT full-width banners.

**Card 1 — Brand Authority:**
Brand logo/icon + key brand claim + supporting stat

**Card 2 — Customer Review Slider:**
- Dashed border card
- Real customer reviews (from JudgeMe/review data)
- Auto-rotate every 4 seconds
- Navigation arrows + dots
- Customer photo, name, city, star rating, review text

**Card 3 — Quality Guarantee:**
Guarantee badge + brand promise + trust copy

### 7. Pagination or Load More
- Match original site's pagination style

## Design Rules
- CSS variables from brand-dna.md at top
- Brand font via Google Fonts
- Card styling MUST match original (scrape and compare before building)
- Currency in local format (Rs. for PKR)
- No emojis
- No neon colors, no invented colors
- Mobile-first responsive
- Reviews must be REAL (from JudgeMe CSV or scrape, never placeholder)
- Filters must actually work — not just visual decorations

## Output
Single self-contained HTML file with embedded CSS and JS.
Save to `clients/{slug}/designs/collection-page.html`
