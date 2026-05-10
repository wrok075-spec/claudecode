---
name: ugc-prompt-builder
description: End-to-end UGC ad generation system for Seedance 2.0. Writes the ChatGPT Images 2.0 character prompt that creates the UGC creator AND the Seedance scene prompts with creator dialogue. Handles standard single-creator UGC (problem-solution, demo-first, testimonial) plus advanced formats — multi-environment day-in-life ads, multi-creator dialogue ads, and action-shot product demos. Use whenever the user wants to create a UGC ad, generate a UGC creator, write a UGC shot list, plan a creator-style video, or mentions Seedance with UGC. Also trigger for talking-head ads, product demos, testimonials, two-creator dialogue, day-in-the-life ads, POV ads, or any DTC/agency video that needs to feel native and unproduced. Trigger on phrases like "UGC ad," "UGC creator," "Seedance UGC," "creator ad script," "TikTok ad," "DTC video ad," "two creators talking," "day in my life ad," or "POV ad."
---

# UGC Prompt Builder for Seedance 2.0 (v2)

End-to-end UGC ad generation system. This skill orchestrates the entire workflow: writes the ChatGPT Images 2.0 prompt that generates the creator, then writes the Seedance 2.0 scene prompts with creator dialogue. Built for DTC brands and creative agencies producing UGC video ads for TikTok, Meta, and similar native feeds.

**This is v2.** All instructions here have been production-tested through real builds. The character archetype library, the Higgsfield Element architecture, the no-bite rule, the word-count pacing rule, and the voice consistency guidance all come from hard-won learnings.

## The Two-Step Workflow

This skill handles two distinct outputs based on what the user needs:

**Step 1: Character Generation Prompt** (for ChatGPT Images 2.0)
- Writes the prompt the user pastes into ChatGPT to generate their UGC creator
- Matches the creator to the brand's actual ICP — wellness mom, downtown girl, desk worker, active adult, etc.
- Outputs a single fully-specified prompt the user copies and pastes

**Step 2: Scene Prompts** (for Seedance 2.0)
- Writes the structured shot-by-shot scene prompts with dialogue
- Selects the right UGC format (problem-solution, demo-first, testimonial, multi-environment, multi-creator, action-shot)
- Outputs the four-section structure with creator dialogue layered into each shot

The user typically does Step 1 first (generates the creator, saves them as a Higgsfield Character Element), then Step 2 (uses the saved Element in the scene prompts).

## How this skill works

1. The user provides a **creative brief** — product, angle, target audience, format, etc.
2. **Default behavior**: when the user asks for help with a UGC ad and doesn't explicitly say they already have a creator, ALWAYS start with Step 1 (character generation prompt) without asking. Do not hedge or ask the user which step they want — lead with Step 1, generate the character prompt, then tell them to come back for Step 2 after they've saved the creator as a Character Element in Higgsfield.
3. Skip Step 1 only if the user explicitly says they already have their creator, or if they ask only for the script.
4. Identify which step(s) they need:
   - "Help me make a UGC ad for [Brand]" → both steps (lead with Step 1, no clarifying questions)
   - "Help me with a UGC ad" → both steps (lead with Step 1, no clarifying questions)
   - "I have my creator already, write the script" → skip to Step 2
   - "Write me a ChatGPT prompt for a UGC creator for [Brand]" → only Step 1
3. Check for brand foundation files at `brand/brand-dna.md`, `brand/brand-voice.md`, and `brand/icp-cards.md`. If they exist, read them and use them.
4. **For Step 1**: read `references/character-creation-reference.md` for the archetype library and prompt template.
5. **For Step 2**: identify the UGC format and read the relevant reference file(s) (see Format Selection).
6. Output cleanly — Step 1 outputs a single ChatGPT prompt; Step 2 outputs the full four-section scene structure.

## Step 1: Character Generation

When the user needs a creator generated, write a ChatGPT Images 2.0 prompt that matches the brand's ICP. Read `references/character-creation-reference.md` for the full archetype library and worked examples.

