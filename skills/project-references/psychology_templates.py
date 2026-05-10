#!/usr/bin/env python3
"""
60 Reusable Ad Templates — Psychology + Frustration — All Products

These templates are product-agnostic. Each uses placeholder variables:
  {PRODUCT}     — short product name (e.g., "Hair Color Shampoo", "Hair Styling Powder")
  {BRAND}       — brand name (e.g., "KIWINZ PROFESSIONAL")
  {HERO}        — the product reference string (e.g., "the bottle (described above)")
  {PRICE}       — product price (e.g., "$29")
  {TIME}        — application time (e.g., "15 minutes", "10 seconds")
  {BENEFIT_1}   — primary benefit (e.g., "100% grey coverage", "instant volume")
  {BENEFIT_2}   — secondary benefit (e.g., "ammonia-free", "matte finish")
  {BENEFIT_3}   — tertiary benefit (e.g., "argan oil + keratin", "all-day hold")
  {BENEFIT_4}   — fourth benefit (e.g., "no skin staining", "non-greasy")
  {COMPETITOR}  — what the product replaces (e.g., "box dye", "hair gel")
  {COMP_TIME}   — competitor time (e.g., "45 minutes", "re-apply every 2 hours")
  {COMP_PRICE}  — competitor price (e.g., "$150 salon visit", "$18 gel")
  {AUDIENCE}    — target audience (e.g., "men", "women", "men and women")
  {STAT_USERS}  — user count (e.g., "200,000+", "50,000+")
  {REVIEW_NAME} — review name (e.g., "Marcus T., 49", "Jake M., 28")
  {REVIEW_TEXT} — review quote
  {PALETTE_BG}  — primary background color (e.g., "cream #EBDFCB", "matte black #1A1A1A")
  {PALETTE_ACCENT} — accent color (e.g., "gold #B8884A", "yellow #F1CC19")
  {PALETTE_TEXT}    — text color (e.g., "espresso #3B2718", "white #FFFFFF")

Usage:
  from psychology_templates import TEMPLATES
  # Fill in product-specific variables and merge with your prompts list
"""

TEMPLATES = [

# ─── SECTION A: VALUE PROPOSITION ADS (1-10) ───

(1, "salon-math-calculator", True,
 "Use the attached image as brand reference. Match the exact product structure precisely. "
 "Create a financial comparison ad on a clean {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT} headline reading \"THE SALON MATH NOBODY TALKS ABOUT.\" "
 "Center: a large, clean infographic-style calculation in bold {PALETTE_TEXT} text, each line on its own row like a receipt: "
 "\"{COMP_PRICE}: $150\" "
 "\"× 8 visits per year\" "
 "\"= $1,200/year\" "
 "A thick {PALETTE_ACCENT} horizontal divider line. "
 "\"{BRAND}: {PRICE}/bottle\" "
 "\"× 6 bottles per year\" "
 "\"= $174/year\" "
 "Below: massive bold {PALETTE_ACCENT} text reading \"YOU SAVE $1,026 EVERY YEAR.\" "
 "Bottom right: {HERO} small, clean studio light. "
 "Bottom left: five gold stars and \"Same results. Your shower. Your schedule.\" "
 "1:1 aspect ratio."),

(2, "speed-split-comparison", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a time-comparison split ad divided vertically. "
 "LEFT HALF: muted grey background. An hourglass timer showing {COMP_TIME}. "
 "Below: stressed man in bathroom surrounded by {COMPETITOR} supplies — gloves, mixing bowls, stained towels. "
 "Red text: \"{COMP_TIME} of mess.\" "
 "RIGHT HALF: warm {PALETTE_BG} background. A simple clock showing {TIME}. "
 "Below: same man, relaxed, casually using {HERO} in the shower. "
 "{PALETTE_ACCENT} text: \"{TIME} of shampoo.\" "
 "Top center spanning both: bold white text on dark bar: \"SAME RESULT. FRACTION OF THE TIME.\" "
 "1:1 aspect ratio."),

(3, "ingredient-transparency", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a clean-formula trust ad on a clean white background. "
 "Top: bold {PALETTE_TEXT} headline: \"WHAT'S NOT IN IT MATTERS AS MUCH AS WHAT IS.\" "
 "Left column labeled \"WHAT'S NOT IN IT\" with red X icons: "
 "\"Ammonia\", \"Harsh Chemicals\", \"Parabens\", \"Synthetic Fragrances\", \"Skin-Staining Agents\". "
 "Right column labeled \"WHAT IS IN IT\" with green checkmarks: "
 "\"{BENEFIT_3}\", \"Natural Color Pigments\", \"Moisturizing Complex\", \"Scalp-Safe Formula\", \"Pleasant Scent\". "
 "Bottom center: {HERO} with soft studio lighting. "
 "Small text: \"Read every ingredient at kiwinzprofessional.com\" "
 "1:1 aspect ratio."),

(4, "simplicity-is-luxury", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a minimalist simplicity ad on clean {PALETTE_BG} background. "
 "Top: elegant italic serif in {PALETTE_TEXT}: \"The most sophisticated thing about {BRAND}\" "
 "Below in massive bold uppercase: \"IS HOW SIMPLE IT IS.\" "
 "Center: three large numbered steps in {PALETTE_ACCENT} circles with bold {PALETTE_TEXT} text: "
 "\"1. APPLY\" — \"2. WAIT {TIME}\" — \"3. RINSE\" "
 "Below: smaller text: \"No mixing. No gloves. No mess. No salon appointment.\" "
 "Bottom: {HERO} centered, elegant studio lighting. Generous white space. "
 "Small {BRAND} wordmark bottom right. 1:1 aspect ratio."),

(5, "multi-benefit-stack", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a benefit-stacking ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT} headline: \"ONE BOTTLE REPLACES YOUR ENTIRE ROUTINE.\" "
 "Center: {HERO} large, hero-lit. "
 "Five {PALETTE_ACCENT} horizontal lines extending outward to five benefit cards: "
 "Card 1: icon + \"{BENEFIT_1}\" + supporting detail "
 "Card 2: icon + \"{BENEFIT_2}\" + supporting detail "
 "Card 3: icon + \"{BENEFIT_3}\" + supporting detail "
 "Card 4: icon + \"{BENEFIT_4}\" + supporting detail "
 "Card 5: icon + \"Smells Great\" + supporting detail "
 "Bottom: five gold stars + \"One product. Five jobs. Zero compromise.\" "
 "1:1 aspect ratio."),

