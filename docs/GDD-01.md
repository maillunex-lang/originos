# GDD-01 — Liquid Graphite (APPROVED)

Date: 2026-11-21
Target: iQOO 15R, OriginOS 7, GLOBAL firmware.

## Approved decisions
- STYLE-001: B — Liquid Graphite. Smoked graphite, rounded-square icons, delicate glass edge, soft highlights and shadows.
- GLASS-001: moderate — visual glass effect approximately 30% (art direction, not a literal alpha requirement).
- ICON-001: original — retain recognizable brand colors and shapes; apply a consistent glass container treatment.
- SCOPE-001: full — target as much system theming as the device and firmware permit; do not promise unsupported elements.
- DEVICE-001: global — compatibility must be verified on the physical iQOO 15R.

## Non-negotiable acceptance criteria
1. Source assets and reproducible build scripts are versioned; no mockup is labeled an installable theme.
2. Build and validate a candidate .itz only after verifying a real compatible sample structure; inspect archive paths, manifests, icon mapping, previews and packaging.
3. Test on actual OriginOS 7 Global device; record import, apply, persistence after restart, rollback, and which components changed.
4. No root, bootloader unlocking, system-app replacement, firmware downgrade, or destructive workaround by default.
5. Preserve a backup/restore path and a safe icons+wallpaper fallback if full system theming is blocked.
6. Original app logos should be reproduced faithfully; verify redistribution rights before publishing third-party artwork.

## Visual guidance
Dark premium interface, graphite smoke glass, subtle refraction and bevels, restrained sheen, high contrast and legible icons. Preserve user's current rounded-square dark aesthetic. Never fake system-wide live blur with static PNGs.

## Status
APPROVED by owner. Implementation NOT STARTED. GDD-02 is technical research and compatibility verification; decisions there remain proposals until approved.
