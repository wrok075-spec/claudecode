Generate a design brief combining GA data and brand research for a client.

Client: $ARGUMENTS

Ask the user to paste or attach:
1. The output from /ga-audit (analytics data)
2. The output from /research-client (brand research)

Then generate a structured design brief with:

## Client Overview
- Brand name, store URL, niche
- Target customer profile
- Current monthly sessions (from GA)
- Current conversion rate (from GA)

## What the Data Says
- Top 3 problems identified from GA (bounce rates, drop-off points, device issues)
- Top 3 problems from brand research (weak copy, missing trust signals, poor layout)

## Design Priorities (ranked)
1. **[Page/element]** — [why, what metric it affects, expected impact]
2. **[Page/element]** — [why]
3. **[Page/element]** — [why]

## Design Direction
- Visual style: [describe in 3 words, e.g. "clean, premium, direct"]
- Color palette to use: [from brand research]
- Fonts: [confirmed from CLAUDE.md or research]
- Tone: [benefit-first? urgency-driven? trust-focused?]

## Page-by-Page Scope
For each page being redesigned:
- Current problem (data-backed)
- What the new design must achieve
- Key elements to include (social proof, urgency, benefit strip, etc.)
- Success metric (what number should improve)

## What NOT to do
- [Design patterns that don't match the brand]
- [Things the client specifically wants to avoid]

## First Deliverable
What gets built first, and why.

Output this as a clean PDF-ready brief.

## Verification Rules (CRITICAL -- do not skip)

Before making ANY recommendation in this report:

1. **Verify the client's current site state.** Scrape or screenshot the live site before claiming a feature is missing. Never recommend something the client already has -- it destroys credibility instantly.
2. **Never claim something is "invisible" or "missing" without checking.** Reference actual screenshots or scrape data. If you can't verify, write "pending verification" instead of a false claim.
3. **Check current defaults before recommending default changes.** Always verify which variant, option, or layout is currently pre-selected or active before suggesting a change.
4. **Label screenshots accurately.** Cart drawer is not checkout. PDP is not landing page. Use the correct term for what the screenshot actually shows.
5. **PDF formatting.** Always include `@page{margin:40px 24px 24px 24px}` in print styles. Font size 11px minimum for print. Page breaks between major sections. `break-inside:avoid` on cards, tables, callouts. Never make print so compact it's unreadable.
