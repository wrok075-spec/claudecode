#!/usr/bin/env python3
"""
Static Ad Generator — Phase 3: Image Generation via FAL API (Nano Banana 2)

Reads prompts.json from the brand folder, uploads product images to FAL,
and generates ads using Nano Banana 2's text-to-image and edit endpoints.

Usage:
    python generate_ads.py                          # Generate all 40 templates
    python generate_ads.py --templates 1,7,13,15    # Generate specific templates
    python generate_ads.py --resolution 2K          # Use 2K resolution
    python generate_ads.py --variations 3           # Generate 3 variations per template
    python generate_ads.py --dry-run                # Show what would be generated without calling API
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import base64
import mimetypes
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: 'requests' package required. Install with: pip install requests")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

FAL_KEY = os.environ.get("FAL_KEY", "")
FAL_QUEUE_URL = "https://queue.fal.run"
FAL_UPLOAD_URL = "https://fal.run/fal-ai/file-storage/upload"
T2I_ENDPOINT = "fal-ai/nano-banana-2"
EDIT_ENDPOINT = "fal-ai/nano-banana-2/edit"

POLL_INTERVAL = 2        # seconds between status checks
MAX_POLL_TIME = 180      # max seconds to wait per generation (higher for 2K + 4 images)
DEFAULT_RESOLUTION = "2K"
DEFAULT_OUTPUT_FORMAT = "png"


# ---------------------------------------------------------------------------
# FAL API helpers
# ---------------------------------------------------------------------------

def fal_headers():
    return {
        "Authorization": f"Key {FAL_KEY}",
        "Content-Type": "application/json",
    }


def upload_image_to_fal(image_path: str) -> str:
    """Upload a local image to FAL storage. Returns the hosted URL."""
    mime_type = mimetypes.guess_type(image_path)[0] or "image/png"

    with open(image_path, "rb") as f:
        image_data = f.read()

    # FAL accepts multipart upload or base64 data URIs.
    # Using the REST upload endpoint:
    resp = requests.post(
        "https://fal.run/fal-ai/file-storage/upload",
        headers={"Authorization": f"Key {FAL_KEY}"},
        files={"file": (os.path.basename(image_path), image_data, mime_type)},
    )

    if resp.status_code != 200:
        # Fallback: try base64 data URI approach (always works with FAL)
        b64 = base64.b64encode(image_data).decode("utf-8")
        return f"data:{mime_type};base64,{b64}"

    data = resp.json()
    return data.get("url", data.get("file_url", ""))


def submit_generation(endpoint: str, payload: dict) -> str:
    """Submit a generation request to FAL queue. Returns request_id."""
    url = f"{FAL_QUEUE_URL}/{endpoint}"
    resp = requests.post(url, headers=fal_headers(), json=payload)
    resp.raise_for_status()
    data = resp.json()
    return data["request_id"]


def poll_status(endpoint: str, request_id: str) -> dict:
    """Poll until the request is completed. Returns the result."""
    # FAL status/result URLs use the parent app path, stripping any sub-route like /edit
    base_endpoint = endpoint.split("/edit")[0]
    url = f"{FAL_QUEUE_URL}/{base_endpoint}/requests/{request_id}/status"
    elapsed = 0

    while elapsed < MAX_POLL_TIME:
        resp = requests.get(url, headers=fal_headers())
        resp.raise_for_status()
        status_data = resp.json()
        status = status_data.get("status", "")

        if status == "COMPLETED":
            # Fetch the actual result
            result_url = f"{FAL_QUEUE_URL}/{base_endpoint}/requests/{request_id}"
            result_resp = requests.get(result_url, headers=fal_headers())
            result_resp.raise_for_status()
            return result_resp.json()
        elif status == "FAILED":
            error = status_data.get("error", "Unknown error")
            raise RuntimeError(f"Generation failed: {error}")

        time.sleep(POLL_INTERVAL)
        elapsed += POLL_INTERVAL

    raise TimeoutError(f"Generation timed out after {MAX_POLL_TIME}s")


def download_image(image_url: str, save_path: str):
    """Download an image from URL to local path."""
    resp = requests.get(image_url, stream=True)
    resp.raise_for_status()
    with open(save_path, "wb") as f:
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)


# ---------------------------------------------------------------------------
# Template name mapping
# ---------------------------------------------------------------------------

TEMPLATE_NAMES = {
    1: "headline",
    2: "offer-promotion",
    3: "testimonials",
    4: "features-benefits",
    5: "bullet-points",
    6: "social-proof",
    7: "us-vs-them",
    8: "before-after-ugc",
    9: "negative-marketing",
    10: "press-editorial",
    11: "pull-quote-review",
    12: "lifestyle-colorway",
    13: "stat-surround-hero",
    14: "bundle-showcase",
    15: "social-comment-screenshot",
    16: "curiosity-gap-testimonial",
    17: "verified-review-card",
    18: "stat-surround-flatlay",
    19: "highlighted-testimonial",
    20: "advertorial-editorial",
    21: "bold-statement",
    22: "flavor-story",
    23: "long-form-manifesto",
    24: "product-comment-callout",
    25: "us-vs-them-color-split",
    26: "stat-callout-lifestyle",
    27: "benefit-checklist",
    28: "feature-arrow-callout",
    29: "ugc-viral-post",
    30: "hero-statement-icon-bar",
    31: "comparison-grid",
    32: "ugc-story-callout",
    33: "faux-press-screenshot",
    34: "faux-iphone-notes",
    35: "hero-product-stat-bar",
    36: "whiteboard-before-after",
    37: "hero-statement-promo",
    38: "ugc-lifestyle-review-split",
    39: "curiosity-gap-scroll-stopper",
    40: "post-it-note-style",
}


# ---------------------------------------------------------------------------
# Main generation logic
# ---------------------------------------------------------------------------

def generate_ads(
    brand_dir: str,
    templates_filter: list[int] | None = None,
    resolution: str = DEFAULT_RESOLUTION,
    num_variations: int = 1,
    dry_run: bool = False,
):
    brand_path = Path(brand_dir)
    prompts_file = brand_path / "prompts.json"
    product_images_dir = brand_path / "product-images"
    outputs_dir = brand_path / "outputs"

    # Validate
    if not prompts_file.exists():
        print(f"Error: {prompts_file} not found. Run Phase 2 first.")
        sys.exit(1)

    if not FAL_KEY and not dry_run:
        print("Error: FAL_KEY environment variable not set.")
        print("Set it with: export FAL_KEY='your-key-here'")
        sys.exit(1)

    # Load prompts
    with open(prompts_file) as f:
        prompts_data = json.load(f)

    brand_name = prompts_data.get("brand", "unknown")
    prompts = prompts_data.get("prompts", [])

    if templates_filter:
        prompts = [p for p in prompts if p["template_number"] in templates_filter]

    print(f"\n{'='*60}")
    print(f"  Static Ad Generator — {brand_name}")
    print(f"  Templates: {len(prompts)} | Resolution: {resolution} | Variations: {num_variations}")
    print(f"{'='*60}\n")

    # Upload product images once (reuse URLs across all generations)
    product_image_urls = []
    if product_images_dir.exists() and not dry_run:
        image_files = sorted([
            f for f in product_images_dir.iterdir()
            if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
        ])
        if image_files:
            print(f"Uploading {len(image_files)} product image(s) to FAL storage...")
            for img_file in image_files:
                try:
                    url = upload_image_to_fal(str(img_file))
                    product_image_urls.append(url)
                    print(f"  ✓ {img_file.name}")
                except Exception as e:
                    print(f"  ✗ {img_file.name}: {e}")
            print()
        else:
            print("Warning: No product images found in product-images/ folder.\n")

    # Track results
    results = []
    total = len(prompts) * num_variations  # 1 image per call now
    completed = 0
    failed = 0

    for prompt_entry in prompts:
        tpl_num = prompt_entry["template_number"]
        tpl_name = prompt_entry.get("template_name", TEMPLATE_NAMES.get(tpl_num, f"template-{tpl_num}"))
        prompt_text = prompt_entry["prompt"]
        aspect_ratio = prompt_entry.get("aspect_ratio", "1:1")
        needs_images = prompt_entry.get("needs_product_images", True)

        # Create output folder
        folder_name = f"{tpl_num:02d}-{tpl_name}"
        output_folder = outputs_dir / folder_name
        output_folder.mkdir(parents=True, exist_ok=True)

        # Save prompt text
        with open(output_folder / "prompt.txt", "w") as f:
            f.write(prompt_text)

        print(f"[{tpl_num:02d}] {tpl_name}")

        if dry_run:
            print(f"     → DRY RUN: would generate {num_variations} variation(s) × 4 images each")
            print(f"     → Aspect: {aspect_ratio} | Product images: {needs_images}")
            print(f"     → Endpoint: {'edit' if (needs_images and product_image_urls) else 't2i'}")
            print()
            continue

        for var_idx in range(num_variations):
            var_label = f"v{var_idx + 1}" if num_variations > 1 else "v1"

            # Determine endpoint and payload
            num_images = 1  # 1 image per call — use --variations for more
            if needs_images and product_image_urls:
                endpoint = EDIT_ENDPOINT
                payload = {
                    "prompt": prompt_text,
                    "image_urls": product_image_urls,
                    "aspect_ratio": aspect_ratio,
                    "num_images": num_images,
                    "output_format": DEFAULT_OUTPUT_FORMAT,
                    "resolution": resolution,
                    "safety_tolerance": "5",
                    "limit_generations": False,
                }
            else:
                endpoint = T2I_ENDPOINT
                payload = {
                    "prompt": prompt_text,
                    "aspect_ratio": aspect_ratio,
                    "num_images": num_images,
                    "output_format": DEFAULT_OUTPUT_FORMAT,
                    "resolution": resolution,
                    "safety_tolerance": "5",
                    "limit_generations": False,
                }

            try:
                # Submit
                request_id = submit_generation(endpoint, payload)
                print(f"     → Submitted ({var_label}) [id: {request_id[:12]}...]")

                # Poll
                result = poll_status(endpoint, request_id)
                images = result.get("images", [])

                if not images:
                    print(f"     ✗ No images returned")
                    failed += 1
                    continue

                # Save only the first image from the response (FAL sometimes returns extras)
                img_url = images[0].get("url", "")
                if img_url:
                    save_name = f"{tpl_name}_{var_label}.{DEFAULT_OUTPUT_FORMAT}"
                    save_path = output_folder / save_name
                    download_image(img_url, str(save_path))
                    print(f"     ✓ Saved: {save_name}")
                    completed += 1
                    results.append({
                        "template": tpl_num,
                        "name": tpl_name,
                        "variation": var_label,
                        "file": str(save_path),
                        "fal_url": img_url,
                    })
                else:
                    print(f"     ✗ No image URL in response")
                    failed += 1

            except Exception as e:
                print(f"     ✗ Error: {e}")
                failed += 1

        print()

    # Summary
    if not dry_run:
        print(f"\n{'='*60}")
        print(f"  Generation Complete")
        print(f"  ✓ Completed: {completed}/{total}")
        if failed:
            print(f"  ✗ Failed: {failed}/{total}")
        print(f"  Output: {outputs_dir}/")
        print(f"{'='*60}\n")

        # Save results manifest
        manifest = {
            "brand": brand_name,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "resolution": resolution,
            "total_generated": completed,
            "total_failed": failed,
            "results": results,
        }
        manifest_path = outputs_dir / "manifest.json"
        with open(manifest_path, "w") as f:
            json.dump(manifest, f, indent=2)
        print(f"Manifest saved: {manifest_path}")

        # Generate HTML gallery
        generate_gallery(outputs_dir, brand_name, results)


def generate_gallery(outputs_dir: Path, brand_name: str, results: list):
    """Generate an HTML gallery of all generated ads."""
    html_parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{brand_name} — Static Ad Gallery</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0a0a0a; color: #fff; padding: 2rem; }}
  h1 {{ font-size: 1.8rem; margin-bottom: 0.5rem; }}
  .meta {{ color: #888; margin-bottom: 2rem; font-size: 0.9rem; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; }}
  .card {{ background: #1a1a1a; border-radius: 12px; overflow: hidden; }}
  .card img {{ width: 100%; display: block; }}
  .card .info {{ padding: 1rem; }}
  .card .info h3 {{ font-size: 0.95rem; margin-bottom: 0.3rem; }}
  .card .info p {{ font-size: 0.8rem; color: #888; }}
</style>
</head>
<body>
<h1>{brand_name} — Static Ad Gallery</h1>
<p class="meta">Generated {time.strftime("%B %d, %Y")} · {len(results)} ads</p>
<div class="grid">
"""]

    for r in results:
        file_path = Path(r["file"])
        rel_path = file_path.relative_to(outputs_dir)
        tpl_num = r["template"]
        tpl_name = r["name"].replace("-", " ").title()
        html_parts.append(f"""  <div class="card">
    <img src="{rel_path}" alt="Template {tpl_num}: {tpl_name}" loading="lazy">
    <div class="info">
      <h3>#{tpl_num:02d} — {tpl_name}</h3>
      <p>{r['variation']}</p>
    </div>
  </div>
""")

    html_parts.append("</div>\n</body>\n</html>")

    gallery_path = outputs_dir / "gallery.html"
    with open(gallery_path, "w") as f:
        f.write("".join(html_parts))
    print(f"Gallery saved: {gallery_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate static ads via Nano Banana 2")
    parser.add_argument(
        "--templates",
        type=str,
        default=None,
        help="Comma-separated template numbers to generate (e.g., 1,7,13,15)",
    )
    parser.add_argument(
        "--resolution",
        type=str,
        default=DEFAULT_RESOLUTION,
        choices=["0.5K", "1K", "2K", "4K"],
        help="Image resolution (default: 1K)",
    )
    parser.add_argument(
        "--variations",
        type=int,
        default=1,
        help="Number of variations per template (default: 1)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated without calling the API",
    )
    parser.add_argument(
        "--brand-dir",
        type=str,
        default=".",
        help="Path to the brand folder (default: current directory)",
    )

    args = parser.parse_args()

    templates_filter = None
    if args.templates:
        templates_filter = [int(t.strip()) for t in args.templates.split(",")]

    generate_ads(
        brand_dir=args.brand_dir,
        templates_filter=templates_filter,
        resolution=args.resolution,
        num_variations=args.variations,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
