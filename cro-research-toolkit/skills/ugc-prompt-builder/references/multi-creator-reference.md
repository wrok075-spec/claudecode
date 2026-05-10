# MULTI-CREATOR DIALOGUE UGC REFERENCE
For UGC ads where two (or rarely three) creators appear in conversation about a product. Used for "friend recommendation" formats, reaction ads, and authentic peer-to-peer endorsement formats.

================================================================
## WHEN TO USE MULTI-CREATOR DIALOGUE FORMAT

Multi-creator dialogue is one of the most powerful UGC formats because it inherits a fundamental conversion mechanic: **third-party endorsement is more trusted than first-person endorsement.** When Creator A tells Creator B about a product, the viewer (positioned as overhearing) processes it as an authentic recommendation, not an ad.

Use this format when:

- The brand wants to demonstrate peer-to-peer recommendation as a customer behavior
- The product is in a category where "my friend told me about it" is the actual purchase pathway (skincare, supplements, beauty, wellness)
- The creator persona benefits from contrast (skeptic + enthusiast, expert + novice, two friends)
- A traditional first-person UGC has felt too "sell-y" and the brand wants to soften the persuasion

Do NOT use this format for:
- Demos that need close product focus (the camera can't be in two places)
- Hard educational content where one expert needs sustained authority
- Categories where peer recommendation isn't the buying pattern (B2B SaaS, technical hardware)

================================================================
## THE CORE ARCHITECTURE

A multi-creator dialogue ad is structurally **3-5 scenes alternating between two creators**, with the dialogue passing back and forth in a recognizable conversation pattern.

The two most common architectures:

**Pattern A — The Recommendation Setup**
Creator A discovers/uses something. Creator B asks about it. Creator A explains. Creator B is converted.

**Pattern B — The Mutual Discovery**
Both creators are users. They affirm each other's experience. The dialogue is two friends who both love the product validating each other.

Pattern A is stronger for high-consideration purchases (the product needs explanation). Pattern B is stronger for low-consideration purchases (the product needs vibe, not pitch).

================================================================
## EXAMPLE BREAKDOWN: SKINCARE BRAND — RECOMMENDATION SETUP
Reference: 26 seconds, 4 scenes, two creators, Pattern A architecture

### SHOT-BY-SHOT TIMELINE

SCENE 1 (00:00–00:06) — Creator B asks the question (split screen or shot-reverse)
• ENVIRONMENT: Bathroom or vanity setting, both creators visible — could be a split-screen "duet" style or single shot with both in frame side-by-side
• EFFECT: Selfie-angle handheld, both creators looking at the camera initially, then Creator B turns slightly toward Creator A
• Creator B (the asker): late-20s, slight skeptic energy, hair down, casual top
• Creator A (the recommender): late-20s, friend-of-Creator-B, dewy-skin, slight knowing smile
• DIALOGUE: Creator B: "Wait, your skin has been INSANE lately. What are you actually doing differently?"
• Delivery: Creator B's "actually doing differently" lands with genuine curiosity, slight head-cock toward Creator A

SCENE 2 (00:06–00:14) — Creator A reveals (single creator close-up)
• ENVIRONMENT: Cut to Creator A alone, bathroom or vanity, soft natural light, slightly closer framing
• EFFECT: Direct eye contact + product reveal + close-hold product
• @creator_a holds @bubble_serum at chest height, brief lens focus hunt as it enters frame
• DIALOGUE: Creator A: "Okay so I've been using this for like three weeks. It's the Bubble [product name]. It's barely $20 and I genuinely cannot go back."
• Delivery: low-key reveal energy, slight smile on "barely $20," "cannot go back" lands with mild surprise at her own enthusiasm

SCENE 3 (00:14–00:21) — Creator B's reaction (single creator close-up)
• ENVIRONMENT: Cut to Creator B alone, same setting context, soft light
• EFFECT: Direct eye contact + reaction micro-expression + natural eye break
• Creator B's eyes go slightly wide, head tilts, eyes dart down briefly
• DIALOGUE: Creator B: "Wait — under $20? I'm literally about to order it. Where do I get it?"
• Delivery: genuine surprise, the "literally" lands with a half-laugh, energy is rising

SCENE 4 (00:21–00:26) — Creator A delivers the CTA (back to Creator A or two-shot)
• ENVIRONMENT: Either back to Creator A solo OR a two-shot of both creators visible
• EFFECT: Direct eye contact + on-screen text overlay + soft CTA
• If two-shot: both creators visible, Creator B nodding, Creator A looking at camera
• On-screen text: "@bubblebeauty.com — code [NAME]15"
• DIALOGUE: Creator A: "Their site, link's down there. You'll text me thanking me in two weeks."
• Delivery: warm-knowing energy, soft smile, the line "thanking me" lands with playful confidence

### THE CRITICAL CONSISTENCY RULES

1. **Save BOTH creators as Character Elements before generating anything.** This is non-negotiable for multi-creator ads. `@creator_a` and `@creator_b` must both be saved Elements with descriptions that lock their faces, hair, and wardrobe.

2. **Decide framing strategy upfront.** Three options:
   - **Solo cut-back-and-forth** (most common): each scene has one creator, the dialogue alternates. Cleanest for Seedance because each generation is a single character.
   - **Split screen duet style**: both visible side-by-side in a faux-duet. Possible in CapCut by stacking two solo generations.
   - **Two-shot in-frame**: both creators in the same generated frame. Hardest for Seedance — drift and inconsistency are common. Use sparingly, usually only for the opening or closing scene.

3. **Dialogue handoff cues.** The end of one scene's dialogue should feel like a question or pause that the next scene answers. "What are you actually doing differently?" is a complete handoff — Scene 2 responds. "I love this" is not — there's nothing to respond to.

4. **Eyeline matching.** When cutting between two solo creators, their gaze direction should imply they're looking at each other. If Creator A is on-screen looking slightly camera-right, Creator B should look slightly camera-left in her solo. This sells the conversation.

5. **Energy contrast.** The two creators should have slightly different energies. Same energy on both = boring. Skeptic + enthusiast, calm + excited, expert + novice — pick a contrast.

================================================================
## PROMPT STRUCTURE FOR MULTI-CREATOR SCENES

For solo cut-back-and-forth (the recommended approach):

**Solo scene with Creator A:**
```
Vertical 9:16 selfie-style video, [DURATION] seconds, single continuous handheld phone shot. @creator_a is in [ENVIRONMENT], [LIGHTING], [BACKGROUND]. Subject framing: slightly off-axis right of center, phone held about 20 inches from her face. She is looking [SLIGHTLY CAMERA-RIGHT, as if at someone off-screen / OR DIRECTLY AT CAMERA].

[TIMESTAMP RANGE]: [PERFORMANCE]. She says: "[DIALOGUE]." [DELIVERY NOTES].

Lighting: [LIGHTING], no color grade. Camera: handheld phone. No music. Native UGC quality.
```

**Solo scene with Creator B (responding):**
```
Vertical 9:16 selfie-style video, [DURATION] seconds, single continuous handheld phone shot. @creator_b is in [SAME ENVIRONMENT or matching aesthetic], [LIGHTING], [BACKGROUND]. Subject framing: slightly off-axis left of center, phone held about 20 inches from her face. She is looking [SLIGHTLY CAMERA-LEFT, as if at someone off-screen / OR DIRECTLY AT CAMERA].

[TIMESTAMP RANGE]: [PERFORMANCE — RESPONDING TO PREVIOUS SCENE'S DIALOGUE]. She says: "[DIALOGUE]." [DELIVERY NOTES].

Lighting: [SAME LIGHTING AS CREATOR A'S SCENE for visual continuity], no color grade. Camera: handheld phone. No music. Native UGC quality.
```

**Two-shot scene (use sparingly):**
```
Vertical 9:16 phone-style video, [DURATION] seconds, single continuous handheld shot. @creator_a and @creator_b are both in frame, side-by-side or with @creator_a slightly forward. [ENVIRONMENT, LIGHTING]. Both visible from chest up. Creator A is looking at the camera; Creator B is looking at Creator A nodding, or vice versa.

[TIMESTAMP RANGE]: @creator_a says: "[DIALOGUE]." Meanwhile @creator_b [PHYSICAL REACTION — nodding, smiling, etc.].

Lighting: [LIGHTING]. Camera: handheld phone. No music. Native UGC quality.
```

================================================================
## DIALOGUE PRINCIPLES FOR MULTI-CREATOR

1. **Each line must be in-character.** Creator A and Creator B should sound different. Different word choices, different rhythm, different energy. Read the lines aloud — if you can't tell which character is speaking, rewrite.

2. **Questions drive the dialogue.** The strongest multi-creator scripts use questions to advance the story. "What are you using?" "Why do you love it?" "Is it worth it?" Questions force responses, which force engagement.

3. **The recommender uses softer language than the asker.** The asker can be dramatic ("your skin has been INSANE"). The recommender should be measured ("I've been using this for three weeks, it's pretty good"). The contrast makes the recommendation believable — if both are dramatic, it sounds rehearsed.

4. **The conversion moment lives in the asker's reaction, not the recommender's pitch.** Scene 3 (Creator B's "I'm literally about to order it") is what converts the viewer, not Scene 2 (Creator A's reveal). The viewer identifies with the asker more than the recommender.

5. **Word count: 15-25 words per scene.** Multi-creator ads have shorter scenes because the cut between creators provides pacing variety. Each scene should land its line and hand off.

================================================================
## EFFECTS DENSITY FOR MULTI-CREATOR

Multi-creator ads run LOW-MEDIUM density. The variety is in the cut between creators, not in within-shot effects.

Per scene:
- 2-3 effects max (selfie-angle, eye contact, micro-expression, focus hunt)
- The cut between creators IS an effect
- Don't add jump cuts, speed ramps, or transitions — the dialogue handoff carries the pacing

================================================================
## COMMON FAILURE MODES

1. **Both creators look the same.** If your two saved Character Elements are too similar (similar age, hair color, vibe), the viewer can't distinguish them and the dialogue confuses. Build creators with deliberate contrast — different hair colors, different style, different energy archetype.

2. **Eyeline mismatch.** Creator A is on-screen looking right, then Creator B is on-screen also looking right. The viewer reads them as looking at the same off-screen thing, not at each other. Always specify gaze direction in your prompts and ALWAYS reverse it between cuts.

3. **Lighting drift between scenes.** Creator A in soft window light, Creator B in harsh overhead light. The viewer registers them as in different physical spaces, breaking the conversation illusion. Match lighting descriptions across scenes.

4. **Both creators talk like the same person.** No vocal contrast = unbelievable. Force differences in vocabulary, sentence length, and energy.

5. **Dialogue that doesn't actually respond.** "What are you using?" → "I love it!" doesn't answer the question. The response must engage the previous line. Read all dialogue together before generating.

6. **Two-shot generations failing.** Seedance struggles to keep both creators consistent in a single frame. If you must do a two-shot, generate it 4-6 times and pick the cleanest. For most multi-creator ads, just do solo cut-back-and-forth and stitch in CapCut.

================================================================
END OF DOCUMENT
