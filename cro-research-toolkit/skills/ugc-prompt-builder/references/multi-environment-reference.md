# MULTI-ENVIRONMENT UGC REFERENCE
For UGC ads where the same creator appears across multiple distinct settings within one ad. Used for "day-in-the-life" formats, routine-based product positioning, and lifestyle integration ads.

================================================================
## WHEN TO USE MULTI-ENVIRONMENT FORMAT

Multi-environment ads work when the product fits naturally into multiple moments of someone's day. Think:

- Wellness/supplement brands ("here's how I use it from morning to evening")
- Beauty routines (vanity → bathroom → on-the-go touch-ups)
- Beverage brands (kitchen pour → workout sip → desk afternoon)
- Apparel/footwear ("I wore this everywhere this week")
- Tech/gadgets that work across contexts

Multi-environment ads do NOT work for:
- Products that are inherently single-context (a kitchen tool used only at the stove)
- Pain-point pivots that need ONE problem moment to land (problem-solution structure)
- Testimonial formats where the credibility comes from sustained eye contact

If the brief is "show this product fitting into a real day," use multi-environment. If the brief is "convince me this product works," use a standard single-environment format from the main reference file.

================================================================
## THE CORE ARCHITECTURE

A multi-environment ad is structurally **3-5 scenes, each in a different setting, connected by ONE narrative thread.**

The narrative thread is the through-line that ties the scenes together. Without it, the ad feels like a montage of disconnected clips. With it, the ad feels like a story.

The four most common narrative threads for multi-environment UGC:

1. **Time-of-day arc** — morning → midday → afternoon → evening (e.g., AG1 across a wellness day)
2. **Activity arc** — workout → work → social (e.g., a hydration product across active moments)
3. **Need-state arc** — sleepy → focused → tired → recovered (e.g., a supplement positioned as functional)
4. **Emotional arc** — chaotic → centered → confident → reflective (e.g., beauty/wellness positioned as ritual)

Pick ONE thread and commit to it. The dialogue across scenes should reinforce the thread, not introduce a second one.

================================================================
## EXAMPLE BREAKDOWN: WELLNESS SUPPLEMENT — TIME-OF-DAY ARC
Reference: 28 seconds, 4 environments, single creator, "morning to evening" thread

### SHOT-BY-SHOT TIMELINE

SCENE 1 (00:00–00:07) — Kitchen, Morning
• ENVIRONMENT: Apartment kitchen, early morning soft window light from camera-left, lived-in marble counter, water kettle visible in background, a partially-open laptop on the counter
• EFFECT: Selfie-angle handheld + direct eye contact + relaxed morning energy
• Creator in casual loungewear (oversized t-shirt or robe), hair messy, no makeup or minimal
• @creator_a is preparing the supplement — pouring water, scooping, stirring — natural unscripted action
• DIALOGUE: "Okay so this is the only thing I do every single morning before anything else. Coffee can wait."
• Delivery: low-energy, friend-tone, the line lands on "before anything else" with a small smile

SCENE 2 (00:07–00:14) — Office Desk, Mid-Morning
• ENVIRONMENT: Home office or desk space, natural daylight, laptop open with vague work visible, a notebook, a coffee mug now visible (the supplement came first, coffee came after)
• EFFECT: Selfie-angle + slightly more energetic + direct eye contact
• Same creator, now in casual professional wear (button-down or sweater), hair clipped up
• Holding the supplement container or empty glass briefly visible on desk
• DIALOGUE: "By 10am I'm two emails deep and I can actually feel the difference. I used to crash by 11."
• Delivery: mid-energy, the line "actually feel the difference" lands with a small headshake of mild disbelief

SCENE 3 (00:14–00:21) — Gym or Outdoor Walk, Afternoon
• ENVIRONMENT: Either a gym mid-workout (light sweat, athletic wear) OR an outdoor walk (sunlight, casual jacket, headphones visible)
• EFFECT: Selfie-angle + slight handheld breathiness + casual-active energy
• Same creator, athletic or active wardrobe, hair pulled back, slight flush
• DIALOGUE: "And I'm not crashing in the afternoon anymore. Like, I had energy for this workout. That used to be unheard of."
• Delivery: slightly out-of-breath if mid-workout, conversational pace, "unheard of" lands with a laugh

SCENE 4 (00:21–00:28) — Couch, Evening
• ENVIRONMENT: Living room couch, low warm lamp lighting, evening cozy energy, TV on in the background blurred, a blanket
• EFFECT: Selfie-angle + soft direct eye contact + reflective energy
• Same creator, in evening loungewear (different from morning loungewear — the wardrobe progression is the visual marker of the day passing), hair down
• DIALOGUE: "I sleep better, I wake up better, my whole day is better. I'm not even joking. Get the green one — it's @ag1.com."
• Delivery: warm, low energy, the CTA at the end is conversational and feels earned after the full-day arc

### THE CRITICAL CONSISTENCY RULES

