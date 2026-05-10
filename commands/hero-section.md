Build a CRO-optimized homepage hero section.

Client slug or store URL: $ARGUMENTS

## Pre-requisites (MANDATORY — do ALL before building)
1. **Scrape the live store FIRST** — capture:
   - Current homepage hero (screenshot + extract all text, images, CTAs)
   - Current announcement bar and header — **DO NOT CHANGE THESE**. The hero section is ONLY the content area below the header.
   - Color scheme: is the site LIGHT or DARK? Match accordingly.
   - Brand fonts (check Firecrawl branding data or inspect live site)
   - Product images, prices, review counts from `products.json`
   - Trust badges, USPs, social proof elements already on the site
2. **Read brand files** if they exist:
   - `clients/{slug}/brand/brand-dna.md` — colors, fonts, logo, USPs
   - `clients/{slug}/brand/brand-voice.md` — tone, register, CTA language
   - `clients/{slug}/brand/icp-cards.md` — objections, motivations, desires
3. **Ask: "Is this for Validare or CROTactic?"** before building

**CRITICAL RULES:**
- **NEVER change the announcement bar or header** — only redesign the hero section below them
- **Match the site's color scheme** — if the site is light/white, build a light hero. If dark, build dark. Don't default to dark.
- **Use the client's actual fonts** — check Firecrawl branding or live site CSS, don't assume
- **No emojis** — use SVG icons only
- **Assess brand positioning FIRST** — premium/luxury brands need minimalist designs with white space. Not every hero needs pills, carousels, and dense content. Don't default to cramming everything above the fold.

## Decision Framework — Brand Positioning → Design Density

| Brand Type | Design Direction | Density |
|-----------|-----------------|---------|
| Premium/luxury (watches, jewelry, fashion) | **Minimalist** — full-bleed image, bold headline, white space, single CTA | Low |
| DTC health/wellness | **Medium** — headline + USP pills + product showcase | Medium |
| Multi-SKU consumables | **Higher** — flavor selectors, subscribe & save inline | High |
| Discount/value brands | **Dense** — badges, countdowns, urgency elements | High |

### Minimalist Hero Pattern (premium brands)
Reference: Nomadic Watches redesign (Figma: JyHrzQwo0PE8tqeZvGGI0I)
- Full-bleed lifestyle image (product in real context, NOT on white background)
- Social proof pill OVERLAID on the image (bottom-left or top-left)
- Bold uppercase headline below image or overlaid
- Origin/authority line: "Built in Belfast, Northern Ireland" or "Masterfully Crafted Since 2014"
- Single CTA — wide, bold, uppercase
- Trust icons as separate row below with generous spacing
- Desktop: product card floats beside hero image (split layout)
- Mobile: stacked, generous padding between every element
- **White space is a feature** — don't fill it with more content
- Maximum 3-4 elements above fold: proof pill, headline, CTA, image
- Testimonial as separate section below, NOT crammed into hero

### Standard Hero Pattern (DTC/wellness brands)
- Social proof pill above headline
- Benefit-driven headline with accent color keyword
- USP pills (3-4 horizontal badges)
- CTA button
- Product circular picks or showcase below
- Trust bar at bottom

## Decision Framework — Light vs Dark Hero