The output is a single block of prose the user pastes into ChatGPT. Do NOT include shot timelines or scene structure — that's Step 2 territory.

After delivering the character prompt, include a short note covering:
- The archetype identified (e.g., "Downtown Girl 24-29")
- A reminder to save the resulting image as a Character Element in Higgsfield
- A short Element description suggestion that locks face/hair/wardrobe

## Step 2: Scene Prompt Generation

When the user has their creator and is ready to generate scenes, identify the right UGC format and write the structured scene output.

### Standard formats — read `references/ugc-breakdown-reference.md`

- **Problem-Solution** — Hook is a pain-point confession. Structure: problem → discovery → proof → CTA. Best for skincare, supplements, beauty, anything where the customer has an existing frustration. ~20-22 seconds.
- **Demo-First** — Hook IS the product in motion. Structure: show → contextualize → explain → result → CTA. Best for gadgets, kitchen tools, anything visually compelling on its own. ~22-24 seconds.
- **Testimonial** — Hook is skeptic-framing ("I didn't think this would work"). Structure: skepticism → turn → detail → recommendation → CTA. Best for trust-forward categories — supplements, wellness. ~24-26 seconds. Lowest effect-density on purpose.

### Advanced formats — additional reference files required

- **Multi-environment** (single creator across multiple settings, day-in-life format) → also read `references/multi-environment-reference.md`. Use when the brief mentions "day in my life," "morning routine," "across my whole day," or when the product fits naturally into multiple moments. ~26-30 seconds, 3-5 environments.
- **Multi-creator dialogue** (two creators in conversation) → also read `references/multi-creator-reference.md`. Use when the brief mentions "two creators," "friend recommends," "duet," "reaction," or peer-to-peer endorsement. ~24-28 seconds, 3-5 alternating scenes.
- **Action-shot product demo** (creator physically using/applying/pouring the product) → also read `references/action-shot-reference.md`. Use when the brief involves visible product use beyond holding — pours, applications, scoops, sprays. The action mode (over-shoulder, close-hold, POV) is the critical decision. ~22-26 seconds.

If the brief could fit multiple formats, ask the user which they prefer. If the brief clearly points to one, use it and note the choice.

## Platform defaults

- Default platform: **TikTok** (9:16 vertical, 20-30s target).
- If user specifies Meta: 9:16, 15-20s target, slightly tighter pacing.

## Scene Output Structure

The output is FOCUSED. Give the user only what they need to copy into Seedance, plus the operational notes that prevent regen-cycle waste. Do NOT include strategic breakdowns, effects inventories, density maps, or energy arc analysis. The user is shipping ads, not studying craft.

Output exactly these sections, in order:

### 1. Format header (one line)

A single line at the top noting the format selected and why, e.g. "Action-shot product demo, close-hold application as the signature moment. ~22s, 4 scenes, single creator."

### 2. The shot prompts

Each shot in its own block, formatted as a copyable Seedance prompt:

```
SHOT [N] (00:XX–00:XX) — [Beat Name]
• EFFECT: [Primary framing/camera mode] + [performance cues]
• ENVIRONMENT: [Specific setting with 3-4 props]
• [Description of what the creator is doing in this shot]
• DIALOGUE: "[The exact line]"
• Delivery: [Tone, energy level, physical tells]
```

