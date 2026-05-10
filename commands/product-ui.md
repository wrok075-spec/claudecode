Build a CRO-optimized product page UI.

Product URL or description: $ARGUMENTS

## Pre-requisites
Read these BEFORE building:
- `clients/{slug}/brand/brand-dna.md` — colors, fonts, logo, button styles, card styles
- `clients/{slug}/brand/brand-voice.md` — tone, CTA language
- `clients/{slug}/brand/icp-cards.md` — objections, motivations

## Process
1. If a URL is provided, scrape the page (Firecrawl with `waitFor: 8000`) and extract: product name, images, variants, prices, reviews, description, trust badges
2. Read brand files for colors, fonts, styling rules
3. Build the complete PDP

## PDP Structure

### 1. Product Gallery with Thumbnails
- Main image + thumbnail strip below or beside
- Image swaps on variant/bundle change (show bundle photo when bundle selected)
- Zoom on hover (desktop) or tap (mobile)

### 2. Product Title + Rating
- Product name in brand headline font
- Star rating with review count (pull real data): "4.8 (234 reviews)"

### 3. Bundle Selector Cards
- Visual cards for each option: 1 unit / 3-pack / 5-pack (adapt to actual product)
- Each card shows: quantity, total price, per-unit price, save % badge
- "Most Popular" or "Best Value" badge on recommended tier
- Selected card has brand primary border/highlight

### 4. Weight/Size Selector
- Pill buttons for variants (weight, size, flavor, etc.)
- Selected pill filled with brand primary color

### 5. "What's Included" Link (bundles only)
- Small underlined text with info icon below bundle selector
- Opens a modal with product photos, names, weights for the bundle
- Hidden for single-item variants

### 6. Dynamic Pricing
- Price updates on bundle/weight change
- Per-unit price shown as pill badge: "Only Rs.483/jar"
- NO compare-at strikethrough — use per-unit framing instead

### 7. Quantity Selector + CTAs
- Qty selector (+/- buttons)
- Full-width "Add to Cart" button (brand primary color)
- "Buy It Now" below (brand secondary or outline style)

### 8. 3-Step Shipping Tracker
- Ordered -> Shipped -> Delivered with estimated dates
- Dates calculated dynamically: today + delivery window (e.g., 4-5 days)
- Progress bar at ~15% (order placed stage)
- Not static text — real date calculation in JS

### 9. Trust Badges Row
- 4 badges: Quality Guaranteed, Fast Delivery, Flat-rate Shipping, Social proof count
- Brand primary color for icons
- Horizontal row, centered

### 10. Social Proof
- "X people are viewing this right now" with pulsing green dot
- Randomized number (15-45 range) that updates occasionally

## Design Rules
- Set CSS variables from brand-dna.md at top of file
- Brand font via Google Fonts import
- Match button styles (pill/rounded, colors) from brand
- Currency in local format (Rs. for PKR, never USD unless US brand)
- Card styling matches original site (border-radius, shadows)
- Mobile-first, above-the-fold focused, compact
- No emojis unless brand uses them

## Output
Single self-contained HTML file with embedded CSS and JS.
Save to `clients/{slug}/designs/product-page.html`
