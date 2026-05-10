# Listicle Section Template

Annotated template for `sections/listicle-{slug}.liquid`. Customize the copy, product URLs, CDN images, and offer text per store.

## Structure

```liquid
{{ 'listicle-{slug}.css' | asset_url | stylesheet_tag }}

{%- assign product_url_primary = '/products/HANDLE-HERE' -%}
{%- assign product_url_secondary = '/products/HANDLE-HERE' -%}
{%- assign cdn = 'https://cdn.shopify.com/s/files/1/SHOP_ID/files/' -%}

{%- comment -%} Brand product images as fallback defaults {%- endcomment -%}
{%- assign img_1 = cdn | append: 'filename.png?v=VERSION' -%}
{%- assign img_2 = cdn | append: 'filename2.png?v=VERSION' -%}
{%- comment -%} ... define all image variables ... {%- endcomment -%}

<div class="lv">

  <!-- ══════ URGENCY BAR ══════ -->
  <div class="lv-urgency">
    OFFER TEXT HERE (match actual store offer)
    <div class="lv-countdown">
      <div class="lv-countdown__box" id="lv-hrs">02<small>hrs</small></div>
      <div class="lv-countdown__box" id="lv-min">15<small>min</small></div>
      <div class="lv-countdown__box" id="lv-sec">00<small>sec</small></div>
    </div>
  </div>

  <!-- ══════ HERO ══════ -->
  <div class="lv-container">
    <section class="lv-hero">
      <h1>X Reasons Why [Product] Is the #1 Way to [Outcome]</h1>
      <div class="lv-byline">
        {%- if section.settings.author_image != blank -%}
          <img class="lv-byline__avatar" src="{{ section.settings.author_image | image_url: width: 88 }}" alt="Author">
        {%- else -%}
          <div class="lv-byline__avatar"></div>
        {%- endif -%}
        <div class="lv-byline__info">
          <strong>by {{ shop.name }}</strong>
          Last Updated {{ 'now' | date: '%b %d, %Y' }}
        </div>
      </div>
      <p class="lv-summary"><strong>Summary:</strong> Hook paragraph here.</p>
      <p class="lv-summary"><em>Teaser line encouraging them to keep reading.</em></p>
    </section>

    <!-- ══════ ITEM 1 ══════ -->
    <article class="lv-item">
      <div class="lv-item__img">
        {%- if section.settings.image_1 != blank -%}
          <img src="{{ section.settings.image_1 | image_url: width: 800 }}" alt="..." loading="lazy">
        {%- else -%}
          <img src="{{ img_1 }}" alt="..." loading="lazy">
        {%- endif -%}
      </div>
      <div class="lv-item__text">
        <div class="lv-item__header">
          <span class="lv-item__num">1</span>
          <h2>Benefit-Led Headline</h2>
        </div>
        <p>Copy with <strong>bolded key takeaway</strong>.</p>
      </div>
    </article>

    <!-- ══════ ITEM 2 (reversed) ══════ -->
    <article class="lv-item lv-item--reverse">
      <div class="lv-item__img">
        {%- if section.settings.image_2 != blank -%}
          <img src="{{ section.settings.image_2 | image_url: width: 800 }}" alt="..." loading="lazy">
        {%- else -%}
          <img src="{{ img_2 }}" alt="..." loading="lazy">
        {%- endif -%}
      </div>
      <div class="lv-item__text">
        <div class="lv-item__header">
          <span class="lv-item__num">2</span>
          <h2>Second Benefit</h2>
        </div>
        <p>Copy here.</p>
        <!-- Optional: feature pills -->
        <div class="lv-pills">
          <span class="lv-pill">Feature 1</span>
          <span class="lv-pill">Feature 2</span>
        </div>
      </div>
    </article>

    <!-- ══════ TESTIMONIAL ══════ -->
    <div class="lv-testimonial">
      <div class="lv-testimonial__stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p>"Quote from real or realistic customer."</p>
      <span class="lv-testimonial__author">Name, Location</span>
    </div>

    <!-- Continue alternating items 3-5... -->
    <!-- Item 3: normal, Item 4: --reverse, Item 5: normal -->
  </div>

  <!-- ══════ MID CTA BANNER ══════ -->
  <div class="lv-container">
    <div class="lv-cta-banner">
      <div class="lv-cta-banner__img">
        {%- if section.settings.cta_image != blank -%}
          <img src="{{ section.settings.cta_image | image_url: width: 800 }}" alt="Product" loading="lazy">
        {%- else -%}
          <img src="{{ img_1 }}" alt="Product" loading="lazy">
        {%- endif -%}
      </div>
      <div class="lv-cta-banner__content">
        <h2>Try the #1 Rated [Product]</h2>
        <a href="{{ product_url_primary }}" class="lv-btn">Shop Now &rarr;</a>
        <!-- If dual variants: -->
        <a href="{{ product_url_secondary }}" class="lv-btn" style="margin-top:10px;">Shop [Variant] &rarr;</a>
      </div>
    </div>
  </div>

  <div class="lv-container">
    <!-- Continue items 6-10 (alternating) with testimonials between 7-8 -->

    <!-- ══════ HOW IT WORKS ══════ -->
    <section class="lv-how">
      <div class="lv-how__title">How It Works</div>
      <div class="lv-how__steps">
        <div class="lv-how__step">
          <div class="lv-how__icon">&#128075;</div>
          <p>Step 1 instruction</p>
        </div>
        <div class="lv-how__step">
          <div class="lv-how__icon">&#9201;</div>
          <p>Step 2 instruction</p>
        </div>
        <div class="lv-how__step">
          <div class="lv-how__icon">&#10024;</div>
          <p>Step 3 instruction</p>
        </div>
      </div>
    </section>

    <!-- ══════ FINAL CTA ══════ -->
    <div style="text-align:center;padding:20px 0 20px;">
      <a href="{{ product_url_primary }}" class="lv-btn" style="font-size:18px;padding:18px 48px;">Shop Now &rarr;</a>
      <p style="font-size:12px;color:#999;margin-top:10px;">Results guaranteed or Your Money Back</p>
    </div>

    <!-- ══════ FAQ ══════ -->
    <section class="lv-faq">
      <h2>Frequently Asked Questions</h2>
      <details class="lv-faq__item">
        <summary>Question 1?</summary>
        <p>Answer 1.</p>
      </details>
      <details class="lv-faq__item">
        <summary>Question 2?</summary>
        <p>Answer 2.</p>
      </details>
      <!-- 3-5 FAQ items total -->
    </section>
  </div>

</div>

<!-- ══════ STICKY CTA BAR ══════ -->
<div class="lv-sticky-cta" id="lv-sticky-cta">
  <div class="lv-sticky-cta__inner">
    <div class="lv-sticky-cta__text">
      <span class="lv-sticky-cta__badge">LIMITED OFFER</span>
      <span class="lv-sticky-cta__msg">Offer text here</span>
    </div>
    <div class="lv-sticky-cta__btns">
      <a href="{{ product_url_primary }}" class="lv-sticky-cta__btn lv-sticky-cta__btn--primary">
        Shop Now
      </a>
      <!-- If dual variants: -->
      <a href="{{ product_url_secondary }}" class="lv-sticky-cta__btn lv-sticky-cta__btn--secondary">
        Shop [Variant]
      </a>
    </div>
  </div>
</div>

<script>
(function(){
  /* ── Countdown timer (3-hour cycle) ── */
  function pad(n){return n<10?'0'+n:n}
  var total = (3*3600) - (Math.floor(Date.now()/1000) % (3*3600));
  function tick(){
    if(total<=0) total = 3*3600;
    var h=Math.floor(total/3600), m=Math.floor((total%3600)/60), s=total%60;
    var eH=document.getElementById('lv-hrs'), eM=document.getElementById('lv-min'), eS=document.getElementById('lv-sec');
    if(eH) eH.innerHTML=pad(h)+'<small>hrs</small>';
    if(eM) eM.innerHTML=pad(m)+'<small>min</small>';
    if(eS) eS.innerHTML=pad(s)+'<small>sec</small>';
    total--;
  }
  tick();
  setInterval(tick,1000);

  /* ── Sticky CTA: show after scrolling past hero ── */
  var stickyCta = document.getElementById('lv-sticky-cta');
  if (stickyCta) {
    var shown = false;
    var threshold = 400;
    function checkScroll() {
      var y = window.pageYOffset || document.documentElement.scrollTop;
      if (y > threshold && !shown) {
        stickyCta.classList.add('lv-sticky-cta--visible');
        shown = true;
      } else if (y <= threshold && shown) {
        stickyCta.classList.remove('lv-sticky-cta--visible');
        shown = false;
      }
    }
    window.addEventListener('scroll', checkScroll, { passive: true });
    checkScroll();
  }
})();
</script>

{% schema %}
{
  "name": "Listicle – [Product Name]",
  "tag": "section",
  "class": "listicle-section",
  "settings": [
    { "type": "header", "content": "Images (override defaults)" },
    { "type": "image_picker", "id": "author_image", "label": "Author avatar" },
    { "type": "image_picker", "id": "image_1", "label": "Image – Item 1" },
    { "type": "image_picker", "id": "image_2", "label": "Image – Item 2" },
    { "type": "image_picker", "id": "image_3", "label": "Image – Item 3" },
    { "type": "image_picker", "id": "image_4", "label": "Image – Item 4" },
    { "type": "image_picker", "id": "image_5", "label": "Image – Item 5" },
    { "type": "image_picker", "id": "cta_image", "label": "Mid-article CTA image" },
    { "type": "image_picker", "id": "image_6", "label": "Image – Item 6" },
    { "type": "image_picker", "id": "image_7", "label": "Image – Item 7" },
    { "type": "image_picker", "id": "image_8", "label": "Image – Item 8" },
    { "type": "image_picker", "id": "image_9", "label": "Image – Item 9" },
    { "type": "image_picker", "id": "image_10", "label": "Image – Item 10" }
  ]
}
{% endschema %}
```

