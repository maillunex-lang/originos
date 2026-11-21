# Cursor task T-001 — OriginOS 7 Global .itz feasibility spike

Role: autonomous researcher/implementer. Repository: maillunex-lang/originos. Follow docs/GDD-01.md, docs/GDD-02.md and ROADMAP.md; approved decisions immutable without owner permission. Work on a feature branch and open a PR, never force-push or rewrite main.

## Goal
Establish evidence-based feasibility of importing a minimal Liquid Graphite .itz on iQOO 15R running OriginOS 7 Global. Do not generate a full icon pack yet.

## Work sequence
1. Read repository canon and inspect current tree. Research official vivo documentation and source repositories (zTheme, VFont, legitimate .itz samples). Record source URL, date, license, supported firmware and exact evidence; separate Chinese and Global ROM claims. Never treat extension alone as proof of compatibility.
2. Write docs/research/ITZ_FORMAT.md: archive signature, entries, manifests, XML fields, path conventions, icon package mapping, compression rules, theme metadata and any unknowns. Validate observations against actual inspectable samples; if unavailable, mark BLOCKED, do not fabricate schema.
3. Write docs/research/INSTALL_METHODS.md comparing native Themes import, VFont + Shizuku (optional, explicit owner permission), and reversible icons+wallpaper fallback. Explain supported components and risks. No root, unlock, downgrade, replacing system apps, or bypassing device protections.
4. Build minimal reproducible candidate ONLY if a legitimate sample demonstrates format: 3-5 representative app icons with recognisable colors and a single test wallpaper, clearly labeled TEST. Keep sources in assets/test and scripts in tools. Supply validation script that checks archive integrity, required files, mapping and image dimensions. Do not copy copyrighted assets without redistribution rights.
5. Create docs/tests/DEVICE_SMOKE_TEST.md with precise manual steps on iQOO 15R Global: record build number, native theme app version, backup original theme, import, apply, inspect home screen, reboot persistence, restore and log screenshots. Treat device-only steps as USER ACTION REQUIRED; no claims of having executed them.
6. Create docs/reviews/T-001_REPORT.md: evidence table (confirmed / unverified / unsupported), blockers, sample provenance, exact commands and outputs, artifact hashes, rollback, recommended next step. Update ROADMAP.md truthfully. Candidate .itz must never be labeled working/released until tested on the device.

## Exit criteria
- Evidence-backed format analysis or explicit BLOCKED report.
- Reproducible minimal candidate if feasible, otherwise no fake package.
- Safe device instructions and fallback strategy.
- Clear PASS/FAIL/NOT TESTED per import, icons, wallpaper, lockscreen, AOD, notification shade, control center, status bar, settings, reboot persistence and rollback.
- No changes to approved GDD text without owner permission; no full icon generation until feasibility decision.

## Handoff
Summarize branch/PR, files, commands, actual test evidence and exactly what owner must do on phone. Stop before device-side installation; wait for owner to report results.
