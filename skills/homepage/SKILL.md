---
name: homepage
description: Build a CRO-optimized full homepage for a Shopify store.
---

Build a CRO-optimized full homepage for a Shopify store.

Client slug or store URL: $ARGUMENTS

## Shopify Liquid Reference Templates
When building as Shopify Liquid sections (not just HTML mockup), ALWAYS read these proven TT templates first:
- **Hero:** `/Users/eapple/tongue-tang-theme/sections/tt-homepage-hero.liquid` — star rating badge, trust bar, dual mobile/desktop images
- **USP Bar:** `/Users/eapple/tongue-tang-theme/sections/tt-usp-bar.liquid` — marquee on mobile, static on desktop
- **USP Cards:** `/Users/eapple/tongue-tang-theme/sections/tt-usp-cards.liquid` — icon circles with title + description
- **Reviews:** `/Users/eapple/tongue-tang-theme/sections/tt-reviews.liquid` — scroll-snap carousel with dots/arrows
- **Instagram/UGC:** `/Users/eapple/tongue-tang-theme/sections/tt-instagram-reels.liquid` — two-column with reel grid
- Rename `tt-` prefix to client prefix, adapt brand colors/copy via schema settings

## Pre-requisites (MANDATORY)
1. **Scrape the live store** — homepage, PDP, collection, cart drawer, footer, announcement bar, header
2. **Get branding** — Firecrawl branding scrape for actual fonts, colors, button styles, border-radius
3. **Get products** — `products.json` for real images, prices, names, review counts
4. **Get collections** — all collection names, URLs, and product counts
5. **Read brand files** if they exist — brand-dna.md, brand-voice.md, icp-cards.md
6. **Check what already exists** — what sections does the current homepage have?
7. **Ask: "Is this for Validare or CROTactic?"**
8. **Assess brand positioning** — premium/luxury (minimal) vs DTC/wellness (medium density) vs value (dense)

## Homepage Section Architecture (12 sections — pick what fits)

Build the homepage as a single responsive HTML file. Every section below is a module — include the ones that fit the brand, skip the rest. The order below is the recommended flow.

### Section 1: Hero
Use the `/hero-section` skill patterns. Key options:
- **Minimalist** (premium brands): full-bleed lifestyle image, bold headline, single CTA, trust strip
- **Video hero** (engagement brands): looping background video with overlay content
- **Standard** (DTC/wellness): social proof pill, headline, USP pills, CTA, product showcase
- Header and announcement bar: replicate EXACTLY from live site, don't redesign

