---
name: Never wipe outputs folder
description: Do not rm -rf outputs before regenerating ads — only overwrite specific templates being regenerated
type: feedback
---

Never delete the entire outputs folder before regenerating ads. Only overwrite the specific templates being re-run.

**Why:** User lost 40 generated ads when I ran `rm -rf outputs` before a full regeneration that got interrupted. The old images were unrecoverable (not a git repo).

**How to apply:** When re-running generate_ads.py, use `--templates X,Y,Z` to target only the ones that need fixing. If a full re-run is truly needed, rename the old outputs folder as a backup first (e.g. `outputs-backup`) rather than deleting it.