## IP Geolocation Snippet

If the listicle needs a shipping estimate bar, use this pattern (also works as a standalone snippet at `snippets/shipping-estimate-inline.liquid`):

```liquid
<div class="lv-shipping-bar">
  <div class="lv-shipping-bar__left">
    <span class="lv-shipping-bar__dot"></span>
    Ships by <strong id="shipDate"></strong>
  </div>
  <div class="lv-shipping-bar__right">
    Free Shipping To <strong id="shipLoc"></strong>
  </div>
</div>

<script>
(function(){
  var d = new Date(), added = 0;
  while (added < 4) {
    d.setDate(d.getDate() + 1);
    if (d.getDay() !== 0 && d.getDay() !== 6) added++;
  }
  var dn = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
  var mn = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var el = document.getElementById('shipDate');
  if (el) el.textContent = dn[d.getDay()] + ', ' + mn[d.getMonth()] + ' ' + d.getDate();

  var locEl = document.getElementById('shipLoc');
  if (!locEl) return;

  function setLoc(region, country) {
    var loc = '';
    if (region && country) loc = region + ', ' + country;
    else if (country) loc = country;
    if (loc) locEl.textContent = loc;
    else locEl.textContent = 'Your Location';
  }

  fetch('https://ipwho.is/')
    .then(function(r) { return r.json(); })
    .then(function(data) {
      if (data.success !== false && (data.region || data.country)) {
        setLoc(data.region, data.country);
      } else { throw new Error('no data'); }
    })
    .catch(function() {
      fetch('https://ipapi.co/json/')
        .then(function(r) { return r.json(); })
        .then(function(data) { setLoc(data.region, data.country_name); })
        .catch(function() { locEl.textContent = 'Your Location'; });
    });
})();
</script>
```

**Important**: Use unique IDs if multiple shipping bars exist on the same page.
