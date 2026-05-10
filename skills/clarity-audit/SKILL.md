# Microsoft Clarity CRO Audit

Analyze Microsoft Clarity heatmaps, session recordings, and behavioral data to identify UX issues and conversion blockers.

Client store and Clarity data: $ARGUMENTS

## Overview
Microsoft Clarity provides heatmaps (click, scroll, area), session recordings, and behavioral metrics (dead clicks, rage clicks, quick backs, excessive scrolling) that reveal WHERE users struggle on the site. This audit translates that behavioral data into specific CRO recommendations.

## Pre-requisites
- Client must have Microsoft Clarity installed on their Shopify store
- Client provides either:
  - **Option A:** Clarity dashboard access (email to add as viewer)
  - **Option B:** Screenshots/exports of key Clarity reports (heatmaps, scroll maps, dashboard metrics)
  - **Option C:** PDF export of Clarity insights

## What to Analyze

### 1. Dashboard Metrics
- **Dead clicks** — users clicking on non-clickable elements (indicates UX confusion)
- **Rage clicks** — rapid repeated clicks (indicates frustration)
- **Quick backs** — users who navigate to a page and immediately go back (indicates wrong content/expectations)
- **Excessive scrolling** — users scrolling up and down repeatedly (indicates they can't find what they need)
- **JavaScript errors** — broken functionality affecting conversion

### 2. Heatmaps (per page)
For each key page (Homepage, Collection, PDP, Cart), analyze:

**Click Heatmaps:**
- Where do users click most?
- Are they clicking non-clickable elements? (dead clicks = redesign needed)
- Is the ATC button getting clicks proportional to its importance?
- Are users clicking on images expecting them to do something?
- Are navigation elements getting ignored?

**Scroll Heatmaps:**
- What % of users reach the ATC button?
- What % reach reviews/testimonials?
- Where is the biggest scroll drop-off?
- Does content below the fold get seen?
- Are important trust signals below the scroll threshold?

**Area Heatmaps:**
- Which sections get the most engagement?
- Which sections are ignored entirely?
- Is the most important content in the most-engaged area?

### 3. Session Recordings (patterns to look for)
- Users scrolling past ATC without clicking
- Users going to FAQ/Science pages and not returning to PDP
- Users opening and closing the cart drawer without checking out
- Users toggling between pricing tiers repeatedly (pricing confusion)
- Users scrolling to reviews and then leaving (trust seeking behavior)
- Users on mobile struggling with specific elements (pinch zoom, misclicks)
- Users abandoning at specific checkout steps

### 4. Funnel Analysis (if available)
- Clarity's built-in funnel: which pages users visit before purchase
- Drop-off points in the conversion path
- Pages with highest exit rates
- Common navigation paths (do users follow the intended flow?)

## Report Structure

### Section 1: Cover
"Validare x [Brand] | Microsoft Clarity Behavioral Audit"

### Section 2: Executive Summary
- 3 callout boxes: biggest behavioral issues found
- Key metrics: dead clicks %, rage clicks %, scroll depth on PDP, quick back rate

### Section 3: Dead Click Analysis
- Table of pages with highest dead clicks
- What users are clicking that isn't clickable
- Recommendation for each (make it clickable, add visual feedback, or redesign)

### Section 4: Rage Click Analysis
- Where users rage click (specific elements)
- Why — slow loading, broken buttons, confusing UI
- Recommendations

### Section 5: Scroll Depth Analysis (per page)
For each key page:
- Scroll depth visualization (what % of users see each section)
- Where the biggest drop-off happens
- Cross-reference with content: is important content below the scroll threshold?
- Recommendation: move critical content above the drop-off point

### Section 6: Session Recording Insights
- Top 5 behavioral patterns observed
- Screenshots or descriptions of key moments (user confusion, abandonment triggers)
- Each pattern linked to a specific CRO recommendation

### Section 7: Mobile vs Desktop Behavior
- How mobile users interact differently
- Touch-specific issues (misclicks, pinch zoom, scroll jacking)
- Recommendations for mobile-specific fixes

### Section 8: Cross-Reference with Prior Research
**CRITICAL: Connect every Clarity finding to existing research**
- If dead clicks on pricing → link to FS Test "Fix Pricing Architecture"
- If scroll drop-off before ATC → link to Visual Audit "Sticky Mobile CTA"
- If rage clicks on reviews → link to recommendation for review app installation
- If quick backs from science pages → link to GA4 finding about Pages LP 0.30% CVR
- Use format: "Clarity confirms [finding]. We recommended [TEST X] in the [report name] to address this."

### Section 9: Priority Actions
Ranked table: Issue, Severity, Pages Affected, Recommended Fix, Cross-Reference

### Section 10: Summary Box
Top 3 behavioral fixes with expected impact

## Output
- HTML report matching Validare brand styling (same CSS as other reports)
- PDF: `{Brand}-Clarity-Audit-Validare.pdf` (portrait A4)
- Publish to here.now
- Save markdown to `clients/{slug}/research/clarity-audit.md`

## Rules
- ONLY analyze data the client provides — if no Clarity data available, tell the user what to export and how
- If Clarity is not installed, provide installation instructions: Settings → Integrations → add clarity.microsoft.com tracking script to theme.liquid
- Cross-reference EVERY finding with prior research (visual audit, FS tests, competitor analysis, GA4)
- Never fabricate heatmap data — only use what's provided
- Include screenshots from Clarity if the client provides them
- Branded as "Validare x [Brand]"
- No methodology terms — don't say "from Clarity session recordings", say "behavioral analysis shows"

## If Clarity Is Not Installed
Provide setup instructions:
1. Go to clarity.microsoft.com and create a free account
2. Create a new project for the store URL
3. Copy the tracking code
4. In Shopify Admin → Online Store → Themes → Edit Code → theme.liquid
5. Paste the Clarity tracking code before </head>
6. Wait 48-72 hours for data to accumulate
7. Then run this audit

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
