# T-001 Report — OriginOS 7 Global `.itz` feasibility spike

**Date:** 2026-11-21  
**Branch:** `cursor/t-001-itz-feasibility-e78a`  
**Device under test:** iQOO 15R / OriginOS 7 Global — **not exercised by the agent**  
**GDD:** GDD-01 / GDD-02 left unchanged (approved text immutable)

---

## Executive verdict

| Gate | Result |
| --- | --- |
| Evidence-backed Chinese/legacy `.itz` ZIP layout | **PASS** (inspected samples) |
| OriginOS 7 Global native `.itz` acceptance | **BLOCKED / UNVERIFIED** |
| Opaque `key` / `md5result` algorithms | **UNKNOWN** |
| Minimal TEST structural candidate | **BUILT** — labeled TEST, not “working” |
| Full Liquid Graphite icon set | **NOT STARTED** (blocked until feasibility) |
| On-device import/apply/reboot/rollback | **NOT TESTED** (USER ACTION REQUIRED) |

**Honest blocker:** Format compatibility for **OriginOS 7 Global** is **not confirmed**. Community and tooling evidence covers Chinese OriginOS (and Global “experimental” for VFont). Do not treat the candidate `.itz` as a released theme.

---

## Evidence table

| Item | Status | Evidence |
| --- | --- | --- |
| `.itz` ≈ ZIP | **Confirmed** | Sample trees packable as ZIP; FileXT; VFont docs |
| Root `description.xml` | **Observed** | `bmw.itz`, `RePure.itz` in copperate sample repo |
| `icons/<package>.png` mapping | **Observed** | RePure 192×192 dominant |
| `launcher/` masks + `iconsize.xml` | **Observed** | bmw + RePure |
| `wallpaper/` + `preview/` | **Observed** | both samples; zTheme thumbnail note |
| `key` 768-char | **Observed / opaque** | identical in both samples; algorithm unknown |
| Nested `com.bbk.*` ZIP components | **Observed** | bmw only |
| Official vivo third-party `.itz` schema for OS7 Global | **Unsupported / not found** | vivo.com/originos marketing only |
| Native Themes import on iQOO 15R Global | **Unverified** | no device run |
| Deep System UI theming on Global | **Unverified** (likely limited) | iQOO community wishlist contrast CN vs Global |
| zTheme on OS7 Global | **Unverified** | README targets OS 4/5/6 |
| VFont theme apply on Global | **Unverified** | README: CN OS7 verified; Global experimental |
| CN iTheme/Docs overwrite guides | **Out of scope** | Explicitly not Global; safety policy |

---

## Sample provenance

| Field | Value |
| --- | --- |
| Repo | https://github.com/copperate/vivo-theme-pack-for-origin-os |
| Commit | `3d07199894845c5b4e033cfb378a13b6b54ad2b8` (2023-02-17) |
| License | **None declared** — sample **assets not redistributed** into this repo |
| Inspection | read-only clone under `/tmp`; structure documented in `docs/research/ITZ_FORMAT.md` |
| Other sources | zTheme GPL-3.0; VFont Komorebi 2.0.0; Reddit CN-only guide; iQOO community thread |

---

## Commands & outputs (agent environment)

```bash
git clone --depth 1 https://github.com/copperate/vivo-theme-pack-for-origin-os.git
find bmw.itz RePure.itz -maxdepth 2 -type f | head
# description.xml present; key length 768; RePure icons mostly 192x192
python3 tools/build_minimal_itz.py
python3 tools/validate_itz.py dist/LiquidGraphite_TEST_minimal.itz
```

Built artifact SHA-256: `2ba892768d08aa94bb9ef834279ee8924044b2c82ee1eff8b897e52e27e6b945`  
(also in `dist/LiquidGraphite_TEST_minimal.itz.sha256.json`). Structural validate: **PASS** with warning that opaque `key` is omitted.

---

## Artifacts

| Path | Role |
| --- | --- |
| `docs/research/ITZ_FORMAT.md` | Format research + unknowns |
| `docs/research/INSTALL_METHODS.md` | Native / VFont / fallback |
| `docs/tests/DEVICE_SMOKE_TEST.md` | Manual iQOO 15R procedure |
| `assets/test/**` | Original TEST icons (5), wallpaper, preview, launcher masks |
| `tools/build_minimal_itz.py` | Reproducible packager |
| `tools/validate_itz.py` | Structural validator |
| `dist/LiquidGraphite_TEST_minimal.itz` | TEST candidate (if built) |
| `dist/*.sha256.json` | Hash metadata |

Candidate labeling: **TEST_CANDIDATE**. `key` **omitted** (unknown algorithm — not forged).

---

## Device results (owner)

| Check | Result |
| --- | --- |
| Import | NOT TESTED |
| Icons | NOT TESTED |
| Wallpaper | NOT TESTED |
| Lockscreen | NOT TESTED |
| AOD | NOT TESTED |
| Notification shade | NOT TESTED |
| Control center | NOT TESTED |
| Status bar | NOT TESTED |
| Settings | NOT TESTED |
| Reboot persistence | NOT TESTED |
| Rollback | NOT TESTED |

---

## Blockers

1. **Global acceptance unproven** — cannot claim working install.
2. **`key` / `md5result` unknown** — may cause Themes/VFont rejection.
3. **No lawful redistributable official OS7 Global sample** with declared license.
4. **Package-name drift** on Global (Google apps vs `com.android.*` / `com.vivo.*`).
5. Device steps not run (by design).

---

## Rollback guidance

Use stock Themes restore / previous theme. If that fails, re-set wallpaper manually and restore prior icon style (Method C). No root recovery assumed.

---

## Recommended next step

1. Owner runs `docs/tests/DEVICE_SMOKE_TEST.md` on iQOO 15R (**no agent install**).
2. Report: native import UI present? import/apply outcomes per component.
3. If native path fails → choose **FALLBACK-001** or separately approve **VFont+Shizuku** experiment.
4. Only after a clear feasibility decision → open GDD-03 icon inventory / full generation.

**Roadmap:** GDD-02 implementation remains **open** until device evidence lands; marked blocked for Global confirmation in `ROADMAP.md`.