(6, "natural-look-guarantee", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a natural-result reassurance ad. "
 "Full frame: close-up portrait of a man in his late 40s with rich, natural-looking dark hair — "
 "subtle depth and variation between strands, healthy shine, zero flat helmet look. "
 "Warm natural window light, shot on 85mm f/1.8. "
 "The hair looks so natural that the viewer's first thought is 'good genes, not good product.' "
 "Large bold white text overlaid: \"NOBODY WILL KNOW.\" "
 "Below in smaller white: \"They'll just think you look great. That's the point.\" "
 "Bottom: {HERO} small, corner. Five gold stars. "
 "1:1 aspect ratio."),

(7, "cost-per-use-breakdown", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a value-math ad on dark {PALETTE_TEXT} background. "
 "Top: bold white headline: \"WHAT {PRICE} ACTUALLY GETS YOU.\" "
 "Center: a vertical list showing cost-per-use math: "
 "\"1 bottle = ~6 applications\" "
 "\"That's {PRICE} ÷ 6 = less than $5 per use\" "
 "\"vs. {COMP_PRICE} per salon visit\" "
 "\"vs. $18 per box dye kit\" "
 "Each line with a large bold price number in {PALETTE_ACCENT}. "
 "Bottom: {HERO} centered. Bold {PALETTE_ACCENT} text: \"The smartest {PRICE} you'll spend this month.\" "
 "1:1 aspect ratio."),

(8, "application-ease-ugc", False,
 "Use the attached image as brand reference for tone ONLY. This must look like a real person's TikTok. "
 "Create a casual iPhone-filmed tutorial that looks like genuine UGC. "
 "A man in his 40s in a normal bathroom, filming himself applying {PRODUCT} to his dry hair. "
 "He's talking to camera, relaxed, slightly amused at how easy it is — "
 "no gloves, no mixing, just working it through like regular shampoo. "
 "Handwritten Procreate-style text: \"literally just shampoo and wait\" "
 "Bottom caption: \"my wife doesn't believe this costs {PRICE}\" "
 "Raw, slightly grainy, iPhone front camera. Not polished. 1:1 aspect ratio."),

(9, "bundle-value-reveal", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a bundle promotion ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT} headline: \"THE SMART WAY TO BUY.\" "
 "Three horizontal tiers: "
 "Tier 1 (small): \"1 BOTTLE\" — {PRICE} — \"Try it\" "
 "Tier 2 (medium, highlighted with {PALETTE_ACCENT} border): \"2 BOTTLES + FREE GIFT\" — price — \"Most Popular\" with a star badge "
 "Tier 3 (large): \"3 BOTTLES + 3 FREE GIFTS\" — price — \"Best Value\" with a crown badge "
 "Each tier shows {HERO} multiplied. "
 "Bottom: bold {PALETTE_ACCENT} text: \"Free shipping on all orders. 30-day money-back guarantee.\" "
 "1:1 aspect ratio."),

(10, "beard-and-hair-one-bottle", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a dual-use showcase ad, split composition. "
 "LEFT: close-up of a man's freshly colored rich dark hair — natural-looking, healthy shine, no grey. "
 "Label: \"HAIR ✓\" "
 "RIGHT: close-up of the same man's freshly colored beard — neat, naturally dark, even coverage. "
 "Label: \"BEARD ✓\" "
 "Center overlapping both: {HERO} at a slight angle. "
 "Top: bold {PALETTE_TEXT} headline: \"ONE BOTTLE. HEAD TO BEARD.\" "
 "Bottom: {PALETTE_ACCENT} text: \"Why buy two products when one handles everything?\" "
 "1:1 aspect ratio."),

# ─── SECTION B: PAIN POINT / FRUSTRATION ADS (11-20) ───

(11, "ammonia-cloud-escape", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a sensory frustration ad, split vertically. "
 "LEFT HALF: dark, hazy atmosphere — a man in his 40s in a bathroom filled with visible chemical vapor, "
 "eyes squinting, hand covering nose. Open {COMPETITOR} kit on counter. Sickly yellow-green color cast. "
 "Small red text: \"Every {COMPETITOR}. Every time.\" "
 "RIGHT HALF: same man, same bathroom, clean air, relaxed expression, warm natural light. "
 "{HERO} visible on counter. Argan nuts nearby. "
 "Small {PALETTE_ACCENT} text: \"{BENEFIT_2}. Finally.\" "
 "Top center: bold white text on dark bar: \"YOUR NOSE WILL THANK YOU.\" "
 "1:1 aspect ratio."),

(12, "scalp-safety-triptych", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a safety ad on clean white background. "
 "Top: bold {PALETTE_TEXT} headline: \"WHAT YOUR SCALP GOES THROUGH WITH {COMPETITOR}.\" "
 "Three clinical-style photo panels — \"BURNING\" | \"ITCHING\" | \"PEELING\" — red borders. "
 "Center divider: \"vs.\" "
 "Below: single calm photo of healthy scalp and naturally colored hair. Green border. "
 "\"ZERO IRRITATION. {BENEFIT_2}. ZERO DAMAGE.\" "
 "Bottom: {HERO} centered. \"{BENEFIT_3}. Your scalp is safe.\" "
 "1:1 aspect ratio."),

