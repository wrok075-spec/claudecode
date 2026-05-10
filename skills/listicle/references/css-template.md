# Listicle CSS Template

Production-ready CSS for listicle pages. Copy this and customize the `:root` variables per brand.

```css
/* ── Listicle – CRO Advertorial ───────────────── */

.lv * { box-sizing: border-box; margin: 0; padding: 0; }
.lv img { max-width: 100%; height: auto; display: block; }
.lv a { text-decoration: none; color: inherit; }

:root {
  --lv-accent: #f1cc19;       /* CHANGE per brand */
  --lv-accent-soft: #fdf8e1;  /* light tint of accent */
  --lv-dark: #1a1a1a;
  --lv-text: #333;
  --lv-muted: #777;
  --lv-bg: #ffffff;
  --lv-surface: #f9f9f9;
  --lv-border: #eee;
  --lv-radius: 16px;
  --lv-star: var(--lv-accent);
}

.lv-container { max-width: 780px; margin: 0 auto; padding: 0 24px; }

/* ── Urgency bar ─────────────── */
.lv-urgency {
  background: var(--lv-accent-soft);
  text-align: center;
  padding: 10px 20px;
  font-size: 13px;
  font-weight: 700;
  color: var(--lv-dark);
  letter-spacing: 0.04em;
  text-transform: uppercase;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
}
.lv-countdown { display: inline-flex; gap: 6px; }
.lv-countdown__box {
  background: #fff;
  border: 1px solid #ddd;
  border-radius: 6px;
  padding: 4px 8px;
  font-size: 14px;
  font-weight: 800;
  min-width: 32px;
  text-align: center;
}
.lv-countdown__box small {
  display: block;
  font-size: 8px;
  font-weight: 500;
  color: var(--lv-muted);
  text-transform: uppercase;
}

/* ── Hero / Header ───────────── */
.lv-hero { padding: 48px 0 32px; }
.lv-hero h1 {
  font-family: Inter, -apple-system, sans-serif;
  font-size: clamp(28px, 4.5vw, 42px);
  font-weight: 800;
  line-height: 1.2;
  color: var(--lv-dark);
  margin-bottom: 20px;
}
.lv-byline {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}
.lv-byline__avatar {
  width: 44px; height: 44px;
  border-radius: 50%;
  object-fit: cover;
  background: #ddd;
}
.lv-byline__info { font-size: 14px; color: var(--lv-muted); line-height: 1.4; }
.lv-byline__info strong { color: var(--lv-dark); display: block; }
.lv-summary { font-size: 15px; color: #555; line-height: 1.7; margin-bottom: 12px; }
.lv-summary strong { color: var(--lv-dark); }

/* ── Listicle Items ──────────── */
.lv-item {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  align-items: center;
  padding: 48px 0;
  border-top: 1px solid var(--lv-border);
}
.lv-item--reverse .lv-item__img { order: 2; }
.lv-item--reverse .lv-item__text { order: 1; }

.lv-item__img {
  border-radius: var(--lv-radius);
  overflow: hidden;
  background: var(--lv-surface);
}
.lv-item__img img { width: 100%; aspect-ratio: 4/3; object-fit: cover; }
.lv-item__header {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 14px;
}
.lv-item__num {
  flex-shrink: 0;
  width: 36px; height: 36px;
  background: var(--lv-accent);
  color: var(--lv-dark);
  font-size: 16px; font-weight: 800;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}
.lv-item__header h2 {
  font-family: Inter, sans-serif;
  font-size: 22px; font-weight: 800; line-height: 1.3;
  color: var(--lv-dark);
}
.lv-item__text p { font-size: 15px; line-height: 1.7; color: #555; margin-bottom: 12px; }

/* Feature pills */
.lv-pills { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
.lv-pill {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--lv-accent-soft);
  border: 1px solid var(--lv-accent);
  border-radius: 100px;
  padding: 6px 14px;
  font-size: 12px; font-weight: 700; color: var(--lv-dark);
}
.lv-pill svg { width: 14px; height: 14px; color: var(--lv-star); }

/* ── Testimonial cards ───────── */
.lv-testimonial {
  background: var(--lv-dark);
  border-radius: var(--lv-radius);
  padding: 24px;
}
.lv-testimonial__stars { color: var(--lv-star); font-size: 16px; letter-spacing: 2px; margin-bottom: 10px; }
.lv-testimonial p {
  font-size: 14px; color: rgba(255,255,255,0.85);
  line-height: 1.6; font-style: italic; margin-bottom: 12px;
}
.lv-testimonial__author {
  display: inline-block;
  background: var(--lv-accent);
  color: var(--lv-dark);
  font-size: 12px; font-weight: 700;
  padding: 4px 12px; border-radius: 4px;
}

/* ── Mid CTA Banner ──────────── */
.lv-cta-banner {
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 0; border-radius: var(--lv-radius);
  overflow: hidden; margin: 48px 0;
  background: var(--lv-dark);
}
.lv-cta-banner__img img { width: 100%; height: 100%; object-fit: cover; }
.lv-cta-banner__content {
  display: flex; flex-direction: column; justify-content: center;
  padding: 40px; color: #fff;
}
.lv-cta-banner__content h2 {
  font-size: clamp(22px, 3vw, 30px); font-weight: 800;
  line-height: 1.25; margin-bottom: 24px;
}

/* ── Buttons ─────────────────── */
.lv-btn {
  display: inline-block;
  background: var(--lv-accent);
  color: var(--lv-dark);
  font-size: 15px; font-weight: 800;
  padding: 14px 32px; border-radius: 10px;
  text-align: center;
  transition: transform 0.2s, box-shadow 0.2s;
  border: none; cursor: pointer;
}
.lv-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.15);
  color: var(--lv-dark);
}

/* ── How It Works ────────────── */
.lv-how { padding: 60px 0; text-align: center; }
.lv-how__title {
  display: inline-block;
  background: var(--lv-accent);
  font-size: 22px; font-weight: 800;
  color: var(--lv-dark);
  padding: 12px 40px; border-radius: 100px;
  margin-bottom: 40px;
}
.lv-how__steps { display: flex; gap: 40px; justify-content: center; max-width: 600px; margin: 0 auto; }
.lv-how__step { flex: 1; text-align: center; }
.lv-how__icon {
  width: 64px; height: 64px;
  border: 2px dashed #ccc; border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 14px; font-size: 28px;
}
.lv-how__step p { font-size: 14px; color: #555; line-height: 1.5; font-style: italic; }

/* ── FAQ ─────────────────────── */
.lv-faq { padding: 60px 0; border-top: 1px solid var(--lv-border); }
.lv-faq h2 { font-size: 28px; font-weight: 800; text-align: center; margin-bottom: 32px; color: var(--lv-dark); }
.lv-faq__item { border-bottom: 1px solid var(--lv-border); }
.lv-faq__item summary {
  padding: 18px 0; font-size: 16px; font-weight: 700;
  color: var(--lv-dark); cursor: pointer; list-style: none;
  display: flex; justify-content: space-between; align-items: center;
}
.lv-faq__item summary::-webkit-details-marker { display: none; }
.lv-faq__item summary::after {
  content: '+'; width: 28px; height: 28px;
  background: var(--lv-accent); border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; font-weight: 400; flex-shrink: 0;
}
.lv-faq__item[open] summary::after { content: '\2212'; background: #fdd; color: #c00; }
.lv-faq__item p { padding: 0 0 18px; font-size: 15px; color: #666; line-height: 1.65; }

/* ── Sticky CTA Bar ─────────── */
.lv-sticky-cta {
  position: fixed; bottom: 0; left: 0; right: 0;
  z-index: 9999;
  transform: translateY(100%);
  transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  background: var(--lv-dark);
  border-top: 3px solid var(--lv-accent);
  box-shadow: 0 -4px 24px rgba(0,0,0,0.25);
}
.lv-sticky-cta--visible { transform: translateY(0); }
.lv-sticky-cta__inner {
  max-width: 900px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px 24px; gap: 16px;
}
.lv-sticky-cta__text { display: flex; flex-direction: column; gap: 2px; }
.lv-sticky-cta__badge {
  font-size: 11px; font-weight: 800; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--lv-accent);
}
.lv-sticky-cta__msg { font-size: 13px; font-weight: 600; color: rgba(255,255,255,0.8); }
.lv-sticky-cta__btns { display: flex; gap: 10px; flex-shrink: 0; }
.lv-sticky-cta__btn {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 14px; font-weight: 800;
  padding: 12px 22px; border-radius: 10px;
  text-decoration: none;
  transition: transform 0.2s, box-shadow 0.2s;
  white-space: nowrap; cursor: pointer;
}
.lv-sticky-cta__btn:hover { transform: translateY(-2px); }
.lv-sticky-cta__btn--primary {
  background: var(--lv-accent); color: var(--lv-dark);
}
.lv-sticky-cta__btn--primary:hover {
  box-shadow: 0 4px 16px rgba(0,0,0,0.2); color: var(--lv-dark);
}
.lv-sticky-cta__btn--secondary {
  background: #fff; color: var(--lv-dark);
  border: 2px solid rgba(255,255,255,0.3);
}
.lv-sticky-cta__btn--secondary:hover {
  box-shadow: 0 4px 16px rgba(255,255,255,0.3); color: var(--lv-dark);
}

/* ── Responsive ──────────────── */
@media (max-width: 700px) {
  .lv-item { grid-template-columns: 1fr; gap: 20px; }
  .lv-item--reverse .lv-item__img { order: 0; }
  .lv-item--reverse .lv-item__text { order: 0; }
  .lv-cta-banner { grid-template-columns: 1fr; }
  .lv-cta-banner__img { max-height: 250px; overflow: hidden; }
  .lv-cta-banner__content { padding: 28px; }
  .lv-how__steps { flex-direction: column; gap: 28px; }
  .lv-hero h1 { font-size: 28px; }

  .lv-sticky-cta__inner { flex-direction: column; padding: 10px 16px 14px; gap: 8px; }
  .lv-sticky-cta__text { flex-direction: row; align-items: center; gap: 8px; }
  .lv-sticky-cta__btns { width: 100%; }
  .lv-sticky-cta__btn { flex: 1; justify-content: center; font-size: 13px; padding: 12px 14px; }
  .lv-faq { padding-bottom: 100px; }
}

/* Bottom padding so sticky bar doesn't cover content */
.lv { padding-bottom: 80px; }
```
