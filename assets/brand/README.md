# PEROVANO — Core 07 Brand Identity

## Concept
Core 07 is a geometric **P** built around an architectural central cube. The mark represents software architecture, systems integration, and reliability. This is a simplified flat vector reinterpretation of the selected Core 07 visual concept to remain legible at small sizes.

## Palette
- Navy: `#101B2B` (header, dark backgrounds)
- Steel: `#263B52` (secondary surfaces)
- Gold: `#B38C54` (primary brand accent)
- Champagne: `#D4B284` (highlight on dark surfaces)
- White: `#FFFFFF`
- Cloud: `#F3F5F7`

## Files
- `core-07-symbol.svg`: standalone transparent symbol.
- `core-07-symbol-navy.svg`: symbol on navy rounded square; main SVG favicon.
- `core-07-monochrome.svg`: one-color navy symbol.
- `perovano-horizontal-dark.svg`: horizontal lockup intended for dark headers.
- `perovano-horizontal-light.svg`: horizontal lockup for light surfaces and footer.

## Usage
- Keep the icon aspect ratio and clear space.
- Use the full horizontal brand signature for navigation, documents, and desktop layouts.
- Use the symbol alone for icon-sized usage; avoid reducing the full signature to favicon size.
- Do not recreate the metallic/shadow effects from the exploratory concept. Flat SVG is deliberate to preserve accessibility and reproducibility.
- Keep the brand attribution **Software Engineering & Consulting**.

## Integration
Both `/index.html` and `/en/index.html` load the correct header and footer vector assets and use `core-07-symbol-navy.svg` as SVG favicon. The previous .ico, PNG, and Apple touch icon assets remain in place as legacy fallbacks and should be regenerated to match Core 07 when binary assets are updated.

## QA
Verify the header on desktop/mobile, footer on light background, SVG favicon in modern browsers, and remaining legacy browser/touch icons before considering the visual identity fully consistent.