(13, "bathroom-aftermath", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a mess-frustration ad. Top 65%: overhead photo of a bathroom counter disaster — "
 "stains on countertop, stained latex gloves, open {COMPETITOR} kit, mixing bowl with dark residue, "
 "stained towel, crumpled instructions. Harsh overhead lighting. "
 "Bold white text: \"YOUR BATHROOM AFTER {COMPETITOR}.\" "
 "Bottom 35%: pristine clean {PALETTE_BG} background. "
 "{HERO} centered, one argan nut beside it. "
 "Bold {PALETTE_TEXT} text: \"Your bathroom after {BRAND}: exactly how you left it.\" "
 "1:1 aspect ratio."),

(14, "stained-skin-evidence", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a skin-staining frustration ad. "
 "Top 60%: extreme close-up of a man's hairline and temple showing dark DYE STAINING on skin — "
 "along forehead, behind ear, on neck. Harsh clinical lighting. "
 "Man's hand mid-scrub with washcloth, stain refusing to come off. "
 "Bold white text: \"THIS IS WHY {AUDIENCE} QUIT {COMPETITOR}.\" "
 "Bottom 40%: clean {PALETTE_BG} background. "
 "{HERO} standing with soft warm lighting. "
 "Bold {PALETTE_TEXT}: \"{BENEFIT_4}. {BENEFIT_2}. Just natural-looking color.\" "
 "1:1 aspect ratio."),

(15, "hair-damage-texture-split", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a hair TEXTURE comparison ad (not color — texture). "
 "Top: bold {PALETTE_TEXT}: \"{COMPETITOR} COVERS YOUR GREY. THEN DESTROYS YOUR HAIR.\" "
 "LEFT panel: extreme close-up of dry, straw-like, frayed hair strands. \"AFTER {COMPETITOR}\" in red. "
 "RIGHT panel: smooth, glossy, healthy strands with shine. \"AFTER {BRAND}\" in {PALETTE_ACCENT}. "
 "Center: thin {PALETTE_ACCENT} divider. "
 "Bottom: {HERO} centered. Three benefit callouts: \"{BENEFIT_3}\" | \"{BENEFIT_2}\" | \"{BENEFIT_4}\". "
 "\"Color that IMPROVES your hair. Not a trade-off — an upgrade.\" "
 "1:1 aspect ratio."),

(16, "transfer-staining-evidence", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a transfer/staining frustration ad. "
 "Top half: close-up of a white dress shirt collar with dark smear — "
 "from spray-on color transferring. Next to it: white pillowcase with similar stains. "
 "Harsh flash photography. "
 "Bold white text: \"{COMPETITOR}: LOOKS GREAT UNTIL IT'S ON EVERYTHING YOU OWN.\" "
 "Bottom half: clean {PALETTE_BG} background. "
 "{HERO} centered. Bold {PALETTE_TEXT}: \"{BRAND} doesn't transfer. Ever.\" "
 "\"The color is IN your hair, not ON your hair.\" "
 "1:1 aspect ratio."),

(17, "root-regrowth-treadmill", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a maintenance-frustration ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"THE NEVER-ENDING CYCLE.\" "
 "Center: a circular diagram with 4 stages connected by arrows forming a loop: "
 "\"DYE HAIR\" → \"Look good for 2 weeks\" → \"Roots appear\" → \"Book salon / Buy more dye\" → back to start. "
 "A large red \"STOP\" stamp over the cycle. "
 "Below: {HERO} breaking through the cycle visually. "
 "Bold {PALETTE_ACCENT}: \"Break the cycle. {TIME}. In your shower. Done.\" "
 "1:1 aspect ratio."),

(18, "coworker-noticed-scene", False,
 "Use the attached image as brand reference for tone ONLY. No product or branding. "
 "Create a UGC-style frustration scene. Modern office break room, natural light. "
 "A man in his 40s in business casual by the coffee machine. A female coworker giving him a look — "
 "not mean, but clearly noticing his freshly-{COMPETITOR}'d flat helmet hair. "
 "He's touching his hair self-consciously. "
 "Large bold white text: \"'DID YOU DO SOMETHING TO YOUR HAIR?' — THE SIX WORDS NOBODY WANTS TO HEAR AT WORK.\" "
 "Below: \"They noticed. They always notice.\" "
 "No product, no logo. Raw, relatable. 1:1 aspect ratio."),

(19, "mirror-defeat-moment", False,
 "Use the attached image as brand reference for tone ONLY. No product or branding. "
 "Create an emotionally raw scene. A man in his late 40s, dimly lit bathroom, shirtless, "
 "hands on sink counter, staring at reflection. "
 "Hair has flat helmet look — too dark, too uniform. Faint dye stains on forehead and temples. "
 "Open {COMPETITOR} kit on counter. Expression is pure defeat. "
 "35mm f/1.8, moody warm-amber grade, cinematic. "
 "Bold white text: \"You fixed the grey. You created a bigger problem.\" "
 "Below: \"There's a better way.\" "
 "No product, no logo, no CTA. Just the feeling. 1:1 aspect ratio."),

(20, "process-comparison-strip", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a visual process comparison in two rows. "
 "TOP ROW \"{COMPETITOR} PROCESS\": 5 mini-panels — open kit, putting on gloves, mixing chemicals, "
 "timer at {COMP_TIME}, scrubbing stains off skin. Harsh lighting. Red X marks. "
 "BOTTOM ROW \"{BRAND} PROCESS\": 3 mini-panels — applying {HERO} to hair (no gloves), "
 "timer at {TIME}, man rinsing in shower looking relaxed. Warm clean lighting. Green checkmarks. "
 "Top headline: \"{COMP_TIME} OF MESS vs. {TIME} OF SHAMPOO.\" "
 "1:1 aspect ratio."),

# ─── SECTION C: OBJECTION CRUSHER ADS (21-30) ───

