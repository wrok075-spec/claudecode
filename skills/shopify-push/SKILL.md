---
name: shopify-push
description: Push current Shopify theme changes.
---

Push current Shopify theme changes.

Target: $ARGUMENTS (use "draft" if not specified, "live" only if explicitly stated)

Steps:
1. Check git status or list recently modified files in the theme directory
2. If target is "draft": run `shopify theme push --theme [draft-theme-id]` or the appropriate CLI command
3. If target is "live": **confirm with the user first**, then push
4. Report which files were pushed and the theme editor preview URL
5. If there are errors, show them clearly and suggest fixes

Working directory: /Users/eapple/Desktop/claudecode/dawn-theme
