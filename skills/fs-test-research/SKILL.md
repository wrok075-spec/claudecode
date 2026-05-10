---
name: fs-test-research
description: Run a Full-Stack CRO Test Research analysis on a product page.
---

Run a Full-Stack CRO Test Research analysis on a product page.

Product page URL: $ARGUMENTS

## Overview
This is the most comprehensive CRO testing analysis in the workflow. It produces a complete testing roadmap with 5 steps, covering every element on a product page — from headline to FAQ — with specific, actionable test variations backed by conversion psychology.

## Pre-requisites
- Scrape the full product page using Firecrawl with `waitFor: 8000` — extract ALL copy, pricing, claims, reviews, testimonials, FAQ, trust badges, social proof numbers, ingredients, guarantees, shipping info, bundles, CTAs, images, doctor endorsements, everything
- If client brand files exist, read `clients/{slug}/brand/brand-dna.md`, `brand-voice.md`, `icp-cards.md`
- If Shopify analytics or GA4 audit exists, reference conversion data for grounding test recommendations in real numbers

## STEP 1: IN-DEPTH PAGE ANALYSIS

Analyze the page across 5 dimensions. For each, identify specific issues and propose 3 tests per issue.

### 1. User Experience Flow
Analyze the page's conversion funnel structure (Hook → Problem → Solution → Evidence → Conversion). Identify friction points:
- Missing above-the-fold benefit headline (product name ≠ headline)
- Redundant content (e.g., ingredient list appearing twice)
- Inconsistent section labeling or formatting errors
- Missing sticky CTA for long-page scrollers
- Cart upsell messaging issues
- Navigation/scroll flow problems

For each friction point: describe the issue, explain why it hurts conversion, and propose 3 specific tests to fix it.

### 2. Content and Messaging
Analyze the copy, educational content, and messaging strategy:
- Is the core differentiator visualized or just text?
- Are there demographic-specific angles buried in the wrong place (e.g., menopause angle in FAQ instead of main page)?
- Does the skepticism-handling section provide verifiable proof or just empathy text?
- Is there a competitive comparison anywhere?
- Are benefits dimensionalized or generic?

For each issue: describe, explain impact, propose 3 tests.

### 3. Visual Elements
Analyze imagery, statistics presentation, and visual credibility:
- Does the gallery include lifestyle/demographic-specific imagery or just product shots?
- Are key statistics (success rates, review counts) text-only or visually amplified?
- Do endorsements have visual credibility markers (photos, badges, credentials)?
- Is there before/after or transformation imagery?

For each issue: describe, explain impact, propose 3 tests.

### 4. Offer and Value Proposition
Analyze pricing, bundles, guarantees, and value framing:
- Is pricing display clear and mathematically correct? (Flag contradictions immediately)
- Is there a cost comparison vs. buying ingredients separately?
- Do bundle options have strategic defaults and outcome-based naming?
- Is the guarantee prominently placed at the CTA?
- Is there a subscription option?

For each issue: describe, explain impact, propose 3 tests.

### 5. Call-to-Actions (CTAs)
Analyze all CTA buttons, urgency, and scarcity elements:
- Is CTA text generic ("Add to Cart") or benefit-driven?
- Are there urgency/scarcity signals near the purchase point?
- Is the guarantee directly beneath the CTA?
- Is social proof adjacent to the CTA?
- Is there an exit-intent recovery mechanism?

For each issue: describe, explain impact, propose 3 tests.

## STEP 2: FEATURES, BENEFITS, AND TESTING MATRIX

### Main Table
For EVERY key feature of the product (aim for 25-40 features), create a row with:

| Feature | Benefit | Benefit of the Benefit | Dimensionalized Benefit | Test Locations |

**Feature categories to cover:**
- Every individual ingredient/component and what it does
- Formula/formulation advantages (clinical dosing, form factor, flavor)
- Clean label claims (vegan, non-GMO, gluten-free, no artificial anything)
- Quality certifications (FDA-registered, GMP, 3rd-party tested)
- Guarantee and risk reversal
- Timeline/results claims
- Manufacturing origin (Made in USA, etc.)
- Social proof metrics (customer count, review count, success rate)
- Expert endorsements
- Core differentiator framework (e.g., "addresses 3 root causes")
- Transformation timeline
- Shipping/delivery
- Research/study backing
- Demographic-specific benefits (e.g., menopause, ADHD, age 40+)
- Bundle/pricing structure
- Caffeine-free or stimulant-free positioning

**Dimensionalized benefits** must be vivid, specific, second-person scenarios — not abstract. Example: "Remember why you walked into a room" not "improved memory."

### Step 2a: How to Use Benefit Recommendations
For EACH feature in the table, provide:
- **Location:** Where on the page to test this
- **What to Test:** The specific angle being compared
- **Test 1, 2, 3:** Three distinct test variations with different psychological angles (e.g., clinical vs. emotional vs. consequence-based)
- **Reason:** Why testing these angles matters for conversion

## STEP 3: RECOMMENDATIONS FOR TESTING WITH SEMANTIC SEPARATION

Identify **10 major page variables** to test. For each variable:

1. **Variable name and location**
2. **Reasoning for choosing this variable** — why it matters for conversion
3. **10 testing inputs** in a table:

| # | Variation | Emotional Trigger / Angle | Reasoning for Input |

- V1 is always the Control (current state)
- V2-V10 are semantically separated variations — each must test a DIFFERENT psychological angle, not just rewording the same idea
- Angles to cover across variations: problem identification, relief, social proof, curiosity, identity restoration, empowerment, fear of decline, scientific authority, demographic targeting, risk reversal, urgency, comparison