(21, "too-cheap-text-convo", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a price-objection-crusher on dark {PALETTE_TEXT} background. "
 "Top: large bold white: \"'{PRICE} CAN'T REPLACE A {COMP_PRICE}.'\" "
 "Below in {PALETTE_ACCENT} italic: \"— Every man, right before they tried it.\" "
 "Center: text message screenshot mockup — "
 "Friend: 'Did you get a salon job? Your hair looks great' "
 "Me: 'Nah bro it's a {PRICE} shampoo' "
 "Friend: 'Shut up' "
 "Me: 'Dead serious. {BRAND}. Look it up' "
 "Friend: 'Sending me the link rn' "
 "Bottom: {HERO} small. \"We cut the salon overhead, not the formula.\" Five gold stars. "
 "1:1 aspect ratio."),

(22, "shampoo-dyes-dont-work-crusher", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a skepticism-crusher targeting {AUDIENCE} who've tried other products. "
 "Dark {PALETTE_TEXT} background. "
 "Top: bold white: \"'I'VE TRIED {COMPETITOR} BEFORE. THEY DON'T WORK.'\" "
 "Below in {PALETTE_ACCENT} italic: \"— You're right. Most don't. Here's why this one is different.\" "
 "Three comparison rows with red X → gold checkmark: "
 "Row 1: \"Surface tinting\" → \"Deep color that bonds\" "
 "Row 2: \"Weak formula\" → \"Concentrated 5-in-1 with {BENEFIT_3}\" "
 "Row 3: \"One shade fits all\" → \"Natural-looking color that blends\" "
 "Bottom: {HERO} hero-lit. \"{STAT_USERS} already switched.\" Five gold stars. "
 "1:1 aspect ratio."),

(23, "5-in-1-unpacked-diagram", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a multi-benefit unpacking ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"'TOO GOOD TO BE TRUE?' — LET'S UNPACK IT.\" "
 "{HERO} large, hero-lit, centered. "
 "Five {PALETTE_ACCENT} lines extending to benefit cards: "
 "\"{BENEFIT_1}\" | \"{BENEFIT_2}\" | \"{BENEFIT_3}\" | \"{BENEFIT_4}\" | \"Smells Great\" "
 "Each card has an icon and supporting detail. "
 "Bottom: five gold stars + \"One product. Five jobs. Zero compromise.\" "
 "1:1 aspect ratio."),

(24, "time-claim-proof", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a time-claim validation ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"'{TIME} SOUNDS IMPOSSIBLE FOR {PRODUCT}.'\" "
 "Below: italic {PALETTE_ACCENT}: \"Here's the science.\" "
 "Center: a simple diagram showing the product application process — "
 "\"Apply to dry hair\" → \"Formula pre-opens hair cuticle\" → \"Color deposits rapidly\" → \"Rinse\" "
 "Each step with a small clock icon showing elapsed time. "
 "Below: a real customer review card: \"\\\"{REVIEW_TEXT}\\\" — {REVIEW_NAME}\" "
 "Bottom: {HERO}. \"It works because the formula works differently.\" "
 "1:1 aspect ratio."),

(25, "grey-coverage-proof-grid", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a grey-coverage proof ad on white background. "
 "Top: bold {PALETTE_TEXT}: \"WILL IT WORK ON MY GREY?\" "
 "Below: \"YES. ALL OF IT.\" in massive {PALETTE_ACCENT}. "
 "Center: a 2×2 grid of before/after close-up photos: "
 "Grid 1: \"25% grey\" before → after. Grid 2: \"50% grey\" before → after. "
 "Grid 3: \"75% grey\" before → after. Grid 4: \"100% grey\" before → after. "
 "Each with green checkmark and \"{BENEFIT_1}\" beneath. "
 "Bottom: {HERO}. \"Every level of grey. One bottle.\" "
 "1:1 aspect ratio."),

(26, "brand-trust-builder", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a brand-trust ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"YOU'VE NEVER HEARD OF US. HERE'S WHY YOU WILL.\" "
 "Center: five trust signals in a vertical stack with icons: "
 "1. \"{STAT_USERS} {AUDIENCE} have switched\" — crowd icon "
 "2. \"30-day money-back guarantee\" — shield icon "
 "3. \"Based in Austin, TX\" — map pin icon "
 "4. \"Real customer reviews, real photos\" — camera icon "
 "5. \"Organic, ammonia-free formula\" — leaf icon "
 "Bottom: {HERO} centered. Five gold stars. \"Try it risk-free.\" "
 "1:1 aspect ratio."),

(27, "satisfaction-guarantee-badge", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a risk-reversal ad on dark {PALETTE_TEXT} background. "
 "Center: a large circular golden guarantee badge/seal with ornate border: "
 "\"100% SATISFACTION OR YOUR MONEY BACK — 30 DAYS — NO QUESTIONS\" "
 "Above the badge: bold white: \"STILL NOT SURE?\" "
 "Below the badge: \"We're so confident you'll love {BRAND} that we'll refund every cent if you don't.\" "
 "Bottom: {HERO} flanked by five gold stars. "
 "\"{STAT_USERS} {AUDIENCE}. Zero risk to try.\" "
 "1:1 aspect ratio."),

(28, "longevity-calendar", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a color-longevity visualization ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"HOW LONG DOES IT ACTUALLY LAST?\" "
 "Center: a horizontal calendar/timeline bar spanning 4 weeks: "
 "Week 1: deep rich color swatch — \"Day 1: Full Coverage\" "
 "Week 2: still deep — \"Day 14: Still Strong\" "
 "Week 3: very slightly lighter — \"Day 21: Looking Great\" "
 "Week 4: gentle fade — \"Day 28: Time to Refresh\" "
 "A gold line showing consistent color above a red dashed line showing {COMPETITOR} fading rapidly by Day 7. "
 "Bottom: {HERO}. \"Color that actually stays. Not marketing — results.\" "
 "1:1 aspect ratio."),