1. **Same creator across all scenes.** Use a saved Character Element. Reference the same `@creator_a` in every scene's prompt. Without this, the creator's face will drift and the ad falls apart.

2. **Wardrobe MUST change between scenes.** This is the visual marker that time is passing. If she wears the same sweater in scene 1 and scene 4, the viewer doesn't register the day-arc. Specify wardrobe per scene in your prompts.

3. **Hair styling SHOULD change.** Morning hair = messy, mid-morning = clipped up, afternoon = pulled back, evening = down. Subtle but reinforces the time progression.

4. **Lighting changes are non-negotiable.** Morning = soft cool window light. Mid-morning = bright daylight. Afternoon = warm or active. Evening = warm lamp light. Specify lighting in every scene prompt.

5. **Energy level shifts.** Morning = low, mid-morning = focused, afternoon = active, evening = reflective. The creator's vocal delivery should match the energy of each environment.

================================================================
## PROMPT STRUCTURE FOR MULTI-ENVIRONMENT SCENES

Each scene gets its own Seedance generation. The prompt template:

```
Vertical 9:16 selfie-style video, [DURATION] seconds, single continuous handheld phone shot. @creator_a is in [SPECIFIC ENVIRONMENT WITH 3-4 PROPS], [LIGHTING DESCRIPTION] from camera-left, [TIME-OF-DAY ATMOSPHERE]. She is wearing [WARDROBE — different from previous scene], [HAIR STYLE — different from previous scene]. Subject framing: slightly off-axis right of center, phone held about 20 inches from her face at slightly downward tilt, natural micro-wobble throughout.

[OPTIONAL: She is interacting with @product if applicable — describe the action specifically]

[TIMESTAMP RANGE]: [PERFORMANCE DESCRIPTION matched to the environment's energy]. She says: "[DIALOGUE LINE]." [DELIVERY NOTES tuned to time-of-day and environment].

Lighting: [TIME-SPECIFIC LIGHTING], no color grade, no filter. Camera: handheld phone, natural micro-wobble, no zooms, no cuts. Audio: clean dialogue, ambient room tone of [SPECIFIC ENVIRONMENT — kitchen morning sounds, office quiet, gym ambient, evening room tone]. American English, neutral accent. No music. No on-screen text. Native UGC quality, looks like an iPhone selfie video.
```

================================================================
## DIALOGUE PRINCIPLES FOR MULTI-ENVIRONMENT

The dialogue across scenes must:

1. **Reference the previous scene implicitly.** Scene 2's "I used to crash by 11" only works because Scene 1 established a morning routine. Each scene's dialogue should feel like a continuation, not a restart.

2. **Maintain ONE thesis.** If the thesis is "this product gives me sustained energy across my day," every scene's dialogue must reinforce that. Don't pivot to "and it tastes great too" mid-ad.

3. **Stay in character voice.** The creator's personality, slang, and energy should be consistent. If she's deadpan in Scene 1, she's deadpan in Scene 4 — even if the energy level shifts.

4. **The CTA lives in the final scene only.** Don't end every scene with a soft sell. Let the day-arc do the persuasion and put the ask at the end.

5. **Word count per scene: 15-22 words for 7-second scenes.** Multi-environment ads have more scenes than standard UGC, so each scene is shorter. Tighten the dialogue.

================================================================
## EFFECTS DENSITY MAP FOR MULTI-ENVIRONMENT

Multi-environment ads run LOW DENSITY throughout. The variety is in the environment changes, not the effects. Adding effects on top of environment shifts overloads the viewer.

- 1-2 effects per 7-second scene maximum
- The "effect" is often just the environment change itself
- Hard cuts between scenes (no transitions) — the cut IS the visual punctuation

================================================================
## ENERGY ARC FOR MULTI-ENVIRONMENT

Three-act structure across the full ad:

**Act 1 (first scene)**: Establish the routine and the creator's relationship to the product. Low key.
**Act 2 (middle scenes)**: Show the product in action across the day. Build evidence through specific moments. Energy escalates with the time-of-day arc.
**Act 3 (final scene)**: Reflect on the cumulative effect. The CTA lands here. Energy is warm and earned.

================================================================
## COMMON FAILURE MODES

1. **Creator drift.** Most common failure. Always use a saved Character Element across scenes.
2. **Wardrobe consistency** (the OPPOSITE problem — viewer thinks it's all one day if she's in the same outfit). Force wardrobe changes in your prompts.
3. **Lighting inconsistency.** If you say "morning soft light" and Seedance generates harsh midday light, the time-of-day arc fails. Be explicit about lighting per scene.
4. **Environment specificity.** "She's in her kitchen" is too vague — Seedance generates a generic kitchen. Specify 3-4 props per environment to anchor the setting.
5. **Dialogue-thread breaks.** Scenes that don't reinforce the same thesis. Read all four dialogue lines together before generating — they should sound like one continuous argument.

================================================================
END OF DOCUMENT
