# GDD-02 — Format, compatibility, installation (APPROVED)

Status: APPROVED — decisions approved by owner 2026-11-21. Technical compatibility remains UNVERIFIED.

## Research findings
- vivo .itz theme packages exist, but exact accepted manifest and asset layout for iQOO 15R OriginOS 7 Global remain unverified.
- zTheme: https://github.com/St-Dct/zTheme ; project explicitly targets Chinese OriginOS 4/5/6 and warns Global may not work.
- VFont: https://github.com/SubmitCodes/VFont ; physical test reported for Chinese OriginOS 7, Global experimental; uses Shizuku without root.
- Official OriginOS 7 feature page: https://www.vivo.com/en/originos/ ; dynamic translucency is an OS feature, not proof third-party system UI themes can install.

## Approved technical plan
1. Inventory firmware build and available native Themes app/import UI without changing system settings.
2. Obtain lawful compatible sample .itz, inspect archive, manifest, assets, mapping, and license. No invented schema.
3. Create minimal candidate .itz with a few icons and wallpaper; build reproducibly; validate archive.
4. Test native import first, then optionally evaluate VFont + Shizuku with explicit owner permission. Avoid root, bootloader unlock, firmware downgrade, system-app replacement or privileged destructive hacks.
5. Record results per component: icons, wallpaper, lockscreen, AOD, notification shade, control center, settings, status bar. Unsupported means unsupported, not DONE.
6. If full .itz fails, offer reversible icon-pack / launcher or OS-native customization fallback, preserving Liquid Graphite look where possible.
7. Save device test report with screenshots, install and rollback steps, exact firmware build, and reproducible release checks.

## Approved decisions
- FORMAT-001 A: research-first minimal .itz proof of concept before full asset production.
- INSTALL-001 A: native theme manager first; VFont + Shizuku only if needed, after separate owner approval for actual device actions.
- FALLBACK-001 A: reversible icons+wallpaper alternative if Global firmware blocks full theme.
- SAFETY-001 A: no root, bootloader unlock, system-app swaps or firmware changes.

## Exit criteria
No claim of working install without physical test on user's iQOO 15R OriginOS 7 Global. Every verified outcome must be documented. GDD-03 implementation starts only after the feasibility gate is documented; an unsupported Global theme path must be explicitly marked and fallback agreed.
