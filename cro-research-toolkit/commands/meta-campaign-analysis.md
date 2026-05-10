Pull live campaign performance data from the Meta Ads API and deliver a full analysis with scaling recommendations.

Optional: campaign name filter or date range (e.g. "last 7 days", "Landing Page A/B"): $ARGUMENTS

## Connection

Read API credentials from the project `.env` file at the working directory root:
- `META_ACCESS_TOKEN`
- `META_AD_ACCOUNT_ID`

All API calls use the Facebook Graph API v21.0 via `curl`.

## Step 1: Pull Campaign Data

Fetch all campaigns:
```
GET /{ad_account_id}/campaigns?fields=name,status,objective,daily_budget,lifetime_budget,start_time,stop_time,buying_type
```

If `$ARGUMENTS` contains a campaign name filter, only analyze matching campaigns.

## Step 2: Pull Campaign-Level Insights

Fetch performance insights for all campaigns:
```
GET /{ad_account_id}/insights?fields=campaign_name,campaign_id,impressions,clicks,ctr,cpc,cpm,spend,actions,action_values,cost_per_action_type,purchase_roas,reach,frequency&level=campaign&date_preset=maximum&limit=50
```

If `$ARGUMENTS` specifies a date range, use the appropriate `date_preset` or `time_range` parameter:
- "today" → `date_preset=today`
- "yesterday" → `date_preset=yesterday`
- "last 7 days" → `date_preset=last_7d`
- "last 14 days" → `date_preset=last_14d`
- "last 30 days" → `date_preset=last_30d`
- "this month" → `date_preset=this_month`
- Custom range → `time_range={"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}`

Default: `date_preset=maximum` (all-time).

## Step 3: Pull Ad Set Data with Frequency

For each ACTIVE campaign, fetch ad set performance INCLUDING frequency:
```
GET /{campaign_id}/insights?fields=adset_name,adset_id,impressions,reach,frequency,spend,actions,action_values,cost_per_action_type,purchase_roas&level=adset&date_preset=maximum&limit=30
```

This is critical for the waterfall/funnel role analysis.

## Step 4: Pull Ad-Level Data for Active Campaigns

For each ACTIVE campaign, fetch ad-level performance:
```
GET /{campaign_id}/insights?fields=ad_name,ad_id,impressions,clicks,ctr,cpc,spend,actions,action_values,cost_per_action_type,purchase_roas&level=ad&date_preset=maximum&limit=50
```

## Step 4b: Pull 7-Day Click Attribution

For each ACTIVE campaign, also fetch 7-day click attribution separately:
```
GET /{campaign_id}/insights?fields=campaign_name,actions,action_values&level=campaign&date_preset=maximum&action_attribution_windows=["7d_click"]&limit=50
```

Compare 7-day click purchases against the default attribution. If 1-day view conversions exceed 10% of 7-day click conversions, flag it — the ROAS may be inflated.

## Step 5: Extract Key Metrics

From the raw API data, extract these metrics per campaign:

| Metric | Source |
|---|---|
| Spend | `spend` |
| Impressions | `impressions` |
| Reach | `reach` |
| Frequency | `frequency` |
| Link Clicks | `actions` where `action_type = "link_click"` |
| CTR | `ctr` |
| CPC | `cpc` |
| CPM | `cpm` |
| Landing Page Views | `actions` where `action_type = "landing_page_view"` |
| Add to Carts | `actions` where `action_type = "add_to_cart"` |
| Initiate Checkouts | `actions` where `action_type = "initiate_checkout"` |
| Purchases | `actions` where `action_type = "purchase"` |
| Purchase Revenue | `action_values` where `action_type = "purchase"` |
| ROAS | `purchase_roas` where `action_type = "omni_purchase"` |
| Cost per Purchase | `cost_per_action_type` where `action_type = "purchase"` |
| Cost per ATC | `cost_per_action_type` where `action_type = "add_to_cart"` |
| Cost per IC | `cost_per_action_type` where `action_type = "initiate_checkout"` |

## Step 6: Calculate Derived Metrics