**The 10 variables should typically include:**
1. Main page headline
2. Sub-headline / supporting statement
3. Hero CTA button text
4. Social proof placement and format
5. Pricing display and bundle architecture
6. Problem/pain point section opening
7. Ingredient/feature section presentation format
8. Transformation timeline section
9. Trust/skepticism section
10. FAQ section design and placement

Adapt based on what's actually on the page.

## STEP 4: TOP 10 ITEMS TO TEST

The 10 highest-impact elements ranked by expected conversion lift. For each:

1. **Item name and location**
2. **Why this was chosen** — specific conversion impact reasoning
3. **6 variations** in a table (Control + 5 alternatives):

| Version | Content | Reasoning |

Each variation must be specific and implementable — exact copy, exact placement, exact visual description. No vague suggestions.

**Typical top 10 (adapt to page):**
1. Above-the-fold headline
2. Pricing display
3. CTA button text
4. Doctor/expert endorsement presentation
5. Bundle default selection and labeling
6. Demographic-specific content section (e.g., women's/age-specific)
7. Core differentiator visual (e.g., "3 root causes" diagram)
8. Social proof placement relative to CTA
9. Guarantee presentation at CTA
10. Urgency/scarcity elements

## STEP 5: LIST OF 20 TESTABLE VARIABLES

Expand to **20 testable variables** covering the full page. For each:

1. **Variable name and location**
2. **Why it should be tested** — specific reasoning
3. **5 variations** (Control + 4 alternatives)

| # | Variation |

**Variables should cover (adapt to actual page):**
1. Trust bar (top of page)
2. Hero bullet points order and content
3. Product gallery lead image
4. "Why everything else failed" section
5. Science/statistics visual format
6. Cart sidebar upsell messaging
7. Social proof claims (e.g., "Sold out X times")
8. Post-CTA trust icon bar
9. Timeline section labels and format
10. Ingredient section layout and placement
11. FAQ section conversion optimization
12. "Made in [Country]" badge treatment
13. Key ingredient framing for specific demographics
14. Problem/education section headline
15. Exit intent / last-chance element
16. Shipping speed messaging
17. Key statistic placement (e.g., "94% success rate")
18. Quality differentiator education (e.g., fruiting body vs. mycelium)
19. Bundle selector visual hierarchy
20. Mobile above-the-fold layout

## PRIORITY ACTION SUMMARY

End the analysis with a clear priority framework:

### Immediate Non-Negotiable Fixes
Table of critical errors that must be fixed BEFORE any testing begins (pricing errors, labeling inconsistencies, missing headlines, etc.)

### Highest-Impact Tests (20-50%+ Lift Expected)
Top 5 tests ranked by expected conversion impact with reasoning.

### Secondary High-Impact Tests (5-20% Lift Expected)
Tests 6-10 ranked with brief descriptions.

## WINNING TEST DATABASE CROSS-REFERENCE

Read `reference_winning_tests.md` from memory BEFORE starting the analysis. Throughout ALL 5 steps, actively cross-reference every recommendation against the winning test database:

**In Step 1 (Page Analysis):**
When identifying missing elements, check if any winning test covers that gap. Example: "No estimated delivery date on PDP — this is a winning test pattern that lifted RPV +13.7-19.4% across 4 clients (TC, Pittie, Black Oak, MJA)."

**In Step 3 (10 Variables) and Step 4 (Top 10 Items):**
When proposing variations, cite winning test data as supporting evidence. Example: "V3: Add USPs above the fold — winning test evidence: +23.1% RPV for B2D, +4.5% RPV for TC, won across 5 clients."

**In Step 5 (20 Variables):**
Tag each variable with its winning test match (if any):
- **DB Match:** [test name, RPV lift, clients] — if the pattern exists in the database
- **No DB Match** — if this is a page-specific recommendation without database backing

**In Priority Summary:**
Winning-test-backed recommendations get higher priority than recommendations based on CRO psychology alone. A recommendation that's backed by winning test data from 3+ clients is near-certain to work.

**Confidence tagging for every recommendation:**
- "Proven Winner" — matches a winning test that won for 3+ clients
- "High Confidence" — matches a winning test that won for 1-2 clients with >10% RPV lift
- "Theory-Based" — no winning test match, based on conversion psychology principles

## Rules
- Every recommendation must be based EXCLUSIVELY on actual content present on (or demonstrably absent from) the page. No hypothetical features or fabricated claims.
- Every test must be immediately actionable — exact copy, exact placement, exact visual description.
- If analytics data exists (GA4, ShopifyQL), reference specific numbers (bounce rate, ATC rate, CVR, AOV) to ground recommendations in real data.
- Cross-reference EVERY recommendation against the winning test database — if a match exists, cite it with RPV lift and client names.
- Flag critical errors (pricing contradictions, broken elements, trust-destroying issues) at the TOP of the analysis before anything else.
- Dimensionalized benefits must be vivid and second-person ("You wake up and..." not "improved cognitive function").
- Cover ALL buyer segments visible on the page (e.g., if there's a menopause angle, a men's angle, a professional angle — test for each).
- Include the full feature count (25-40 features) — don't skip ingredients or quality claims.

## Output
Save to `clients/{slug}/research/fs-test-research.md`

This is typically the longest single research deliverable in the workflow. It should be comprehensive enough that a CRO team can execute tests for 6-12 months from this single document.

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
