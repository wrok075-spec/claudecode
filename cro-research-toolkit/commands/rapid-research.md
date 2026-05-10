Run a deep product and customer analysis (Rapid Research) for a client.

Client product URL: $ARGUMENTS

## Process

1. **Scrape the product page** using Firecrawl with `waitFor: 8000`. Extract ALL copy, claims, reviews, testimonials, FAQ, trust badges, pricing, social proof numbers, ingredients, guarantees.

2. **Read brand files** if they exist — `clients/{slug}/brand/brand-dna.md`, `brand-voice.md`, `icp-cards.md`

3. **Generate all 8 sections** in a single comprehensive document:

### Section 1: Value Proposition Identification
Rank top 10 value props with:
- Real quotes from the page/reviews
- Market insights (why this matters in their niche)
- Marketing recommendations (how to amplify each)

### Section 2: Sentiment & Attitude Analysis
Top 10 customer sentiments (betrayal, fear, grief, hope, frustration, relief, pride, etc.) with:
- Emotional connection opportunities
- Copy angles that tap into each sentiment

### Section 3: Pain Point Exploration
Top 10 pain points with:
- Deeper fears/concerns beneath the surface pain
- Marketing strategies to address each

### Section 4: Objection Identification
Top 10 purchase objections ranked by urgency with:
- Why this objection exists
- Suggested response/copy to overcome it

### Section 5: Skepticism Drivers
Top 10 reasons customers don't trust yet with:
- Evidence from reviews/page
- Mitigation strategies (trust badges, guarantees, social proof, etc.)

### Section 6: Psychological Triggers
Top 10 triggers that compel purchase:
- Loss aversion, social proof, authority, scarcity, identity restoration, curiosity gap, reciprocity, etc.
- How to deploy each on the site

### Section 7: Imaginary Product Creation
10 product concepts born from the research:
- Bundles, formats, delivery systems, companion tools, premium programs
- For each: features, benefits, dimensionalized benefits, frequency of need

### Section 8: Product Origin Stories
Individual origin story graph for each imaginary product:
Problem → How It Got Worse → Why Everything Else Failed → Desperate Wish → Beginning Solution Journey → Almost Giving Up → Breakthrough Epiphany → Birth of Product

## Output
Save to `clients/{slug}/research/rapid-research.md`

## Why This Matters
This is the foundational intelligence layer that feeds EVERYTHING downstream — headline copy, USP selection, objection-handling in product descriptions, bundle strategy, pricing psychology, review slider quotes, trust badge selection, and CTA text. Without this, design decisions are guesswork.
