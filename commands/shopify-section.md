Create a new fully customizable Shopify Dawn theme section.

Section name/description: $ARGUMENTS

Requirements:
- Create a Liquid section file in `sections/` with a complete {% schema %} block
- Every visual property must be customizable: padding top/bottom, background color, text color, font size, font weight
- If the section contains benefits or icons, extract them into a separate snippet in `snippets/`
- Schema settings must include: section header (text, size, color, weight), content blocks, spacing controls
- Use CSS custom properties for all theme values — no hardcoded colors or sizes
- Mobile-first responsive layout
- Follow the existing Dawn theme CSS naming conventions
- Output the complete file(s) with all code, ready to drop in

After creating the file(s), ask: "Push to draft theme?"