Guidelines:
- Each shot is 2-4 seconds in pacing terms (don't over-cut).
- Use the UGC effects taxonomy from the reference file. No cinematic effects.
- Dialogue sounds like a real person talking to a friend.
- Include performance cues: "slight head tilt on X," "natural eye break," "half-laugh."
- Describe environments with lived-in specificity.
- Mark the SIGNATURE MOMENT inline if relevant.

### 3. Word count check

A short list confirming each shot is under the per-scene word cap. Format:

```
- Shot 1 (5s): X words ✓
- Shot 2 (6s): X words ✓
```

This isn't filler — it's verification that the dialogue won't get compressed by Seedance.

### 4. Operational reminders

A numbered list of 3-5 production reminders specific to this ad. Examples of reminder types:
- Element setup ("Save both as Elements first")
- High-failure-mode shots ("Cap-already-off rule on Shot 2 — start with cap removed")
- Voice consistency ("Extract Shot 1 audio after generating, save as Audio Element for Shots 2+")
- Regen budget warnings ("Application shots typically need 3-5 regens")
- Caption reminders ("Add auto-captions in CapCut")

### 5. Variant suggestion (one line)

A single A/B test suggestion. E.g., "For a B-test, swap Shot 1's hook to a polarizing comparison frame: 'If you spent $30 on Summer Fridays last year, throw it out.'"

That's the entire output. Five sections, focused, copyable.

**Do NOT include:**
- A "Master Effects Inventory" listing every effect used
- An "Effects Density Map" segmenting the timeline
- An "Energy Arc" narrative analysis with three acts
- Strategic justification for why the ad works

These are internal craft considerations. The skill should USE them when writing the shot prompts, but should NOT surface them in the output. The user wants prompts they can ship, not a creative strategy deck.

## CRITICAL: Word-Count-to-Duration Calibration

**The single most operationally important rule.** Seedance 2.0 generates dialogue audio fitted to the duration window. Too many words for the duration = compressed, rushed, inhuman speech.

**Target: ~20-25 words per 10-second scene. Maximum 30.**

Natural conversational pace is ~150 words per minute. A 10-second scene = ~25 words at natural pace.

**Rules:**
- 10-second scene: 20-25 words MAX
- 8-second scene: 15-20 words MAX
- 6-second scene: 10-15 words MAX
- Multi-environment scenes (often 6-7 seconds): 15-20 words

If your dialogue exceeds these limits, CUT before generating.

## Higgsfield Element Architecture (REQUIRED)

For any multi-scene UGC ad, the user MUST save creators and products as Elements in Higgsfield BEFORE generating scenes. Without saved Elements, the creator's face drifts and the product wrapper distorts.

Always remind the user to:

1. **Save the creator as a Character Element** — upload the image generated in Step 1, set Category to "Character," name as `@creator_name`, add a description that locks face/hair/wardrobe.
2. **Save the product as a Prop Element** — upload the product image, set Category to "Prop" (or "Auto"), name as `@product_name`, add a description listing every wrapper text element, color, and logo exactly as they appear.
3. **Reference Elements in prompts using `@handle` syntax** — `@creator_a is holding @product_bar` not `a woman is holding a protein bar`.
4. **Select all required Elements before each generation.**

For multi-creator ads, save BOTH creators as separate Character Elements.

## Eating, Unwrapping, and Other High-Failure-Mode Actions

KNOWN HIGH-FAILURE shot types in Seedance 2.0. Default to AVOIDING them:

1. **Eating shots** — chew motion looks uncanny, product morphs mid-bite. Default to hold-and-talk frames.
2. **Unwrapping shots** — wrapper physics break. If unwrapping is required, save TWO product references (sealed + unwrapped) on the same Element.
3. **Pouring/dispensing powders or unknown internals** — Seedance has no reference for what's inside a sealed product. Default to pre-prepared shots (the shaker is already filled, the cream is already on the finger).
4. **Hands holding small fiddly objects** — extra fingers, melted hands.

For categories that typically involve eating (protein bars, snacks, beverages-from-can), DEFAULT to hold-and-explain framing. The dialogue can reference the experience without performing it.

If the user insists on eating/unwrapping/pouring, warn them about the failure rate and recommend budgeting 4-6 regenerations on those scenes.

## Voice Consistency Across Scenes

Seedance 2.0 generates dialogue audio fresh on each generation. Even with a saved Character Element, voice timbre can drift between generations.

**Mitigation strategies, in order of preference:**

1. **Use Seedance's audio reference upload (RECOMMENDED for multi-scene ads).** After generating Scene 1, extract the audio as MP3, save it as an Audio Element in Higgsfield (`@creator_voice`), and reference it in every subsequent scene's prompt. This locks the voice across all scenes.
2. **Regenerate until voices match.** Variance is high — most mismatches resolve in 2-3 regenerations.
3. **Use Higgsfield Audio's Voice Changer post-generation.** Save a custom voice and run all scenes through Voice Changer.
4. **Replace audio entirely** with ElevenLabs. Last resort — loses lip-sync.

The skill should mention voice consistency as a known caveat in any output where multiple scenes are generated, and recommend extracting Scene 1's audio for use as a reference in Scenes 2+.

## UGC Creative Principles

These principles guide every prompt:

1. **The hook happens in 1.5 seconds or it doesn't happen.** Pattern-interrupt line, visual surprise, or product-in-motion.
2. **Alternate face-shots and product-shots.** The face earns trust. The product earns belief.
3. **Specificity beats superlatives.** "Ten seconds" beats "super fast." "3pm crash" beats "more energy."
4. **The honest caveat is the trust anchor.** "I didn't think this would work." "I don't even care if it's placebo." Include at least one per ad.
5. **The CTA is casual, not urgent.** "Just try it." "Go get one."
6. **Low-density beats high-density.** UGC runs 2-4 effects per 3 seconds, maximum.
7. **Write dialogue the way a 26-year-old texts.** Contractions, incomplete sentences, filler words, self-interruptions.
8. **The product appears on screen within the first 6 seconds.**
9. **No music.** Real UGC ads don't have music beds. Ambient room tone is the soundtrack.
10. **Captions carry sound-off viewers.** ~85% of TikTok and Reels viewers watch with sound off. Always recommend CapCut auto-captions.

## Duration calibration

- **15-20s (Meta default)**: 6-8 shots, tighter pacing, one SIGNATURE MOMENT.
- **20-26s (TikTok default)**: 8-10 shots, full format arc, 1-2 SIGNATURE MOMENTS.
- **26-35s** (multi-environment, multi-creator, narrative arc): 10-14 shots, 2-3 SIGNATURE MOMENTS.

Default to **22 seconds** for TikTok, **18 seconds** for Meta if duration isn't specified.

## Brand foundation integration

If `brand/brand-dna.md`, `brand/brand-voice.md`, or `brand/icp-cards.md` exist, read them BEFORE writing any prompt:

- **Brand DNA** — pull product positioning, category, primary differentiator. The SIGNATURE MOMENT should land on the brand's core claim.
- **Brand Voice** — match dialogue tone to the brand's voice rules.
- **ICP Cards** — match the creator persona AND the language to the target customer.

## Example workflow

**User says:** "Help me make a UGC ad for Liquid Death."

**You do:**
1. Recognize the user needs both Step 1 and Step 2.
2. Read brand foundation files if present.
3. Read `references/character-creation-reference.md` to identify the archetype (likely Active Adult or Desk Worker for Liquid Death).
4. Output Step 1 first: the ChatGPT Images 2.0 character prompt.
5. Tell the user: "Generate this in ChatGPT, save the result as `@creator_liquiddeath` Character Element in Higgsfield, then come back and we'll write the scene prompts."
6. When the user returns with their saved creator, read the relevant scene reference file and output Step 2.

**User says:** "I already have my creator. Write me the Seedance scene prompts for Liquid Death — testimonial format."

**You do:**
1. Skip Step 1.
2. Read `references/ugc-breakdown-reference.md` for testimonial format.
3. Output Step 2 directly.

## Output format

Output everything as plain markdown in chat. Do not save to a file unless the user asks.

For Step 1 (character prompt): output the full ChatGPT prompt in a code block, followed by a brief note (archetype identified, reminder to save as Element).

For Step 2 (scene prompts): output the complete four-section structure, followed by a short note covering:
- The format selected
- A reminder to save Character + Prop Elements before generating
- A reminder to extract Scene 1's audio for voice consistency in later scenes
- A one-line variant suggestion