(29, "hair-type-diversity", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a hair-type reassurance ad on white background. "
 "Top: bold {PALETTE_TEXT}: \"WORKS ON YOUR HAIR. YES, YOURS.\" "
 "Center: a horizontal row of 5 circular portrait photos showing diverse men with different hair types: "
 "\"Thick & Coarse\" | \"Fine & Thin\" | \"Curly\" | \"Straight\" | \"Chemically Treated\" "
 "Each with a gold checkmark. "
 "Below: \"Same bottle. Same {TIME}. Same results.\" "
 "Bottom: {HERO} centered. Five gold stars. "
 "1:1 aspect ratio."),

(30, "fake-shade-fear-crusher", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a shade-anxiety crusher ad. "
 "Top: bold {PALETTE_TEXT}: \"'WILL IT LOOK FAKE?'\" "
 "Below: massive {PALETTE_ACCENT}: \"SEE FOR YOURSELF.\" "
 "Center: two extreme close-up photos of hair side by side: "
 "LEFT: flat, uniform, lifeless {COMPETITOR} color — zero depth. Label: \"{COMPETITOR}\" in red. "
 "RIGHT: rich, multi-dimensional, natural-looking color with subtle strand variation. Label: \"{BRAND}\" in {PALETTE_ACCENT}. "
 "Bottom: {HERO}. Bold {PALETTE_TEXT}: \"Natural black isn't flat. Neither is ours.\" "
 "1:1 aspect ratio."),

# ─── SECTION D: PSYCHOLOGICAL TRIGGER ADS (31-40) ───

(31, "fear-of-aging-perception", False,
 "Use the attached image as brand reference for tone ONLY. No product or branding. "
 "Split composition — same man, same sharp charcoal suit, same meeting room. "
 "LEFT: heavy grey hair and beard. Colleagues across table exchanging subtle glance. "
 "He looks competent but overlooked. Muted, cool lighting. "
 "RIGHT: naturally dark hair and beard. Colleagues leaning in, engaged, listening. "
 "He looks authoritative, vital. Warm lighting. "
 "Bottom: bold white: \"GREY HAIR DOESN'T CHANGE WHO YOU ARE. IT CHANGES HOW THEY SEE YOU.\" "
 "\"Take back the room.\" No product, no logo. 1:1 aspect ratio."),

(32, "identity-restoration-mirror", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Emotionally resonant ad. Full frame: warm bathroom, man in late 40s, freshly showered, towel on shoulders, "
 "looking at reflection with quiet smile of recognition — hair rich, natural, beard matches. "
 "He's seeing someone he hasn't seen in a long time — himself. "
 "50mm f/1.8, warm golden hour grade. "
 "Lower third: bold white italic serif: \"You didn't change your look.\" "
 "Bold uppercase: \"YOU GOT IT BACK.\" "
 "Bottom corner: {HERO} small, five gold stars. "
 "Pure emotion. 1:1 aspect ratio."),

(33, "transformation-reveal-reaction", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a transformation-reaction ad. "
 "Full frame: a man stepping out of the bathroom, freshly styled, natural-looking dark hair. "
 "His wife/partner is in the hallway, mid-conversation, and has stopped — mouth slightly open, eyes wide, "
 "clearly noticing something different. She's about to say something. "
 "Warm home lighting, natural and candid feeling. "
 "Large bold white text: \"THE LOOK ON HER FACE SAID EVERYTHING.\" "
 "Below: \"He didn't tell her. She just knew something was different.\" "
 "Bottom: {HERO} small. Five gold stars. "
 "1:1 aspect ratio."),

(34, "nostalgia-your-color-returned", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a nostalgia-driven ad on {PALETTE_BG} background. "
 "Top: elegant italic serif in {PALETTE_TEXT}: \"Remember your hair at 30?\" "
 "Center: two side-by-side photos with a thin {PALETTE_ACCENT} divider: "
 "LEFT: slightly faded, warm-toned photo styled like a casual photo from 15 years ago — "
 "man with rich, naturally dark hair, looking young and vibrant. Labeled \"Then.\" "
 "RIGHT: same man today — same rich dark hair color, older but looking vital and confident. Labeled \"Now.\" "
 "Below: bold {PALETTE_TEXT}: \"Your hair color, returned.\" "
 "Bottom: {HERO}. \"Not a new look. Your look.\" "
 "1:1 aspect ratio."),

(35, "social-proof-counter", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a social proof momentum ad on dark {PALETTE_TEXT} background. "
 "Center: a massive animated-style counter display reading \"{STAT_USERS}\" in huge bold {PALETTE_ACCENT}. "
 "Below: \"{AUDIENCE} HAVE ALREADY MADE THE SWITCH\" in bold white. "
 "Surrounding the counter: small floating review snippets in white rounded cards — "
 "\"Finally found it\" | \"Best {PRICE} I've spent\" | \"My barber recommended it\" | \"Wife loves it\" | \"Why didn't I find this sooner\" "
 "Bottom: {HERO} centered. \"Join them. Risk-free.\" Five gold stars. "
 "1:1 aspect ratio."),

(36, "loss-aversion-price-rising", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create an urgency ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"THIS PRICE WON'T LAST.\" "
 "Center: large price tag visual showing original price crossed out in red and current {PRICE} in bold {PALETTE_ACCENT}. "
 "A small \"SAVE 50%\" badge. "
 "Below: a progress bar showing \"78% claimed\" in {PALETTE_ACCENT} fill. "
 "\"This batch pricing ends when inventory sells through.\" "
 "Bottom: {HERO}. \"Grab yours before it goes back to full price.\" "
 "Five gold stars. \"30-day money-back guarantee.\" "
 "1:1 aspect ratio."),

(37, "gradual-natural-timeline", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a progressive-result ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"THE BEST COMPLIMENT: 'YOU LOOK GREAT' — NOT 'DID YOU DYE YOUR HAIR?'\" "
 "Center: horizontal timeline — three photos of SAME man labeled Week 1 → Week 2 → Week 3: "
 "Week 1: subtle grey blending. Week 2: deeper, richer. Week 3: full natural coverage. "
 "Gold progress arrows between photos. "
 "Below: review card: \"{REVIEW_TEXT} — {REVIEW_NAME}\" "
 "Bottom: {HERO}. \"Gradual. Natural. Undetectable.\" "
 "1:1 aspect ratio."),

