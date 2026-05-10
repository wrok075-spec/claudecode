---
name: listicle
description: "Build CRO-optimized listicle/advertorial landing pages for Shopify stores. Creates a full Liquid section + CSS + JSON template with urgency bars, countdown timers, alternating image/text items, testimonials, sticky CTAs, shipping estimates, FAQ accordions, and distraction-free layouts. Use this skill whenever the user asks to build a listicle, advertorial, landing page, long-form sales page, editorial-style product page, 'reasons why' page, or any list-style conversion page for a Shopify store. Also trigger when the user mentions 'listicle', 'advertorial', 'CRO landing page', 'sales page', or wants to create a page that reads like an article but sells a product."
---

# Listicle Builder

Build high-converting listicle/advertorial landing pages for Shopify stores. These are distraction-free, editorial-style pages that use CRO psychology (urgency, social proof, trust, friction reduction) to convert readers into buyers.

## What You Build

A complete set of Shopify theme files:

| File | Purpose |
|------|---------|
| `sections/listicle-{slug}.liquid` | Main section: all HTML, JS, and schema |
| `assets/listicle-{slug}.css` | All styles with CSS custom properties |
| `templates/page.{slug}.json` | Page template with layout override |
| `layout/theme.listicle.liquid` | Stripped layout (no header/footer/announcement) |

## Before You Start: Gather Info

Collect these from the user (ask if not provided):

1. **Store domain** — the `xxx.myshopify.com` domain (needed for CLI and product data)
2. **Product URL(s)** — fetch product images/data via appending `.json` to the product URL
3. **Brand accent color** — default `#f1cc19` (gold). Ask the user or pull from `config/settings_data.json`
4. **Key selling points** — a transcript, bullet list, or product description to base the copy on
5. **Product variants** — are there gender/type variants (men/women, etc.)? This determines whether CTAs are single or dual buttons
6. **Current offer** — what's the actual free gift / discount / shipping offer? Never assume "free comb" or generic offers. Check the product page.

### Fetching Product Data

Get real product images from the store's CDN — never use AI-generated images unless specifically asked:

```bash
curl -s 'https://STORE.myshopify.com/products/HANDLE.json' | python3 -c "
import json,sys
p=json.load(sys.stdin)['product']
print(p['title'])
for img in p['images']:
    print(img['src'])
"
```

Use these CDN URLs as fallback defaults in the section. Every image should also have an `image_picker` schema setting so the merchant can override it in the theme editor.

## Page Architecture

The listicle follows this exact structure (this rhythm is proven to convert):

```
URGENCY BAR (countdown + offer text)
HERO (headline, byline, summary)
ITEM 1 (image left, text right)
ITEM 2 (image right, text left) ← alternating
TESTIMONIAL CARD
ITEM 3
ITEM 4 (reversed)
TESTIMONIAL CARD
ITEM 5
─── MID-ARTICLE CTA BANNER ───
ITEM 6 (reversed)
ITEM 7
TESTIMONIAL CARD
ITEM 8 (reversed)
ITEM 9
ITEM 10 (reversed)
HOW IT WORKS (3 steps)
FINAL CTA
FAQ ACCORDION
─── STICKY CTA BAR (fixed bottom) ───
```

### Why This Structure Works

