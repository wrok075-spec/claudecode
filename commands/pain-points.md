Run a Scott Pain Point Analysis for a client's target market.

Client store URL or product page: $ARGUMENTS

## Process

1. **Scrape the client's top product page** using Firecrawl with `waitFor: 8000`. Extract all copy, claims, reviews, testimonials, FAQ, trust badges, pricing, social proof.

2. **Read brand files** — check `clients/{slug}/brand/icp-cards.md` and `brand-dna.md` for existing customer profiles and market context.

3. **Identify Top 20 Pain Points** — list them and confirm with user before proceeding to the full breakdown.

4. **Full Breakdown per Pain Point** — for each of the 20:

   ### Pain Point Feature
   One-line summary of the specific suffering.

   ### 3 Emotions
   First-person quotes capturing each emotion (internal monologue style):
   - "I feel like..."
   - "Why can't I just..."
   - "Nobody understands that..."

   ### 5 Deeper Causes
   The biological, psychological, cultural, social, and environmental root causes. Must include BOTH medical/biological AND psychological/social — never just one.

   ### Per Deeper Cause: 5 Dimensionalizations
   Vivid, specific, second-person scenarios ("You wake up and..."). Write in second person ("you") so the reader feels seen. Include cultural context specific to the market (Pakistani culture, Islam, joint family, food culture, etc. — adapt to actual market).

   ### Per Dimensionalization: 3 Identity Impacts
   How this changes who they see themselves as — not just behavior, but self-image. "You used to be the person who... now you're the person who..."

## Scale
20 pain points x 5 deeper causes x 5 dimensionalizations x 3 identity impacts = **1,500 identity-level insights**

## Output
Save to `clients/{slug}/research/pain-point-analysis.md`

## Why This Matters
This is the deepest customer empathy layer. It feeds:
- Ad copy that makes people feel "they're talking about ME"
- Product page copy that addresses the real objection beneath the stated objection
- Review response language
- Email sequences
- Landing page emotional architecture

The 1,500 identity impacts are the raw material for ALL persuasive copy downstream.