(38, "self-care-not-vanity", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a self-care framing ad on dark background. "
 "Full frame: moody, warm-lit photo of a man's grooming shelf in a modern bathroom — "
 "{HERO} standing among cologne, a nice watch, a good razor. "
 "Everything on the shelf looks intentional, premium, masculine. "
 "The product is just another part of a man who takes care of himself. "
 "Large bold white text: \"IT'S NOT VANITY. IT'S MAINTENANCE.\" "
 "Below: \"You iron your shirts. You polish your shoes. You take care of your hair.\" "
 "No stars, no price. Just positioning. "
 "1:1 aspect ratio."),

(39, "barber-authority-endorsement", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a barber-authority ad. "
 "Full frame: warm barbershop scene. A professional barber in his 50s with a neat beard, "
 "standing confidently behind his chair, arms crossed, looking directly at camera. "
 "{HERO} prominently displayed on his station counter among professional tools. "
 "Large bold white text: \"I'VE BEEN CUTTING HAIR FOR 30 YEARS.\" "
 "Below: \"This is the first product I recommend to every client who asks about covering grey.\" "
 "Bottom: \"— {REVIEW_NAME}, Master Barber\" in italic. Five gold stars. "
 "1:1 aspect ratio."),

(40, "reciprocity-free-gift", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a generous free-gift ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"WE DON'T JUST WANT YOUR ORDER. WE WANT YOUR COMPLETE TRANSFORMATION.\" "
 "Center: {HERO} large and centered. "
 "Three gift items arranged around it with dotted-line \"FREE\" labels: "
 "\"FREE Hair Volume Powder\" | \"FREE Hair Color Stick\" | \"FREE Styling Comb\" "
 "Below: \"Total value: $48 in free gifts — included with every 2-bottle order.\" "
 "Bold {PALETTE_ACCENT} CTA bar: \"CLAIM YOUR FREE GIFTS\" "
 "Bottom: five gold stars. \"30-day money-back guarantee.\" "
 "1:1 aspect ratio."),

# ─── SECTION E: EMOTIONAL / STORY-DRIVEN ADS (41-50) ───

(41, "shade-disaster-story", False,
 "Use the attached image as brand reference for tone ONLY. No product or branding. "
 "Create a storytelling scene. A man in his 40s sitting on the edge of a bathtub, head in hands, "
 "bathroom counter behind him showing an open {COMPETITOR} box. "
 "His hair is visibly the wrong shade — too dark, too flat, not his natural tone. "
 "Staining visible on his forehead. Morning light through frosted window. "
 "Bold white text: \"HE WANTED TO LOOK LIKE HIMSELF. HE ENDED UP LOOKING LIKE A COSTUME.\" "
 "Below: \"The wrong shade doesn't just look wrong. It feels wrong.\" "
 "No product. No CTA. Pure empathy. 1:1 aspect ratio."),

(42, "relief-reveal-moment", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a positive resolution ad. "
 "Full frame: man in late 40s, freshly showered, bright natural light. "
 "Hair looks NATURAL — rich dark with subtle depth, healthy shine, no helmet look. "
 "No staining anywhere. Genuine relieved half-smile at mirror. "
 "\"Finally, something that actually works\" mood. "
 "{HERO} on marble counter beside him, slightly out of focus. "
 "Bold white text: \"THIS IS WHAT 'NATURAL-LOOKING' ACTUALLY LOOKS LIKE.\" "
 "\"{BENEFIT_2}. {BENEFIT_4}. No helmet hair. Just your color — without the grey.\" "
 "Five gold stars. \"Join {STAT_USERS} {AUDIENCE}.\" "
 "1:1 aspect ratio."),

(43, "wife-partner-reaction-text", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a relationship-reaction ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"ACTUAL TEXTS FROM WIVES & GIRLFRIENDS.\" "
 "Center: three stacked iPhone text message screenshots with realistic iOS styling: "
 "Text 1: \"Did you do something different? You look really good today 😍\" "
 "Text 2: \"Ok whatever you're doing to your hair KEEP DOING IT\" "
 "Text 3: \"My mom asked if you got younger lol\" "
 "Below: {HERO} centered. "
 "Bold {PALETTE_ACCENT}: \"The best reviews come from the people who see you every day.\" "
 "Five gold stars. 1:1 aspect ratio."),

(44, "confidence-boardroom-split", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a professional confidence ad, split vertically with thin {PALETTE_ACCENT} divider. "
 "LEFT: man in boardroom, grey hair, slightly uncertain posture, looking down at notes. "
 "Muted cool lighting. Label: \"BEFORE\" in small grey. "
 "RIGHT: same man, same boardroom, naturally colored dark hair, upright confident posture, "
 "making eye contact with the room. Warm lighting. Label: \"AFTER\" in small {PALETTE_ACCENT}. "
 "Bottom center overlapping both: {HERO}. "
 "Bold {PALETTE_TEXT}: \"Same man. Same room. Different energy.\" "
 "1:1 aspect ratio."),

(45, "barber-cringe-to-nod", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a two-panel barber reaction ad. "
 "TOP PANEL: barbershop scene — barber examining client's flat helmet-look {COMPETITOR} hair with a visible wince. "
 "Client looks embarrassed. Label: \"BEFORE {BRAND}\" "
 "BOTTOM PANEL: same barbershop — barber running hands through client's natural-looking, richly colored hair "
 "with an approving nod and slight smile. Label: \"AFTER {BRAND}\" "
 "Between panels: {HERO} centered. "
 "Bold {PALETTE_TEXT}: \"The barber test. Passed.\" "
 "1:1 aspect ratio."),

