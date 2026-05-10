Meta Ads Playbook — living document of everything learned about running Facebook/Instagram ads. Updated automatically whenever new strategies, frameworks, or learnings are shared.

Last updated: 2026-05-10

$ARGUMENTS

If the user shares a new learning, transcript, screenshot, or strategy — add it to the relevant section below and confirm what was added. If the user asks a question about Meta ads, answer using this playbook as the knowledge base.

---

## Campaign Structure

### The Setup
- **CBO (Campaign Budget Optimization)** — budget at campaign level, not ad set level. Meta decides how to allocate.
- Run multiple campaign types simultaneously:
  - **tCPA (Cost Cap)** — target cost per purchase. Main scaling campaign.
  - **tROAS (Min ROAS)** — target return on ad spend. Optimizes for revenue, prioritizes high-AOV buyers.
  - **DPA (Dynamic Product Ads)** — catalog-based retargeting. Shows products people viewed but didn't buy.
  - **Lowest Cost** — no cap, spends everything. Use for testing/discovery only.

### Campaign Roles
| Campaign | Purpose | Budget |
|---|---|---|
| tCPA (Cost Cap) | Main scaling — find buyers at target CPA | 60-70% of budget |
| tROAS (Min ROAS) | Revenue optimization — prioritize bundle/high-AOV buyers | 20-30% of budget |
| DPA Retargeting | Re-engage site visitors who didn't buy | 5-10% of budget |
| Lowest Cost | Test new creatives in isolation | Small fixed budget ($20-30/day) |

### Bid Strategies Explained
| Strategy | How It Works | When to Use |
|---|---|---|
| **Cost Cap (tCPA)** | Sets target CPA. Meta averages around it over 7 days. May go above on some days. | Scaling profitably. Main campaign. |
| **Min ROAS (tROAS)** | Sets minimum ROAS target. Meta only spends when it expects to hit that return. | When you want to optimize for revenue, not just conversions. Higher AOV buyers prioritized. |
| **Bid Cap** | Hard maximum bid per auction. Never exceeds. Very restrictive. | Advanced. High-volume accounts with tight unit economics. |
| **Lowest Cost** | Spends full budget every day. Gets cheapest results possible but no CPA limit. | Testing new creatives. Discovery phase. |

---

## The Waterfall Effect

Every ad set in a CBO plays a funnel role. They work TOGETHER, not in isolation.

### How It Works
- **Low frequency + high spend** = top of funnel "hunter." Going out finding NEW people. May have high CPA — that's OK.
- **Low frequency + low spend** = hunter with less reach. Still prospecting.
- **High frequency + low CPA** = bottom of funnel converter. Cheap CPA BECAUSE the hunters feed it warm audiences.
- **High frequency + high CPA** = fatiguing. The only scenario to consider pausing.

### The Rule
**NEVER pause an ad set just because it has high CPA.** Check frequency first.
- Frequency < 1.5 → it's a hunter, KEEP IT
- Frequency 1.5-2.5 → mid funnel, monitor
- Frequency > 2.5 → possibly fatiguing, consider pausing IF CPA is also high

Killing a hunter creates a "waterfall" — the whole campaign tanks because the top-of-funnel feeder is gone. Other ad sets that looked cheap will get more expensive because they lost their audience supply.

### What the Expert Said
> "The more you try to milk individual ad sets, the worse your campaign performs."
> "Each ad set plays a role in the funnel. Some are hunters, some are converters."
> "If you look at an ad set with $80 CPA and your target is $60, and you turn it off — your whole account tanks."

---

## Frequency

### From the PMVM Paper
- **eCommerce needs 5-7 exposures** (Actionable Frequency Floor) before a cold person buys
- Below AFF = near-zero conversion. NOT proportional — it's a threshold. Spending half the budget doesn't give half the conversions, it gives ZERO.
- **Frequency velocity matters** — 5 exposures in 7 days > 5 exposures in 30 days. Compressed delivery builds cognitive momentum.
- Multiple ad sets in CBO = natural frequency building. Each ad set alone might be 1.2 freq, but combined per-user frequency across ALL ad sets is higher.