### Section 2: Value Propositions / USP Strip
3-column strip below hero with icon + title + 1-line description:
- "Expert Wellness Guidance — Unlock your wellness potential with personalised advice"
- "Unmatched Customer Support — Experience seamless service from purchase to delivery"
- "Satisfaction Guarantee — Your peace of mind is our top priority"
- SVG icons, not emojis. Brand accent color for icons.
- Light background (#fafafa) or white with subtle border-top

### Section 3: Shop by Category / Filter
Interactive category filters that let visitors self-select:
- **Health goal filter** (wellness): "Choose Your Health Goal" — pills/buttons for each benefit
- **Category tiles** (fashion/multi-product): image tiles for each collection (2-3 column grid)
- **Location/type filter** (home goods): "Indoor vs Outdoor" or "By Room" toggle
- **Capacity/size filter**: "1 Person | 2 Person | 3 Person" buttons
- Shows relevant products when a filter is selected
- Each product card: image, star rating, review count, name, compare-at price, sale price, savings badge, short description, ATC button

### Section 4: Featured Products / Best Sellers
Horizontal scrollable product cards (4-6 products):
- Real product images from CDN
- Star rating + review count
- Product name
- Compare-at price (strikethrough) + sale price
- "You Save $X" badge
- Short 1-2 line description
- ATC button
- Can be filtered by category (tabs above: "All | Indoor | Outdoor")

### Section 5: Health Benefits / Why This Product
Educational section explaining product benefits:
- Section heading: "Discover the Health Benefits of [Brand] [Product]"
- Subheading: "Unveil the Transformative Power of [category] for Mind, Body, and Spirit"
- 3-4 benefit cards with icon, title, 2-3 line description
- Examples: Stress Relief, Pain Relief, Detoxification, Passive Cardio
- Social proof pill at top of section ("Rated 4.57/5 by Thousands of Happy Customers")
- Clean grid layout, generous white space

### Section 6: Quiz / Product Finder CTA
Full-width banner driving visitors to a product quiz:
- "Not Sure Where to Start?"
- "Take our [product] quiz to find out which [product] is perfect for you."
- Single CTA button: "Take Quiz Now"
- Can include a lifestyle image or illustration
- Links to Heyflow, Typeform, or Shopify quiz app

### Section 7: Social Proof / Testimonial Feature
Single featured testimonial with depth:
- Large quote text
- Customer name + "Verified Buyer" badge
- Star rating
- Optional: customer photo or product photo
- Context line: "Best knowledge in the industry" or review title
- NOT a carousel of tiny reviews — one impactful story

### Section 8: Us vs Them / Comparison Table
Side-by-side comparison: Brand vs "Others" or vs specific competitors:
- Checkmarks for brand, X marks for others
- 6-8 comparison points (free shipping, warranty, reviews, quality, assembly, etc.)
- Brand column highlighted with accent color
- "Shop Best Sellers Now" CTA at bottom
- Clean table design, not cluttered

### Section 9: How It Works / 3-Step Process
Simple 3-step strip explaining the purchase/use journey:
- Step 1: "Select product" — description
- Step 2: "Easy payment" — description (mention financing/BNPL if applicable)
- Step 3: "Free delivery" — description
- Numbered or icon-based steps
- Horizontal on desktop, vertical on mobile

### Section 10: Instagram / UGC Gallery
Social proof through real customer photos:
- "See how [brand] [products] are [being used] across [location]"
- 4-6 Instagram-style square photos in a grid/row
- @handle tag
- Links to Instagram profile
- Can use real Instagram embed or scraped images

### Section 11: FAQ Accordion
6-8 most common questions:
- Expandable accordion (click to open/close)
- Questions from the client's actual FAQ page
- Covers: shipping, returns, warranty, assembly, sizing, payment options
- Clean, minimal design

### Section 12: Final CTA Banner
Full-width closing CTA:
- Social proof pill ("Rated X/5 by Thousands of Happy Customers")
- Bold headline: "Your Wellness Oasis Awaits" or "Explore Our Collection"
- Subtext reinforcing the main value prop
- CTA button: "Shop Best Sellers Now"
- Lifestyle background image or brand gradient

### Section 13: Footer
Replicate the existing footer structure from the live site:
- Column layout: Quick Links, Contact Info, Newsletter signup
- Social media icons
- Payment method logos (if applicable)
- Copyright line
- Match exact styling from live site

## Product Card Design Rules
Every product card across ALL sections must be consistent:
- Real product image (from CDN, not placeholder)
- Star rating + review count (if available)
- Product name
- Compare-at price (strikethrough) + sale price
- "You Save $X" or "Save X%" badge
- Short description (1-2 lines)
- ATC button matching brand button style
- Cards must have equal height (flexbox with align-items: stretch)
- ATC button pinned to bottom of card (margin-top: auto)

## Responsive Rules
- Single responsive file — NOT separate mobile/desktop frames
- Header: desktop version (1024px+) with full nav, mobile version (<1024px) with hamburger
- Announcement bar: same across breakpoints, text scales down
- Product grids: 4 columns desktop → 2 columns tablet → 1-2 columns mobile
- All sections stack vertically on mobile with generous padding
- Trust/USP strips: horizontal on desktop, 2x2 or stacked on mobile

## Design Rules
- Match the client's actual fonts, colors, button styles from the live site
- No emojis — SVG icons only
- All images from client's Shopify CDN
- Currency in client's format
- Header and announcement bar replicated exactly — not redesigned
- The homepage should feel hand-designed and premium, not AI-generated
- White space is a feature for premium brands
- Match exact font-weight, letter-spacing, text-transform from live site

## Output
Single self-contained responsive HTML file with embedded CSS and JS.
Save to `clients/{slug}/designs/homepage.html`
Publish to here.now for client review.