(46, "helmet-vs-natural-zoom", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a stark visual comparison of hair quality. "
 "LEFT: zoomed-in hair showing flat, uniform, lifeless {COMPETITOR} color — shoe polish look. "
 "\"BOX DYE\" in bold red. "
 "RIGHT: same angle, hair with natural depth, strand variation, healthy shine. "
 "\"{BRAND}\" in bold {PALETTE_ACCENT}. "
 "Top: bold {PALETTE_TEXT}: \"ONE LOOKS LIKE DYE. ONE LOOKS LIKE YOUR HAIR.\" "
 "Bottom: {HERO}. Five gold stars. \"{STAT_USERS} {AUDIENCE} switched.\" "
 "1:1 aspect ratio."),

(47, "morning-routine-integration", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a lifestyle integration ad showing the product fitting into a normal morning. "
 "A horizontal morning-routine timeline strip across the center: "
 "\"6:45 — Wake up\" | \"6:50 — Shower + apply {BRAND}\" | \"7:05 — Coffee\" | \"7:15 — Dressed\" | \"7:20 — Out the door\" "
 "Each moment has a small lifestyle icon. The {BRAND} step is highlighted in {PALETTE_ACCENT}. "
 "Top: bold {PALETTE_TEXT}: \"IT FITS INTO YOUR MORNING. NOT THE OTHER WAY AROUND.\" "
 "Bottom: {HERO}. \"{TIME}. During your shower. Done.\" "
 "1:1 aspect ratio."),

(48, "review-wall-mosaic", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a review mosaic ad on dark {PALETTE_TEXT} background. "
 "Top: bold {PALETTE_ACCENT}: \"REAL {AUDIENCE}. REAL REVIEWS.\" "
 "Center: a mosaic/grid of 9 small review cards, each with: "
 "small avatar, name, five gold stars, and a short one-line excerpt — "
 "varied quotes about natural results, ease of use, no smell, wife noticed, barber approved, etc. "
 "Bottom center: {HERO} overlapping the bottom row. "
 "Bold white: \"{STAT_USERS} and counting.\" "
 "1:1 aspect ratio."),

(49, "first-time-buyer-reassurance", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a first-time buyer ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"FIRST TIME? HERE'S EVERYTHING YOU NEED TO KNOW.\" "
 "Center: five reassurance points in a clean vertical list with {PALETTE_ACCENT} checkmarks: "
 "\"✓ Apply like shampoo — if you can wash your hair, you can use this\" "
 "\"✓ {TIME} — do it during your regular shower\" "
 "\"✓ {BENEFIT_2} — your scalp won't even notice\" "
 "\"✓ Natural-looking — nobody will know unless you tell them\" "
 "\"✓ 30-day money-back — zero risk to try\" "
 "Bottom: {HERO} centered. Bold {PALETTE_ACCENT}: \"Your first bottle is on us if you don't love it.\" "
 "1:1 aspect ratio."),

(50, "final-cta-everything-ad", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a comprehensive everything-in-one ad on {PALETTE_BG} background. "
 "Top: bold {PALETTE_TEXT}: \"{BRAND} {PRODUCT}\" in massive text. "
 "Below: {HERO} large, hero-lit, centered, dramatic. "
 "Surrounding the product in a clean layout: "
 "LEFT column: four benefit checkmarks — \"{BENEFIT_1}\", \"{BENEFIT_2}\", \"{BENEFIT_3}\", \"{BENEFIT_4}\" "
 "RIGHT column: \"{TIME} application\", \"Works on hair + beard\", \"{STAT_USERS} {AUDIENCE} trust it\" "
 "Below product: five large gold stars with review count. "
 "Price: \"{PRICE}\" with original price crossed out. "
 "Bottom: bold {PALETTE_ACCENT} CTA bar: \"SHOP NOW — 30 DAY MONEY-BACK GUARANTEE\" "
 "Clean, dense, conversion-focused. 1:1 aspect ratio."),

# ─── SECTION F: FRUSTRATION / PROBLEM-SOLUTION ADS (51-60) ───

(51, "competitor-disaster-split", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a dramatic side-by-side split comparison ad. "
 "LEFT HALF labeled '{COMPETITOR}' in bold red uppercase at top: a person staring into a bathroom mirror, "
 "visibly frustrated with the results of using {COMPETITOR} — the outcome looks cheap, artificial, and wrong. "
 "Harsh bathroom fluorescent lighting, slightly unflattering. "
 "RIGHT HALF labeled '{BRAND}' in bold {PALETTE_ACCENT} uppercase at top: the SAME person, same bathroom, "
 "but now looking natural, polished, and confident — {BENEFIT_1}. "
 "Warm, flattering natural light from a window. "
 "Bottom center overlapping the divider: {HERO} with soft studio lighting. "
 "Bold {PALETTE_TEXT} at very bottom: \"STOP SETTLING. START SWITCHING.\" 1:1 aspect ratio."),

(52, "staining-damage-closeup", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a frustration-focused ad. Top 60%: extreme close-up photograph showing the visible damage or mess "
 "that {COMPETITOR} leaves behind — residue, staining, greasiness, flaking, or buildup. "
 "Harsh, clinical lighting. A frustrated hand trying to fix/remove the problem. "
 "Overlaid in large bold white uppercase: \"THIS IS WHY {AUDIENCE} QUIT {COMPETITOR}.\" "
 "Bottom 40%: clean {PALETTE_BG} background. "
 "Left: {HERO} standing upright with soft warm lighting. "
 "Right: bold {PALETTE_TEXT}: \"{BENEFIT_4}. {BENEFIT_2}. Just {BENEFIT_1}.\" "
 "Small {BRAND} wordmark bottom right. 1:1 aspect ratio."),

(53, "bathroom-aftermath", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a humorous frustration ad. Top 65%: overhead photo of a bathroom counter AFTER using {COMPETITOR} — "
 "mess everywhere: spills, stains, multiple products, crumpled instructions, residue on surfaces. "
 "The scene looks like a legitimate disaster — harsh overhead bathroom lighting. "
 "Bold white uppercase text overlaid: \"YOUR BATHROOM AFTER {COMPETITOR}.\" "
 "Bottom 35%: pristine clean {PALETTE_BG} background. "
 "{HERO} centered, clean and simple. "
 "Bold {PALETTE_TEXT}: \"Your bathroom after {BRAND}: exactly how you left it.\" "
 "Small {BRAND} wordmark bottom right. 1:1 aspect ratio."),