### Frequency Is NOT Always Bad
- High frequency for RETARGETING = good (showing ads to warm audiences multiple times drives conversion)
- High frequency for COLD audiences with one creative = bad (fatigue)
- The distinction: are you reaching NEW people or hammering the SAME people?

### Monitoring
- Track frequency at the ad set level, not campaign level
- 30-day window for frequency assessment
- Under 2.0 over 30 days = healthy for cold prospecting
- Over 3.0 = needs fresh creative or audience expansion

---

## Creative Strategy

### Creative > Everything
> "You can have the sexiest best ad structure. It's irrelevant. What is relevant is whether your content is good."

- Campaign structure, bid strategy, targeting — all secondary
- If only one ad set gets spend, your content isn't diverse enough
- The path to scale: more good creatives = more distributed spend = more total volume

### Volume
- The $3M/week brand has **800 ads live** across 5 campaigns
- Not all get spend — that's the point. Meta picks winners.
- Weekly cadence: launch 10-15 new ads per week

### The Scaling Loop
```
1. Find the top SPENDER (not highest ROAS)
2. Reverse-engineer WHY it works (hook, structure, mechanism, emotion)
3. Create hook variations (same body, different first 5 seconds)
4. Test hooks → find the super winner
5. Add new ad sets weekly with fresh content
6. Repeat
```

### Why the Top Spender Matters
- Scale based on the ad getting the MOST spend, not highest ROAS
- Meta already decided it's the best performer by giving it budget
- A $1000-spend ad at 2.2x ROAS > a $100-spend ad at 3.5x ROAS
- The high-spend ad has proven it holds under scale pressure

### Hook > Body
- The biggest gains come from new hooks, not new bodies
- Keep the body constant, create multiple hook angles
- Each hook unlocks a different audience segment
- Average watch time on winning video: 12 seconds on a 2-min video — the hook decides everything

### What Makes a Winning Creative
From the Jaxster video analysis:
- **Hook in 1.5 seconds** — show the problem immediately
- **Demo-first format** — the product IS the content
- **Full transparency** — show everything (mixing, applying, waiting, rinsing, result)
- **Mechanism** — make it sound scientific/professional ("two compartments, activator and color")
- **Objection handling in real-time** — prove no stain, no smell during the demo
- **Genuine reaction** — not scripted hype
- **Long-form works** — Meta loves watch time. 60-120 second videos that hold attention outperform short clips

### Creative Diversity
- Don't iterate ONE ad endlessly — that consolidates spend into one pocket
- Post-Andromeda, Meta reads content and matches it to audience segments
- You don't want all spend going to one "pocket" of your audience
- Different creatives reach different audience segments = broader reach

### Andromeda Update (Don't Overthink It)
> "People need to shut the fuck up about Andromeda."
- Still test multiple hooks per video
- Still make headline variations on static ads
- Small iterations (different hook, same body) still work
- Creative diversification comes from different BATCHES, not just within one ad

---

## Ad Set Management

### Weekly Rhythm
- **Monday:** Review last week's data
- **Tuesday:** Launch 1-2 new ad sets with fresh content
- **Rest of week:** Hands off, let it run

### New Content = New Ad Set
- Everything launched is a new ad set
- Don't add new ads to existing ad sets
- 10-15 ads per ad set — let Meta find the winner within

### Duplicating Across Strategies
- Run the SAME creatives in both tCPA and tROAS campaigns
- Different optimization objectives find different audiences
- A creative that doesn't convert under tCPA might work under tROAS

### Don't Touch the Account
> "The more you touch it, the worse it performs."
- Set CBO + cost cap → upload content → hands off
- Human emotion is the enemy of performance
- Don't try to "milk" individual ad sets
- Don't set minimum spend rules on ad sets with good CPA
- Cost caps force you to focus on content quality — if it's not spending, make better ads