| Site Style | Hero Background | Text Color | Accent Treatment |
|-----------|----------------|------------|-----------------|
| Light/white site | White or light (#fff, #f8f6f3) | Dark text (#363636) | Brand accent for highlights |
| Dark/premium site | Dark (#1a1a1a) or dark gradient | White text | Gold/accent for highlights |
| Image-heavy site | Full-bleed lifestyle image with gradient overlay | White text on overlay | CTA in brand color |

## Hero Section Feature Library

### 1. Social Proof Pill (ABOVE headline)
- Pill badge with star rating + customer count
- "Rated 4.9/5 by 5,000+ Customers" or "Loved by 60,000+ runners"
- Light bg: use subtle gray (#f0f0f0) background with border
- Dark bg: use semi-transparent glass effect (rgba white + backdrop-blur)
- Pull real review count from live site

### 2. Benefit-Driven Headline
- Address the primary ICP's core desire — NOT the product name
- Examples: "Handcrafted Wood Watches with Soul" not "Premium Wood Watches"
- "The Natural Way to Lower Blood Pressure" not "Health Supplements"
- Use brand heading font, large (28-32px mobile, 44-62px desktop)
- One keyword or phrase in brand accent color for emphasis

### 3. Objection-Busting Subtext
- 1-2 lines addressing key customer concerns
- Keep it specific: "Every piece features unique wood grain. Personalise with a free engraving."
- Not generic: "Shop our collection of premium products"
- 13-15px, secondary text color, max-width 400-520px

### 4. USP Pill Badges (key differentiators)
- 3-4 horizontal pills with SVG icons
- Examples: "Eco-Friendly" | "Free Engraving" | "Free Shipping" | "Warranty Included"
- Pull from brand's actual USPs — check site footer, PDP, and brand-dna.md
- Subtle background, small text (10-11px), rounded pills

### 5. Single Bold CTA
- One primary CTA — not two competing buttons
- "Shop the Collection" or "Shop Best Sellers" or "Shop Now"
- Match brand button style exactly (square corners if brand uses square, pill if pill)
- Below CTA: micro-text with secondary reassurance ("Masterfully crafted since 2014")

### 6. Product Showcase (below CTA)
Three patterns — pick ONE:

**Circular picks** (best for curated collections):
- 3-4 circular product portraits in a row
- Product name + price below each
- Hover: lift effect + accent border
- Horizontal scroll on mobile if needed

**Hero product image** (best for single-hero-product brands):
- Large product image centered below CTA
- Can include lifestyle context (product in use)

**Inline product cards** (best for multi-SKU brands with variant selection):
- Product cards with image, name, price, variant selector, ATC button
- Based on the PDF pattern: flavor/color selector + subscribe & save option
- Best for consumables, supplements, fashion

### 7. Trust Bar (bottom of hero)
- Full-width strip at the bottom of the hero section
- 3-4 columns with SVG icons
- Adapt to client: "Free Shipping | 1 Tree Planted | Warranty | Since 2014"
- Subtle border-top, lighter background
- Small text (9-10px)

### 8. Authority Badges (optional)
- "Doctor Approved" | "As Seen In [press logos]" | "NSF Certified"
- Only include if the brand has real authority claims
- Position: below subtext or within USP pills

### 9. Testimonial Quote (optional)
- Single short review quote with customer name
- Position: below product showcase or within trust bar
- Best for: brands with strong review counts

## Layout & Responsiveness (CRITICAL)

**The output MUST be a single fully responsive page — NOT separate mobile and desktop frames.**

The hero file should be ONE above-the-fold page that adapts to the browser width. When the user resizes the browser, it should seamlessly switch between mobile and desktop layouts. Never show a phone frame inside a desktop view.

### Responsive breakpoints:
- **Desktop (1024px+):** Split layout (image left, content right), desktop header with full nav, floating product card visible
- **Tablet (768px–1023px):** Stacked layout, desktop header simplifies or switches to mobile header
- **Mobile (<768px):** Fully stacked, mobile header (hamburger + logo + icons), image above content
- **Small mobile (<420px):** Smaller headline (24px), tighter padding, compact trust bar

### Desktop layout (1024px+):
- Split: lifestyle image (60% width, left) + content (40%, right)
- Floating product card overlaid on image (bottom-right)
- Desktop header: country selector left, logo center, account/search/cart right, full nav row below
- Headline: 42-62px
- Content left-aligned, not centered

### Mobile layout (<1024px):
- Stacked: image (aspect-ratio 4/3) → content below
- Mobile header: hamburger left, logo center, search + cart right
- Headline: 24-28px
- Full-width CTA button
- Trust bar compact (smaller text, tighter padding)

### Header & announcement bar rules:
- **Scrape the EXACT header and announcement bar from the live site** — match colors, fonts, layout, text, countdown timers
- Desktop header and mobile header are DIFFERENT — use media queries to show/hide the correct one
- The announcement bar stays the same across all breakpoints (just scales text down on mobile)
- NEVER simplify or redesign the header — replicate it exactly

## Design Rules
- Use client's actual fonts from the live site (Firecrawl branding data)
- Match button style exactly — square corners, pill, or rounded from brand
- No emojis anywhere
- SVG icons for all visual elements
- All product images from client's Shopify CDN — never placeholders
- Currency in client's local format
- The hero should feel hand-designed, matching the brand's exact visual language
- Match exact font-weight, letter-spacing, and text-transform from the live site

## Output
Single self-contained responsive HTML file with embedded CSS and JS.
ONE page that works at all resolutions — NOT separate mobile/desktop frames.
Header and announcement bar replicated exactly from the live site (not redesigned).
Save to `clients/{slug}/designs/hero-section.html`
Publish to here.now for client review.
