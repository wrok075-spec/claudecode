---
name: cart-drawer
description: Build a CRO-optimized cart drawer.
---

Build a CRO-optimized cart drawer.

Client slug or store URL: $ARGUMENTS

## Pre-requisites (MANDATORY — do ALL before building)
1. **Scrape the live store FIRST** — use Firecrawl or Playwright to capture:
   - Homepage, PDP, collection page, cart drawer, checkout (if accessible)
   - Current cart drawer behavior (what happens when you add to cart?)
   - Payment methods visible (installments/BNPL like Afterpay, Klarna, Shop Pay Installments, Clearpay, etc.)
   - Existing trust badges, shipping bars, cross-sells, upsells
   - Free gift mechanisms, subscription toggles, shipping protection
2. **Scrape `products.json`** for real product images, prices, names, and variants
3. **Read `clients/{slug}/brand/brand-dna.md`** — colors, fonts, USPs
4. **Check shipping policy** — free shipping threshold, delivery times
5. **Check what already exists** — never build a feature the store already has. If it exists, the design should improve it, not duplicate it.

**CRITICAL: Never design a cart drawer (or any page) without scraping the live site first. Missing existing features (like installment payments, BNPL options, or existing upsells) makes the design look uninformed.**

## Decision Framework — What to Include

NOT every feature goes on every cart. Assess the client's store and pick the right combination:

| Feature | When to include | When to skip |
|---------|----------------|--------------|
| Multi-tier progress bar | Client has free shipping + free gifts at different thresholds | Only free shipping, no gifts |
| Simple shipping bar | Client has free shipping threshold only | No shipping threshold |
| Free gift display | Client gives away free products with orders | No free gifts |
| Contextual upsell banner | Client has complementary products or bundles | Single-product store |
| Cross-sell scroll | Client has 3+ products that pair well | <3 products total |
| Subscribe & Save | Client has subscription products | No subscriptions |
| Testimonial/review | Client has strong reviews (100+) | Few/no reviews |
| Gift wrap/add-on | Client sells gift items or premium products | Commodity/consumable products |
| BOGO/quantity discount | Client runs BOGO or volume discounts | No volume offers |
| Shipping protection | Client already offers it or high-AOV items | Low-AOV items, unnecessary complexity |
| Order notes | Client sells personalized/engraved items | Standard products |
| Estimated delivery | Client has reliable shipping estimates | Unpredictable shipping |
| Eco/cause badge | Client has sustainability partnerships | No cause alignment |

## Cart Drawer Feature Library (pick what fits)

### 1. Multi-Tier Progress Bar (TOP — most impactful)
Best for: stores with free shipping + free gift thresholds

**Simple version** (shipping only):
- "You're £X away from FREE shipping!" with colored progress bar
- When unlocked: "You've unlocked FREE shipping!" with checkmark animation
- Bar fills based on cart subtotal vs threshold

**Gamified version** (shipping + gifts):
- Multi-milestone progress bar with icons at each threshold
- Example thresholds: £35 Free Shipping → £45 Free Tool → £60 Free Coin Tray
- Each milestone shows: icon, label, threshold amount
- Unlocked milestones get checkmarks and green color
- Current progress highlighted: "Only £X more to receive a Free [Gift]!"
- Auto-add free gift to cart when threshold is reached (show as line item with "FREE" badge and strikethrough original price)
- Congrats message when all tiers unlocked

**Key patterns:**
- Progress bar should be the FIRST thing visible — before cart items
- Use brand accent color for the fill, not generic green
- Show the next milestone prominently, not all at once
- When threshold met, celebrate it (checkmark animation, color change, congrats text)

### 2. Cart Items
- Product image (small, square), title, variant info, price
- Quantity selector (+/- buttons) with inline update
- Remove button (X or trash icon, top right of item)
- Line item total (updates with quantity)
- Show compare-at/strikethrough price if on sale
- Show savings per item: "You save £10.00"
- For personalized products: show engraving/customization preview
- For subscription items: show "Subscribe & Save X%" badge with delivery frequency

### 3. Free Gift Display (when applicable)
Three display patterns — pick ONE based on volume of gifts:

**Inline (1-2 gifts):** Show directly as cart line items with "FREE" badge and strikethrough price
**Collapsed (3-5 gifts):** "View Your X Free Gifts" expandable accordion with gift thumbnails, names, and strikethrough values. Collapsed by default to save space.
**Banner (any count):** Horizontal strip of gift thumbnails with "Free" badges and dollar values: "S'mores Board FREE ($24.99 value) | Roasting Sticks FREE ($19.99 value)"

### 4. Contextual Upsell Banner
Dynamic based on what's in cart:
- **Single item → bundle upsell:** "Complete the Set — Save 20%"
- **Small bundle → upgrade:** "Add one more to unlock 10% off entire order"
- **Max bundle → complementary:** "Pair with [product] for the full experience"
- **Refill/consumable → subscribe:** "Subscribe & Save 15% — delivers monthly, cancel anytime"
- Show product image, name, price, one-click "ADD" button
- Dismissible (but stays for session)

