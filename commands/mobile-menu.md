Build a CRO-optimized mobile menu drawer.

Client slug or store URL: $ARGUMENTS

## Pre-requisites (MANDATORY — do ALL before building)
1. **Scrape the live store FIRST** — use Firecrawl or Playwright to capture:
   - Current mobile menu (click hamburger, screenshot, extract ALL nav items + sub-items + URLs)
   - Current announcement bar text and styling
   - Best sellers or featured products (images, names, prices)
   - Trust badges, USPs, social proof elements
   - Payment methods, BNPL options
   - Social media links
   - Search functionality
   - Any existing promotional banners
2. **Scrape `products.json`** — get real product images, prices, names
3. **Scrape best sellers collection** — `/collections/best-selling-collection` or equivalent
4. **Read `clients/{slug}/brand/brand-dna.md`** — colors, fonts, USPs
5. **Check what already exists** — preserve ALL existing nav items, improve the presentation

**CRITICAL: Never use emojis as nav item icons. Use SVG icons or small product/category images instead. Emojis look unprofessional and AI-generated.**

## Decision Framework — What to Include

Assess the client's store and pick the right combination:

| Feature | When to include | When to skip |
|---------|----------------|--------------|
| Best sellers carousel | Client has 3+ products with images | <3 products |
| Search bar | Client has 10+ products | Very few products |
| Promotional banner | Client has active sale/promotion | No current promotion |
| Category images | Client has distinct product categories | Single-category store |
| Testimonial | Client has strong reviews (100+) | Few reviews |
| Sub-menu with products | Category has hero products to showcase | Simple nav structure |
| Bundle/sale banner | Client has bundles or active sale | No bundles/sales |
| Gift card CTA | Client sells gift cards | No gift cards |
| Trust bar | Always include | Never skip |
| Social links | Client has active social profiles | No social presence |
| Eco/cause badge | Client has sustainability partnerships | No cause |

## Mobile Menu Feature Library

### 1. Best Sellers Carousel (TOP of drawer — highest impact)
- "Best Sellers" header + "See all →" link to collection
- Horizontally scrollable card row
- Each card: **real product image** (from CDN), title, price, "ADD TO CART" button
- Cards MUST have equal height — use CSS grid or flexbox with `align-items: stretch`
- **ATC button pinned to bottom of each card** so they align even when titles wrap
- Use `display:flex; flex-direction:column; justify-content:space-between` on card body
- Show star rating + review count if available
- 3-4 cards visible with horizontal scroll, partial card visible to indicate scrollability
- Pull from actual best-selling collection or analytics data

### 2. Navigation Items
- Keep ALL existing nav items from the original site — never remove items
- Use **SVG icons** or **small category images** next to nav items — NEVER emojis
- Category images: small circular or square thumbnails from client's product photos
- Expandable sub-menus with smooth accordion animation (+/− toggle)
- Add contextual badges where relevant:
  - "NEW" badge (green) on new collections
  - "SALE" badge (red) on sale categories
  - "BEST SELLER" badge on top collection
  - "EXCLUSIVE" badge on limited editions
- Sub-menu items: show product cards with images when expanding into a category

### 3. Sub-Menu with Inline Products
When a category expands, show 2-3 product cards inline:
- Product image, name, price, star rating
- "View Product" or "Add to Cart" button
- This turns navigation into shopping — users don't need to leave the menu to discover products
- Best for: stores with clear category structure and strong hero products per category

### 4. Search Bar
- Search input at the top or just below the logo
- Placeholder: "Search [product type] here..."
- Show trending/popular searches below input
- Show popular products below search (image + name + price)

### 5. Promotional Banner
- Matches current site promotion (sale, discount code, flash sale)
- Compact design — single line with brand accent color background
- Can include countdown timer if time-limited
- Position: below header, above best sellers

### 6. Category Images/Tiles
Instead of text-only nav items, show category tiles with:
- Category image (lifestyle or product photo)
- Category name overlay
- 2-column grid for visual categories
- Best for: fashion, homeware, multi-category stores

### 7. Testimonial / Social Proof
- Single review with: quote, customer name, verified badge
- Position: below nav items, above trust bar
- Star rating display, keep it short (2-3 lines)

### 8. Bundle/Sale Banner
- Highlight bundle deals or active sales with 1-2 product thumbnails
- Compare-at prices visible
- Position: within nav section or below nav

### 9. Gift Card CTA
- "Give the Gift of [Brand]" banner with starting price
- Subtle styling, position below nav items

### 10. Trust Bar (always include)
- 3-column compact strip with **SVG icons** — NOT emojis
- Adapt to client's actual USPs (shipping, returns, quality, security)
- Subtle background color, small text

### 11. Eco/Cause Badge
- Single line with SVG icon if client has sustainability partnerships
- Green-tinted, subtle

### 12. Social Links
- Horizontal row of circular social icon buttons
- Brand-colored hover state
- Only include platforms the client actively uses

### 13. Category Descriptions
Sub-items with 1-line descriptions for context:
- "Grinders — Spectacular Grande suitable for salt or pepper"
- Helps users navigate faster

## Design Rules (CRITICAL)
- **NO EMOJIS anywhere** — use SVG icons or category images only
- Mobile-only component (full width on mobile, 340px drawer on tablet)
- Drawer slides in from LEFT with smooth cubic-bezier animation
- Semi-transparent dark overlay backdrop (click to close)
- Close button (X) top right — always accessible
- Escape key closes drawer
- Brand colors and fonts from brand-dna.md
- All images use real product photos from client's CDN — never placeholders
- **Card alignment**: ATC buttons MUST be pinned to bottom of cards using flexbox column layout with `margin-top:auto` on the button — so buttons align horizontally regardless of title length
- Prevent body scroll when drawer is open
- Smooth accordion animation for sub-menus
- The menu MUST look hand-designed and premium — not AI-generated
- Match the brand's exact visual language (typography, spacing, color palette)

## Output
Single self-contained HTML file with embedded CSS and JS.
Save to `clients/{slug}/designs/mobile-menu.html`
Publish to here.now for client review.
Always ask: "Is this for Validare or CROTactic?" before building.
