#!/usr/bin/env python3
"""
Kiwinz Ad Copy Generator — Frustration / Problem-Solution Ads

Generates 5 ad variations × 10 hooks each (50 total) for any product.
Uses Claude API (Anthropic) to write long-form ad copy.

Usage:
  export ANTHROPIC_API_KEY="sk-ant-..."
  python3 generate_ad_copy.py --brand-dir brands/kiwinz-professional
  python3 generate_ad_copy.py --brand-dir brands/kiwinz-professional --variations 3 --hooks 5

Output:
  brands/<brand>/ad-copy/
    ├── variation_1.md
    ├── variation_2.md
    ├── ...
    ├── all_hooks.md
    └── full_output.md
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not installed. Run: pip3 install anthropic")
    sys.exit(1)


BANNED_WORDS = [
    "embrace", "unlock", "game changer", "game-changer", "transformative",
    "transform your", "delve", "elevate", "dive into", "crucial",
    "secret weapon", "unleash", "empower", "revolutionize", "groundbreaking",
    "cutting-edge", "cutting edge", "paradigm shift", "synergy", "leverage",
    "holistic", "seamless", "robust", "innovative", "disruptive",
    "next-level", "next level", "supercharge", "hack", "life hack",
    "journey", "deep dive", "unpack", "double down", "lean into",
    "level up", "pivot", "circle back", "touch base", "low-hanging fruit",
    "move the needle", "at the end of the day", "it goes without saying",
    "needless to say", "in today's world", "in this day and age",
]

SYSTEM_PROMPT = """You are an expert direct-response copywriter who writes problem-solution ads for men's grooming and beauty products. Your style is:

RULES (ABSOLUTE — NEVER BREAK):
1. Every sentence in the body gets its own paragraph (one-sentence paragraphs, separated by blank lines).
2. Opening hooks are bold (**hook text here**).
3. Section titles/transitions are bold.
4. Every ad body must be 250+ words (not counting hooks).
5. NEVER use question sentences. Every sentence is declarative. No sentence ends with "?".
6. NEVER use these banned words/phrases: """ + ", ".join(f'"{w}"' for w in BANNED_WORDS) + """
7. Tone is plain-spoken, punchy, masculine, relatable. Short sentences. No fluff.
8. The ad follows this exact arc:
   - Problem Hook (the frustration, the failed attempt, the embarrassment)
   - Scenario Setup (relatable situation — present-feeling tense, vivid details)
   - Hope/Confidence Phase (man takes action, buys box dye, feels good about it)
   - Pain Escalation (things go wrong — ammonia smell, staining, flat color)
   - Ultimate Defeat (the result is worse than the grey — helmet hair, coworker notices)
   - Final Twist (salt in the wound — stain won't come off, barber cringes)
   - Bridge to Solution ("That's when..." / "That's a process no man should repeat")
   - Solution Presentation (how the product works — simple, clear, factual)
   - Social Proof (real-sounding review quote, "hundreds of men have switched")
   - Urgency/Scarcity Close (price going up, grab yours now, link)
9. Each hook must be a standalone bold declarative statement — no questions, no ellipsis.
10. Each variation must have a DIFFERENT frustration angle (box dye disaster, spray transfer, coworker noticing, barber reaction, wife/partner comment, mirror defeat, etc.)

OUTPUT FORMAT:
Return ONLY valid JSON with this structure:
{
  "variations": [
    {
      "variation_number": 1,
      "angle": "brief description of the frustration angle",
      "hooks": ["hook 1", "hook 2", ...],
      "body": "Full ad body text with \\n\\n between paragraphs"
    }
  ]
}
"""


def load_brand_info(brand_dir: Path) -> dict:
    """Load brand DNA and product info from brand directory."""
    info = {"brand_name": "", "product_name": "", "brand_dna": "", "product_details": ""}

    dna_path = brand_dir / "brand-dna.md"
    if dna_path.exists():
        info["brand_dna"] = dna_path.read_text()
        # Extract brand name from first heading
        for line in info["brand_dna"].split("\n"):
            if line.startswith("# "):
                info["brand_name"] = line.lstrip("# ").strip()
                break

    prompts_path = brand_dir / "prompts.json"
    if prompts_path.exists():
        data = json.loads(prompts_path.read_text())
        info["product_name"] = data.get("product", "")

    return info


def generate_copy(brand_info: dict, num_variations: int = 5, hooks_per: int = 10) -> dict:
    """Call Claude API to generate ad copy."""
    client = anthropic.Anthropic()

    user_prompt = f"""Write {num_variations} problem-solution ad variations for this product. Each variation needs {hooks_per} unique opening hooks.

PRODUCT: {brand_info.get('product_name', 'Hair Color Shampoo')}
BRAND: {brand_info.get('brand_name', 'Kiwinz Professional')}

BRAND & PRODUCT DETAILS:
{brand_info.get('brand_dna', 'Premium hair color shampoo for men. Ammonia-free. Argan oil + keratin. 5-in-1 formula. Covers 100% grey. 30 minute application on dry hair. No mixing, no gloves, no skin staining. Works on beard too.')}

IMPORTANT REMINDERS:
- {num_variations} variations, each with a DIFFERENT frustration angle
- {hooks_per} hooks per variation ({num_variations * hooks_per} total hooks)
- 250+ words per ad body
- One-sentence paragraphs only
- NO questions anywhere (no "?" in entire output)
- NO banned words
- Follow the exact Problem → Pain → Solution → Proof → Urgency arc
- Include a realistic-sounding customer review quote in each variation
- Return ONLY valid JSON"""

    print(f"\n  Calling Claude API ({num_variations} variations × {hooks_per} hooks)...")
    print(f"  This may take 30-60 seconds...\n")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )

    # Extract JSON from response
    text = response.content[0].text.strip()

    # Handle markdown code blocks
    if text.startswith("```"):
        text = text.split("\n", 1)[1]  # remove first line
        if text.endswith("```"):
            text = text[:-3]
        elif "```" in text:
            text = text[:text.rfind("```")]

    return json.loads(text)


def validate_copy(data: dict) -> list:
    """Check for banned words and questions."""
    issues = []
    for var in data.get("variations", []):
        vnum = var.get("variation_number", "?")
        full_text = " ".join(var.get("hooks", [])) + " " + var.get("body", "")
        full_lower = full_text.lower()

        # Check banned words
        for word in BANNED_WORDS:
            if word.lower() in full_lower:
                issues.append(f"  Variation {vnum}: contains banned phrase '{word}'")

        # Check for questions
        if "?" in full_text:
            issues.append(f"  Variation {vnum}: contains a question mark")

        # Check word count
        body_words = len(var.get("body", "").split())
        if body_words < 250:
            issues.append(f"  Variation {vnum}: body is only {body_words} words (need 250+)")

        # Check hook count
        hook_count = len(var.get("hooks", []))
        if hook_count < 10:
            issues.append(f"  Variation {vnum}: only {hook_count} hooks (need 10)")

    return issues


def save_output(data: dict, output_dir: Path, brand_info: dict):
    """Save all ad copy to markdown files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    variations = data.get("variations", [])
    all_hooks = []

    # Save individual variations
    for var in variations:
        vnum = var["variation_number"]
        hooks = var.get("hooks", [])
        body = var.get("body", "")
        angle = var.get("angle", "")
        all_hooks.extend(hooks)

        md = f"# Ad Variation {vnum}\n"
        md += f"**Angle:** {angle}\n\n"
        md += f"## Opening Hooks ({len(hooks)}):\n\n"
        for i, hook in enumerate(hooks, 1):
            md += f"{i}. **{hook}**\n"
        md += f"\n---\n\n## Ad Body\n\n"
        # Format body with bold first line
        paragraphs = [p.strip() for p in body.split("\n") if p.strip()]
        if paragraphs:
            md += f"**{paragraphs[0]}**\n\n"
            for p in paragraphs[1:]:
                md += f"{p}\n\n"

        filepath = output_dir / f"variation_{vnum}.md"
        filepath.write_text(md)
        print(f"  ✓ Saved: variation_{vnum}.md ({len(hooks)} hooks, {len(body.split())} words)")

    # Save all hooks consolidated
    hooks_md = f"# All Opening Hooks — {brand_info.get('product_name', 'Product')}\n\n"
    hooks_md += f"**Total: {len(all_hooks)} hooks across {len(variations)} variations**\n\n"
    for i, hook in enumerate(all_hooks, 1):
        hooks_md += f"{i}. **{hook}**\n"
    (output_dir / "all_hooks.md").write_text(hooks_md)
    print(f"  ✓ Saved: all_hooks.md ({len(all_hooks)} total hooks)")

    # Save full combined output
    full_md = f"# {brand_info.get('product_name', 'Product')} — Problem-Solution Ad Copy\n\n"
    full_md += f"**Generated:** {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}\n\n"
    full_md += f"**Variations:** {len(variations)} | **Hooks:** {len(all_hooks)} total\n\n"
    full_md += "---\n\n"
    for var in variations:
        vnum = var["variation_number"]
        filepath = output_dir / f"variation_{vnum}.md"
        full_md += filepath.read_text() + "\n---\n\n"
    (output_dir / "full_output.md").write_text(full_md)
    print(f"  ✓ Saved: full_output.md (complete document)")


def main():
    parser = argparse.ArgumentParser(description="Generate frustration/problem-solution ad copy")
    parser.add_argument("--brand-dir", required=True, help="Path to brand directory")
    parser.add_argument("--variations", type=int, default=5, help="Number of ad variations (default: 5)")
    parser.add_argument("--hooks", type=int, default=10, help="Hooks per variation (default: 10)")
    args = parser.parse_args()

    brand_dir = Path(args.brand_dir).resolve()
    if not brand_dir.exists():
        print(f"ERROR: Brand directory not found: {brand_dir}")
        sys.exit(1)

    # Check API key
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ERROR: ANTHROPIC_API_KEY not set. Export it first:")
        print('  export ANTHROPIC_API_KEY="sk-ant-..."')
        sys.exit(1)

    print("=" * 60)
    print("  Kiwinz Ad Copy Generator")
    print("  Frustration / Problem-Solution Format")
    print("=" * 60)

    # Load brand info
    brand_info = load_brand_info(brand_dir)
    print(f"\n  Brand: {brand_info.get('brand_name', 'Unknown')}")
    print(f"  Product: {brand_info.get('product_name', 'Unknown')}")
    print(f"  Variations: {args.variations} × {args.hooks} hooks = {args.variations * args.hooks} total hooks")

    # Generate
    data = generate_copy(brand_info, args.variations, args.hooks)

    # Validate
    issues = validate_copy(data)
    if issues:
        print("\n  ⚠ Validation warnings:")
        for issue in issues:
            print(f"    {issue}")

    # Save
    output_dir = brand_dir / "ad-copy"
    print(f"\n  Saving to: {output_dir}/\n")
    save_output(data, output_dir, brand_info)

    total_hooks = sum(len(v.get("hooks", [])) for v in data.get("variations", []))
    print(f"\n{'=' * 60}")
    print(f"  Done! {args.variations} variations, {total_hooks} hooks")
    print(f"  Output: {output_dir}/")
    print(f"{'=' * 60}\n")


if __name__ == "__main__":
    main()