### 5. "Customers Also Grabbed" / "People Also Buy" Cross-Sells
- Horizontal scrollable row of 3-4 product cards
- Each card: product image, name, star rating (if available), price, mini "ADD" button
- Cards should be actionable (not browse links — one-click add to cart)
- Pull from: same collection, frequently bought together, or best sellers
- Show "BEST SELLER" or "TRENDING" badges on top cards
- For accessories stores: show matching/complementary items

### 6. Subscribe & Save Module (when applicable)
- Appears below cart items or as upsell banner
- "Subscribe & Save X%" with clear savings amount
- Delivery frequency selector (every 2 weeks / 30 days / 60 days)
- "No commitment, cancel anytime" reassurance
- Toggle or checkbox to activate — NOT pre-selected (avoid dark patterns)
- Show per-delivery price vs one-time price comparison

### 7. Testimonial / Social Proof (high impact)
- Single rotating testimonial with: quote, customer name, verified badge
- Keep it short (2-3 lines max)
- Match product in cart if possible ("Reviewing: [product name]")
- Star rating display
- Can include review photo if available
- Position: below cross-sells, above checkout CTA

### 8. Gift Wrap / Add-On Checkbox
- "Add Luxurious Gift Wrap for Just £6.99" with checkbox
- Show preview image of gift packaging
- Include: "Includes a satin ribbon and personalized note"
- Pure margin add-on, no COGS impact
- Best for: jewelry, watches, premium goods, gifting occasions

### 9. Shipping Protection Toggle
- Pre-checked toggle: "Add Shipping Protection (£X.XX)"
- "Covers loss, damage, and delays"
- Position between subtotal and checkout button
- On/Off toggle with brief explainer on hover/tap
- NOTE: Check compliance — auto-opt-in may need review

### 10. Order Notes / Personalization
- "Add a personalized order note" expandable textarea
- Save/Cancel buttons
- After saving: shows condensed note with "Edit" link
- Best for: gift stores, engraving services, custom products

### 11. Single "CHECK OUT" CTA
- NO "View Cart" button — single primary CTA reduces decision paralysis
- Full-width, brand primary color, large text, bold font
- Show total in CTA: "CHECKOUT — £424.50"
- Sticky at bottom if cart scrolls

### 12. Trust & Reassurance Strip (below CTA)
- 2-3 compact trust points with icons
- Adapt to client: "Secure Checkout | Free Returns | UK Handcrafted"
- Or: "Free Shipping | 30-Day Returns | 24/7 Support"
- Small text, subtle styling — don't overpower the CTA
- NO payment logos unless client specifically uses them
- Include cause badge if applicable: "1 tree planted with every order"

### 13. Empty Cart State
- Clean illustration or icon (empty bag/box)
- Headline: "Your Cart is Empty"
- Brief brand message or value prop
- "Continue Shopping" CTA button
- Optional: show best sellers or categories to browse

### 14. Estimated Delivery Date
- "Expected Delivery: [Date]" or "Ships within 1-3 business days"
- Position near checkout button
- Builds urgency and sets expectations
- Calculate from client's actual shipping times

### 15. Urgency Elements (use sparingly)
- "Selling fast — Order Soon" on high-demand items
- "X people viewing this" (only if real data available)
- "Order within X hours for next-day delivery"
- NEVER use fake scarcity — must be backed by real data

## Shopify Liquid Reference Template
When asked to use the TT/draft theme template, read the proven reference:
- Read `/Users/eapple/tongue-tang-theme/snippets/tt-cart-enhancements.liquid` first
- This snippet injects into any theme's cart drawer via JS DOM manipulation + MutationObserver
- It includes: free shipping progress bar, upgrade upsell banner, cross-sell carousel, trust badges
- Rename `tt-` prefix to client prefix, adapt thresholds/copy/colors
- For Kalles themes: uses `T4SThemeJs.T4S_Jar._updateMiniCart()` — adapt for Dawn/other themes
- Also read inline cart JS from `/Users/eapple/tongue-tang-theme/sections/tt-product-chocolate.liquid` for AJAX ATC patterns

### Discount Logic for Cart Upsells
- **Upgrade upsell:** When cart has qty=1 of a product, offer qty=2 at a better per-unit price via `/cart/change.js`
- **Free shipping bar:** Set threshold from client's shipping policy, gradient fill progress bar
- **Cross-sell:** Pull from best-sellers collection, exclude items already in cart

## Design Rules
- Drawer slides in from right with smooth cubic-bezier animation
- Semi-transparent dark overlay backdrop (click to close)
- Close button (X) top right — always accessible
- Cart count badge on trigger icon
- Brand colors and fonts from brand-dna.md
- Currency in client's local format (£, $, Rs., etc.)
- Mobile-first (full-width on mobile, 420px on desktop)
- Escape key closes drawer
- Prevent body scroll when drawer is open
- All images use real product photos from client's CDN
- All prices use real product prices

## Output
Single self-contained HTML file with embedded CSS and JS.
Save to `clients/{slug}/designs/cart-drawer.html`
Include demo buttons to open with items and open empty state.
Publish to here.now for client review.
