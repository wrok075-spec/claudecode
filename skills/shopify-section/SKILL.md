---
name: shopify-section
description: Create a new fully customizable Shopify Dawn theme section.
---

Create a new fully customizable Shopify Dawn theme section.

Section name/description: $ARGUMENTS

## Proven TT Reference Templates
When asked to use TT/draft theme code, check if a matching template exists at `/Users/eapple/tongue-tang-theme/sections/`:
- `tt-homepage-hero.liquid` — hero with star rating badge, trust bar
- `tt-collection.liquid` — collection grid with inline USP cards + review slider
- `tt-product-chocolate.liquid` — PDP with bundle selector, shipping tracker, viewer count
- `tt-product-lollies.liquid` — PDP with tier cards, flavor picker, urgency countdown
- `tt-product-lollies-bundle.liquid` — PDP with per-box flavor picker
- `tt-bundle-builder.liquid` — build-your-own bundle page with tiered discounts
- `tt-usp-bar.liquid` — USP marquee bar
- `tt-usp-cards.liquid` — icon USP cards row
- `tt-reviews.liquid` — scroll-snap review carousel
- `tt-instagram-reels.liquid` — UGC reel grid
- Snippets: `tt-cart-enhancements.liquid` (cart drawer), `tt-mobile-nav.liquid` (mobile menu)

If a match exists, read it first and adapt rather than building from scratch.

Requirements:
- Create a Liquid section file in `sections/` with a complete {% schema %} block
- Every visual property must be customizable: padding top/bottom, background color, text color, font size, font weight
- If the section contains benefits or icons, extract them into a separate snippet in `snippets/`
- Schema settings must include: section header (text, size, color, weight), content blocks, spacing controls
- Use CSS custom properties for all theme values — no hardcoded colors or sizes
- Mobile-first responsive layout
- Follow the existing Dawn theme CSS naming conventions
- Output the complete file(s) with all code, ready to drop in

After creating the file(s), ask: "Push to draft theme?"