---

## Cost Caps

### How They Work
- You set a cost per result goal
- On a 7-day window, Meta does its best to hit that goal
- It's an AVERAGE target, not a hard ceiling — some days above, some below
- If Meta can't find buyers at your cap, it underspends — that's the signal

### Setting the Right Cap
- True break-even CPA = AOV - COGS
- Set cost cap AT or slightly ABOVE true break-even
- Don't set it too tight — restricts spend volume
- Don't gradually increase it — you're training the algorithm to find more expensive buyers

### If Cost Cap Won't Spend
> "The answer is make better ads. Stop trying to force the algorithm to do something it's telling you it can't do."
- Don't raise the cap
- Don't force spend
- Make better content — higher hook rate = more natural spend
- Meta wants to provide good user experience — if people watch your ad, it spends more

---

## Attribution

### 7-Day Click vs 1-Day View
- **7-day click** = someone clicked your ad and bought within 7 days. THIS IS YOUR REAL DATA.
- **1-day view** = someone SAW your ad and bought within 1 day. Could be from email, Google, direct — inflates ROAS.
- If 1-day view > 10% of total purchases, your ROAS is inflated
- Always check custom columns → Attribution Settings → 7-day click, 1-day view
- Scale decisions should be based on 7-day click data, not blended

### What the Expert Said
> "What you do NOT want to be seeing is your one day view conversions exceeding more than say just above 10% of your 7-day click conversions."
> "Try not to scale based on one day view data because your CAC will look really good as you scale, but it's not actually that good. You're just burning money for no reason."

---

## Profit Per Visitor

### The Only Metric That Matters
```
Gross Profit = Revenue - (COGS × Purchases) - Ad Spend
Profit per Visitor = Gross Profit / Landing Page Views
True Break-even CPA = AOV - COGS
True Break-even ROAS = AOV / (AOV - COGS)
```

- ROAS of 1.25x LOOKS profitable but ISN'T when you factor in COGS
- A negative profit per visitor means losing money even if ROAS is "above 1x"
- The two levers: lower CPA (better creatives) or higher AOV (bundles, subscription)

### Cost to Warm (from PMVM Paper)
- **CTW** = money spent showing ads to people who aren't ready to buy yet
- **CTC** = the final push to purchase
- CPA = CTW + CTC blended together
- Hunter ad sets = pure CTW investment
- Spending below the frequency threshold = structurally zero conversions

---

## Unit Economics & Subscription

### First Purchase Is NOT Where You Make Money
> "Facebook is not where you make your money. It's where you acquire a customer. How you handle the back end is where you make money."

- One-time buyers at current CPAs are structurally non-viable for most DTC brands
- LTV through subscription/repeat purchase is the only viable model
- The goal: acquire subscribers, not one-time buyers
- Can afford to LOSE money on first purchase if subscriber rate is >15%

### Viability Ratio (from PMVM Paper)
- LTV:CAC ratio of 3:1+ = structurally sound
- 1:1 to 3:1 = marginal, needs organic/retention channels
- Below 1:1 = structurally non-viable

### Subscription Math Example
| Customer Type | CPA | Revenue (6mo) | COGS (6mo) | Profit |
|---|---|---|---|---|
| One-time buyer | $30 | $37 | $15 | -$8 |
| Subscriber | $30 | $222 | $90 | +$102 |

---

## AOV Optimization

### Levers
- **Bundle pricing** — 2-pack and 3-pack with volume discounts
- **Shipping threshold** — charge shipping on single bottles, free on 2+
- **Free gifts** — unlock gifts at higher tiers (powder at 2-pack, stick at 3-pack)
- **Default selection** — pre-select the 2-pack as "Most Popular"
- **Subscription** — subscribe & get free gifts + auto-delivery
- **Post-purchase upsell** — "Add another bottle for $X" after checkout

