# OriginOS 7 Liquid Graphite — Roadmap

Target: iQOO 15R, OriginOS 7 Global. Strict stage order; approved GDDs are immutable without owner approval.

- [x] GDD-01 Visual direction approved (docs/GDD-01.md)
- [ ] GDD-02 ITZ format, install feasibility and device compatibility (draft awaiting approval)
- [ ] GDD-03 Icon inventory, app/package mapping, generation pipeline
- [ ] GDD-04 Wallpaper, lock screen, AOD where supported
- [ ] GDD-05 System UI components where supported
- [ ] GDD-06 Reproducible packaging and validation
- [ ] GDD-07 On-device installation, rollback and smoke tests
- [ ] GDD-08 Release artifact and user installation guide

Rule: A generated .itz is a candidate until imported and applied successfully on the actual device. Global firmware may limit scope. Record evidence, do not claim unsupported changes. Prefer no-root and reversible procedures.