(54, "expert-reaction", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a storytelling frustration ad. Full frame: a professional setting shot at 50mm f/2.0 with warm natural light. "
 "An expert/professional examining a client's results from using {COMPETITOR} — visibly unimpressed, "
 "wincing at the cheap, obvious results. The client looks embarrassed. "
 "Large bold white uppercase overlaid: \"THE PROFESSIONALS ALWAYS KNOW.\" "
 "Below in smaller white: \"They always know.\" "
 "Bottom right corner: {HERO} small, with text beside it in {PALETTE_ACCENT}: \"The one professionals actually recommend.\" "
 "Mood: warm, real, slightly humorous. 1:1 aspect ratio."),

(55, "cheap-vs-premium-comparison", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a stark visual comparison ad on a split {PALETTE_BG}/white background. "
 "LEFT: zoomed-in showing the cheap, obvious, artificial results of {COMPETITOR} — "
 "clearly fake, no depth, no natural quality. Label: \"{COMPETITOR}\" in bold red. "
 "RIGHT: the same angle showing natural-looking, premium results — {BENEFIT_1}, {BENEFIT_2}. "
 "Label: \"{BRAND}\" in bold {PALETTE_ACCENT}. "
 "Center divider: thin {PALETTE_ACCENT} vertical line. "
 "Top: bold {PALETTE_TEXT} headline: \"ONE LOOKS CHEAP. ONE LOOKS NATURAL.\" "
 "Bottom: {HERO} centered with five gold stars and \"{STAT_USERS} {AUDIENCE} switched\" in {PALETTE_TEXT}. "
 "1:1 aspect ratio."),

(56, "they-noticed-scene", False,
 "Use the attached image as brand reference for tone ONLY. Do NOT include any product or branding. "
 "Create a UGC-style frustration scene. A modern everyday setting, natural lighting. "
 "A person who clearly used {COMPETITOR} — the results are obvious and artificial. "
 "Someone nearby is giving them a look — not mean, but clearly noticing something is off. "
 "The person is self-conscious, sensing something is wrong. "
 "Large bold white text overlaid in the lower third: "
 "\"'Did you do something different?' — the words nobody wants to hear.\" "
 "Below in smaller white: \"They noticed. They always notice.\" "
 "No product, no logo. Raw, relatable, scroll-stopping. 1:1 aspect ratio."),

(57, "transfer-stain-evidence", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a frustration ad showing transfer, staining, or residue. "
 "Top half: close-up photo showing evidence of {COMPETITOR} transferring or leaving residue on clothes, "
 "furniture, pillows, or skin — the kind of mess no one warned you about. "
 "Harsh, unflattering flash photography, like evidence photos. "
 "Bold white text: \"{COMPETITOR}: LOOKS FINE UNTIL IT'S ON EVERYTHING YOU OWN.\" "
 "Bottom half: clean {PALETTE_BG} background. "
 "{HERO} centered. Bold {PALETTE_TEXT}: \"{BRAND} doesn't transfer. Ever.\" "
 "Below in smaller text: \"{BENEFIT_4}. {BENEFIT_2}. The way it should be.\" "
 "1:1 aspect ratio."),

(58, "defeat-moment", False,
 "Use the attached image as brand reference for tone ONLY. Do NOT include any product or branding. "
 "Create an emotionally raw frustration scene. A person standing alone, looking at the result of using {COMPETITOR}. "
 "The result is worse than before they tried — obvious, cheap, embarrassing. "
 "Their expression is pure defeat — they tried to fix a problem and made it worse. "
 "Shot on 35mm f/1.8, moody warm-amber color grade, cinematic. "
 "Large bold white text in lower third: \"You tried to fix it. You created a bigger problem.\" "
 "Below in smaller white: \"There's a better way.\" "
 "No product, no logo, no CTA. Just the feeling. 1:1 aspect ratio."),

(59, "process-comparison-grid", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a visual comparison ad divided into two rows. "
 "TOP ROW labeled \"{COMPETITOR} PROCESS\": a horizontal strip showing 5 mini-panels — "
 "complicated setup, multiple steps, messy application, long wait time ({COMP_TIME}), difficult cleanup. "
 "Harsh lighting, messy, stressful energy. Red X marks on each panel. "
 "BOTTOM ROW labeled \"{BRAND} PROCESS\": a horizontal strip showing 3 mini-panels — "
 "simple application with {HERO}, short wait ({TIME}), done. "
 "Warm, clean, simple energy. Green checkmarks on each panel. "
 "Bold {PALETTE_TEXT} headline at very top: \"{COMP_TIME} OF MESS vs. {TIME} OF SIMPLE.\" "
 "1:1 aspect ratio."),

(60, "relief-reveal-resolution", True,
 "Use the attached image as brand reference. Match exact product structure. "
 "Create a positive-outcome frustration-resolution ad. "
 "Full frame: a person freshly finished with {BRAND}, looking natural and confident. "
 "{BENEFIT_1} — no cheap look, no residue, no embarrassment. "
 "Genuine, relieved half-smile at the mirror. "
 "The mood is: 'finally, something that actually works.' "
 "{HERO} sits casually on the counter beside them, slightly out of focus. "
 "Large bold white text overlaid: \"THIS IS WHAT 'ACTUALLY WORKS' LOOKS LIKE.\" "
 "Below in smaller white: \"{BENEFIT_2}. {BENEFIT_4}. {BENEFIT_1}. Done right.\" "
 "Five gold stars and \"Join {STAT_USERS} {AUDIENCE}\" in {PALETTE_ACCENT} at very bottom. "
 "1:1 aspect ratio."),
]