### Bundle Psychology
- 1-pack should feel like the "starter" option, not the default
- 2-pack should be the obvious choice (Most Popular badge, best value perception)
- 3-pack should be for serious buyers (Best Value badge, most gifts)
- Show per-bottle price to make bundles look cheaper
- Show total savings percentage prominently

---

## Landing Page Testing

### The Right Way
- Same creative, same audience, same budget — only the LP URL changes
- Test within the SAME CBO campaign as duplicate ad sets
- Measure: LP→ATC rate, AOV, profit per visitor, subscriber rate

### Why Listicles Work (from PMVM Paper)
- Cold audiences need 5-7 exposures before buying
- A listicle compresses multiple "exposures" into one page visit
- Each section (problem, social proof, mechanism, testimonials, comparison) = another exposure
- Accelerates the frequency curve within a single session
- Higher conversion rates than PDPs for cold traffic

### Pages to Test
- PDP (product detail page) — assumes visitor already trusts you
- Listicle — long-form editorial, builds trust from scratch
- Advertorial — native article format, problem → solution → product
- Bundle-only — no single bottle option, forces bundle purchase

---

## Retargeting (DPA)

### What It Is
- Dynamic Product Ads — catalog-based retargeting
- Auto-generates ads showing products people viewed but didn't buy
- Targets warm audiences — people who already visited your site

### Setup
- Requires product catalog synced between Shopify and Meta
- Shopify Admin → Sales Channels → Facebook & Instagram app
- Audience: site visitors last 7-14 days who didn't purchase
- Budget: $20-30/day (small — retargeting doesn't need much)
- Usually highest ROAS campaign because audience is warm

---

## Checkout Optimization

### Abandonment
- 60%+ of people who start checkout abandon
- Set up abandoned checkout emails (Shopify built-in or Klaviyo)
- Even 10% recovery = free revenue at zero ad cost
- Biggest causes: shipping cost surprise, lack of trust signals, payment friction

---

## Common Mistakes

1. **Killing ad sets based on CPA alone** — check frequency first. Low-frequency high-CPA = hunter, not failure.
2. **Thinking 1x ROAS = profitable** — forgot COGS. True break-even is usually 1.5-2x.
3. **Touching the account daily** — set and forget. Weekly creative refreshes only.
4. **Only running one bid strategy** — use tCPA AND tROAS simultaneously.
5. **Too few creatives** — can't scale with 5-10 ads. Need 50+ for real scale, 800+ for $3M/week.
6. **Scaling by raising budget** — scale by adding more winning creatives, not increasing budget on one.
7. **Raising cost caps to force spend** — trains algorithm to find expensive buyers. Make better ads instead.
8. **Ignoring 1-day view inflation** — always check 7-day click attribution.
9. **No subscription/LTV strategy** — first-purchase profit is dead. LTV is everything.
10. **No retargeting** — easiest ROAS campaign. DPA catches people who didn't buy on first visit.

---

## Key Quotes

> "If you're running cost caps and it only spends a thousand bucks, it's spending that thousand for a reason. The reason is it can't find enough buyers at that budget. Stop trying to force the algorithm."

> "The more you touch it, the more you try to milk as much money out of all these individual ads, the worse your campaign is going to perform."

> "If you have good content, it's well thought out, then you can use CBO and get a lot of spend."

> "An ad not getting spend tells just as much as one that spent unprofitably."

> "Everything launched is a new ad set. Launching 10-15 ads per ad set."

> "Spending half the required CTW does not produce half the conversions; it produces approximately zero conversions."

> "Facebook is not where you make your money. It's where you acquire a customer."

---

## Update Instructions

When new Meta ads learnings are shared (transcripts, screenshots, strategies):
1. Extract the key insights
2. Add them to the relevant section above
3. If it's a new topic, create a new section
4. Add any new quotes to the Key Quotes section
5. Update the "Last updated" date at the top
6. Confirm to the user what was added