For each campaign with purchases:
- **AOV** = Purchase Revenue / Purchases
- **LP-to-ATC Rate** = ATCs / Landing Page Views
- **ATC-to-IC Rate** = Initiate Checkouts / ATCs
- **IC-to-Purchase Rate** = Purchases / Initiate Checkouts
- **LP-to-Purchase Rate** = Purchases / Landing Page Views

Account-level totals:
- Total spend, total revenue, total purchases
- Blended ROAS = Total Revenue / Total Spend
- Blended CPA = Total Spend / Total Purchases
- Blended AOV = Total Revenue / Total Purchases

### Profit Per Visitor (CRITICAL)

COGS per unit = $15 (product + packaging + fulfillment)

For each campaign and the account overall:
- **Gross Profit** = Revenue - (COGS × Purchases) - Ad Spend
- **Profit per Visitor** = Gross Profit / Landing Page Views
- **True Break-even CPA** = AOV - COGS (e.g., $37 AOV - $15 COGS = $22 max CPA)
- **True Break-even ROAS** = AOV / (AOV - COGS) (e.g., $37 / $22 = 1.68x)

Always show profit per visitor in the Account Overview table. A negative profit per visitor means the campaign is losing money even if ROAS looks "above 1x."

## Step 7: Deliver Analysis

Present the analysis in this exact structure:

### 1. Account Overview Table
Single table with: Total Spend, Total Revenue, Total Purchases, Blended ROAS, Blended CPA, Blended AOV.

### 2. Campaign Breakdown Table
All campaigns ranked by spend, showing: Campaign Name, Status, Budget/Day, Spend, Purchases, Revenue, ROAS, CPA.

### 3. Active Campaign Deep Dive
For each ACTIVE campaign:
- Ad set breakdown with targeting details
- Ad-level performance if available
- Which ad sets / ads are winning vs losing

### 3b. Frequency & Funnel Role Analysis (CRITICAL)
For each ad set, show frequency and classify its funnel role:
- **Frequency < 1.5** = Top of funnel "hunter" — bringing NEW people into the funnel
- **Frequency 1.5-2.5** = Mid funnel — re-engaging warm audiences
- **Frequency > 2.5** = Bottom funnel or fatiguing — showing to same people repeatedly

**The Waterfall Rule:** Do NOT recommend pausing an ad set just because it has high CPA. If its frequency is low (<1.5), it may be a top-of-funnel hunter feeding conversions to other ad sets. Pausing it creates a "waterfall effect" that tanks overall performance.

**Only recommend pausing when:**
- High frequency (>2.5) AND high CPA → true fatigue
- Zero engagement (0 clicks, 0 LPVs) after $20+ spend → creative is dead
- NOT just because CPA is above target with low frequency

### 3c. Attribution Check
Compare 7-day click conversions to overall conversions. If 1-day view makes up >10% of total purchases, flag it — the reported ROAS may be inflated by people who would have bought anyway (email, organic, Google).

### 4. Funnel Analysis
For campaigns with purchase data:
- LP View → ATC → IC → Purchase conversion rates
- Where the biggest drop-offs are happening
- Compare funnel rates across campaigns

### 5. Key Problems
Bullet list of critical issues found:
- Campaigns burning budget with zero purchases
- ROAS below 1x (losing money)
- AOV vs CPA mismatch
- High frequency (audience fatigue)
- Poor CTR (creative fatigue)
- Funnel leakage points

### 6. Scaling Recommendations
Actionable recommendations based on the data:
- What to scale (campaigns/ad sets with strong signals)
- What to kill (campaigns/ad sets bleeding money)
- Budget allocation suggestions
- Targeting adjustments
- Creative/funnel fixes needed before scaling

## Rules

- All dollar amounts in the API are in cents (divide by 100 for display) — EXCEPT `spend` and `action_values` which are already in dollars
- Daily budgets from the API are in cents — divide by 100
- Never fabricate data — only report what the API returns
- If the access token is expired, tell the user and suggest they refresh it
- If a campaign has no insights data, note it as "No data / no spend"
- Be direct and opinionated in the analysis — flag what's working and what's not
- Compare campaigns against each other to identify relative winners
- Always calculate and show the funnel conversion rates — this is where the real insights are