- **Alternating images** create visual rhythm that keeps readers scrolling
- **Testimonials between items** inject social proof at natural pause points
- **Mid-article CTA** catches readers who are already convinced (don't make them scroll to the bottom)
- **Sticky CTA** ensures a buy button is always one tap away
- **No header/footer** eliminates escape routes — the only actions available are "keep reading" or "buy"

## File Templates

### 1. Layout: `layout/theme.listicle.liquid`

Copy the store's existing `layout/theme.liquid` but remove:
- `{% sections 'header-group' %}` (the `<div id="header-group">` block)
- `{% sections 'footer-group' %}`
- Any announcement bar references

Keep everything else (meta tags, stylesheets, fonts, scripts, analytics, `{{ content_for_header }}`). Add `style="margin:0;padding:0;"` to the `<main>` tag.

### 2. Page Template: `templates/page.{slug}.json`

```json
{
  "layout": "theme.listicle",
  "sections": {
    "listicle": {
      "type": "listicle-{slug}",
      "settings": {}
    }
  },
  "order": ["listicle"]
}
```

The `"layout": "theme.listicle"` key is what strips the header/footer.

### 3. CSS: `assets/listicle-{slug}.css`

Use CSS custom properties so the entire color scheme can be changed in one place. Read `references/css-template.md` for the full production CSS.

Key variables to define:
```css
:root {
  --lv-accent: #f1cc19;       /* brand accent — change this per store */
  --lv-accent-soft: #fdf8e1;  /* light tint of accent */
  --lv-dark: #1a1a1a;
  --lv-text: #333;
  --lv-muted: #777;
  --lv-bg: #ffffff;
  --lv-surface: #f9f9f9;
  --lv-border: #eee;
  --lv-radius: 16px;
  --lv-star: var(--lv-accent); /* review stars match accent */
}
```

**Responsive breakpoint**: single column below 700px. On mobile:
- Grid items stack to single column
- Reversed items lose their order override
- CTA banner stacks vertically
- Sticky CTA buttons go full-width side by side
- FAQ and urgency bar text shrink slightly

### 4. Section: `sections/listicle-{slug}.liquid`

Read `references/section-template.md` for the complete annotated section template with all CRO elements.

Key patterns:

**Image with picker fallback:**
```liquid
{%- if section.settings.image_1 != blank -%}
  <img src="{{ section.settings.image_1 | image_url: width: 800 }}" alt="..." loading="lazy">
{%- else -%}
  <img src="{{ fallback_cdn_url }}" alt="..." loading="lazy">
{%- endif -%}
```

**Alternating layout:**
```html
<article class="lv-item">...</article>              <!-- image left -->
<article class="lv-item lv-item--reverse">...</article>  <!-- image right -->
```

**Countdown timer** (cycles every 3 hours):
```javascript
var total = (3*3600) - (Math.floor(Date.now()/1000) % (3*3600));
```

**Sticky CTA** (scroll-triggered):
```javascript
var threshold = 400;
window.addEventListener('scroll', function() {
  if (window.pageYOffset > threshold) {
    stickyEl.classList.add('lv-sticky-cta--visible');
  }
}, { passive: true });
```

**IP Geolocation for shipping estimate:**
- Primary: `https://ipwho.is/` (free, HTTPS, unlimited, no key)
- Fallback: `https://ipapi.co/json/`
- NEVER use `ip-api.com` — it doesn't support HTTPS, fails silently on Shopify

**Shipping date calculation** (today + 4 business days, skipping weekends):
```javascript
var d = new Date(), added = 0;
while (added < 4) {
  d.setDate(d.getDate() + 1);
  if (d.getDay() !== 0 && d.getDay() !== 6) added++;
}
```

## Schema Settings

The section schema must include `image_picker` settings for every visual element. This is non-negotiable — merchants must be able to swap images in the theme editor without touching code.

```json
{
  "type": "image_picker",
  "id": "image_1",
  "label": "Image - Item 1"
}
```

Include pickers for: author avatar, each listicle item image, CTA banner image.

## Writing the Copy

When given a transcript, product description, or bullet points:

1. **Headline**: "X Reasons Why [Product] Is the #1 Way to [Desired Outcome]"
2. **Each item**: Lead with the benefit, not the feature. Make it personal ("you" language). Bold the key takeaway in each paragraph.
3. **Testimonials**: Use first-person quotes with specific details. Include name and location. Always 5 stars.
4. **FAQ**: Address the top 4-5 objections (duration, safety, results, returns, how-to)
5. **Urgency bar**: Match the actual store offer exactly. Don't invent offers.

## Push Workflow

After creating all files:

1. Find the live theme:
   ```bash
   shopify theme list --store DOMAIN.myshopify.com
   ```

2. Push only the listicle files:
   ```bash
   shopify theme push --theme THEME_ID --store DOMAIN.myshopify.com --allow-live \
     --only "sections/listicle-{slug}.liquid" \
     --only "assets/listicle-{slug}.css" \
     --only "templates/page.{slug}.json" \
     --only "layout/theme.listicle.liquid"
   ```

3. The merchant then creates a page in Shopify admin, assigns the template, and sets the URL handle.

## Common Pitfalls

| Mistake | Fix |
|---------|-----|
| Using `ip-api.com` for geolocation | Use `ipwho.is` — ip-api.com doesn't support HTTPS |
| Hardcoding images without picker | Every image needs an `image_picker` + CDN fallback |
| Inventing offers (free comb, etc.) | Always ask or check the actual product page |
| Forgetting `--allow-live` flag | Required when pushing to the published theme |
| Adding section outside `"sections"` in JSON | The section definition must be inside the `"sections": {}` object |
| Using AI-generated images | Use real product CDN images unless told otherwise |
| Lime green / generic colors | Pull actual brand colors from `config/settings_data.json` |
| Leaving header/footer on listicle | Use `"layout": "theme.listicle"` in the page template |
