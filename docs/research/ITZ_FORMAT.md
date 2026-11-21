# ITZ format research — OriginOS / Vivo theme packages

**Date:** 2026-11-21  
**Scope:** Evidence from inspectable samples and public sources.  
**Target device:** iQOO 15R, OriginOS 7 **Global**.  
**Status:** Chinese/legacy `.itz` **structure partially OBSERVED**. Acceptance on OriginOS 7 Global **BLOCKED / UNVERIFIED**.

---

## Verdict (read first)

| Claim | Status |
| --- | --- |
| `.itz` is often a ZIP renamed to `.itz` | **CONFIRMED** (samples + multiple independent sources) |
| Typical root entries: `description.xml`, `icons/`, `launcher/`, `wallpaper/`, `preview/`, optional `key` | **OBSERVED** on Chinese/legacy samples |
| Exact manifest / signing rules accepted by **OriginOS 7 Global** Themes | **UNVERIFIED** |
| Native third-party `.itz` import works on iQOO 15R Global | **BLOCKED** — no device evidence; community reports Global theme depth is limited |
| Opaque `key` file generation algorithm | **UNKNOWN** |
| Invented schema safe to ship as “working theme” | **NO** — do not claim |

**Gate:** Do not generate a full Liquid Graphite icon set until OriginOS 7 Global import/apply is confirmed on the physical iQOO 15R (or owner accepts FALLBACK-001).

---

## Sources (URL, date accessed, license, firmware claims)

| Source | URL | Accessed | License | Firmware claim | Evidence quality |
| --- | --- | --- | --- | --- | --- |
| Sample archive (unpacked themes) | https://github.com/copperate/vivo-theme-pack-for-origin-os | 2026-11-21 | **No LICENSE file** — treat assets as non-redistributable | README only: zip folder → rename `.itz` | **Inspectable tree**; provenance 2023-02-17 upload; Chinese-app icon set |
| zTheme | https://github.com/St-Dct/zTheme | 2026-11-21 | GPL-3.0 | Targets OriginOS **4/5/6**; thumbnail/preview guidance | Tooling claims; **not** OriginOS 7 Global proof |
| VFont | https://github.com/SubmitCodes/VFont | 2026-11-21 | Komorebi 2.0.0 | Physically verified Chinese OriginOS 7 (X200 Ultra); **Global experimental** | Strong for CN OS7; Global explicitly experimental |
| VFont themes doc | https://github.com/SubmitCodes/VFont/blob/main/docs/themes.md | 2026-11-21 | same | ZIP + root `description.xml`; validates XML/checksums | Describes consumer of `.itz`, not Global Themes UI |
| Reddit CN-only install guide | https://www.reddit.com/r/Vivo/comments/1lwajr2/ | 2026-11-21 | user content | **Chinese OriginOS 4/5 only**; warns against Global/Funtouch | Explicit Global exclusion |
| iQOO community wishlist | https://community.iqoo.com/in/thread/164318 | 2026-11-21 | community | Global themes limited vs China deep UI themes | Anecdotal product gap report |
| Official OriginOS page | https://www.vivo.com/en/originos/ | 2026-11-21 | vivo marketing | Dynamic translucency etc. | **Not** third-party `.itz` import documentation |
| FileXT / Indonesian edit guides | filext.com; lutfisyafii.com | 2026-11-21 | third-party | General Funtouch/Vivo ZIP layout folklore | Secondary; corroborates ZIP + folder names |

Chinese vs Global claims must stay separated. Extension `.itz` alone is **not** compatibility proof.

---

## Sample inspection (commands & observations)

Samples cloned for **read-only inspection** (not copied into this repository as theme assets):

```text
git clone --depth 1 https://github.com/copperate/vivo-theme-pack-for-origin-os.git
# commit 3d07199894845c5b4e033cfb378a13b6b54ad2b8 (2023-02-17)
# trees: bmw.itz/  RePure.itz/  (directories named *.itz, not packed archives)
```

### Archive signature

- Packed form: **ZIP** (local file header / central directory), extension renamed to `.itz`.
- Unpacked sample repos store the **inner directory tree** already extracted.
- Secondary ITZ variants (non-ZIP) exist in the wild per FileXT; **not** used here.

### Observed root layout

**RePure.itz (richer):**

```text
description.xml
key                          # 768 ASCII hex-like chars; identical in both samples
icons/*.png                  # mostly 192×192; filename = package name
icons/dynamic_icon/...       # optional live calendar/weather/clock
icons/anim/...               # optional
launcher/                    # masks, backgrounds, iconsize.xml (bmw) / PNGs (both)
wallpaper/default_wallpaper.png
wallpaper/default_lock_wallpaper.png
preview/preview_launcher_0.png
preview/preview_lockscreen_0.png
preview_1959/                # alternate preview set (sample-specific)
```

**bmw.itz (partial):**

```text
description.xml
key
launcher/ (+ iconsize.xml, app_group_info.xml, masks/bgs)
wallpaper/
com.bbk.launcher2            # nested ZIP of launcher style demos
com.bbk.updater              # nested ZIP of updater UI skins
# no icons/ directory in this sample
```

Nested component packages (`com.android.settings`, `com.android.systemui`, `vivo`, …) appear in community guides as optional deep theming; **not fully enumerated** from a lawful OriginOS 7 Global sample.

### `description.xml` (observed fields)

Both samples contained the **same** XML body (suggests incomplete/copied metadata in the archive repo — treat IDs as untrusted):

| Field | Observed | Notes |
| --- | --- | --- |
| `theme/id`, `id3` | numeric store-like IDs | Unknown Global requirements |
| `version` | `3.0.0` | CDATA |
| `uid` | numeric | Unknown meaning |
| `titles/title@locale` | zh_CN | Locale-tagged |
| `authors`, `designers` | zh_CN | |
| `descriptions/description` | zh_CN marketing text | |
| `tool`, `toolversion` | editor identifiers | |
| `time` | epoch ms | |
| `md5result` | 32-hex | **Algorithm / coverage UNKNOWN** (whole archive? payload?) |
| `edition` | `2` | Unknown enum |

**VFont** documents that supported themes are ZIP-based with root `description.xml` and that archives are validated (names, paths, sizes, XML, checksums, resource types) before native apply — still **not** a Global Themes-app guarantee.

### Icon mapping convention (observed)

- Static icons: `icons/<packageName>.png`
- Dominant size in RePure: **192×192** PNG (also some 198×198 outliers)
- Dynamic widgets: `icons/dynamic_icon/<package>/manifest.xml` + resources
- Launcher chrome: `launcher/icon_mask.png`, `icon_bg_*.png`, `folder_icon.png`, optional `iconsize.xml`

No separate `appfilter.xml` inside these samples (unlike some Icon Pack Studio workflows). Mapping is **filename = Android package name**.

### Wallpaper / preview conventions (observed)

- Home: `wallpaper/default_wallpaper.png`
- Lock: `wallpaper/default_lock_wallpaper.png` (one sample had a fullwidth Unicode `。` in the filename — treat as sample defect)
- Preview: `preview/preview_launcher_0.png`, `preview/preview_lockscreen_0.png` (sample ~2000×4000)
- zTheme additionally documents optional root `thumbnail.png` and `preview/` for gallery cards

### Compression rules

- Outer package: ZIP (deflate observed in nested component zips).
- Exact compression method / store vs deflate requirements for Themes import: **UNVERIFIED**.
- Build scripts in this repo use standard `zipfile.ZIP_DEFLATED`.

### `key` file

- Length **768** ASCII characters (hex alphabet observed).
- Identical across both sample trees.
- Purpose likely store/signing related; **generation algorithm UNKNOWN**.
- Copying third-party `key` material into a Liquid Graphite release is **not** done here.
- Missing/invalid `key` may cause Themes/VFont rejection — **blocker for claiming a complete authentic package**.

### Path / Style variants

Community Chinese-ROM tutorials mention assets either at archive root (`icons`, `launcher`) or under `Style/<n>/`. Inspected samples used **root** layout (no `Style/`). Which layout OriginOS 7 Global expects: **UNVERIFIED**.

---

## Unknowns (explicit)

1. Whether iQOO 15R OriginOS 7 Global Themes app accepts sideloaded `.itz` at all.
2. Required `description.xml` schema version / `edition` / `md5result` computation.
3. How to lawfully mint a valid `key`.
4. Global package-name differences vs Chinese system apps (Dialer/MMS/Gallery/Camera).
5. Whether nested System UI packages are honored on Global.
6. Lockscreen engine / AOD resources for OS7 Global.
7. Official vivo developer documentation for third-party `.itz` (none found on vivo.com/originos).

---

## What this repository ships for T-001

- **Research docs** (this file + install methods).
- **Original TEST assets** under `assets/test/` (not scraped from sample themes).
- **Build/validate tools** that assemble a **structural candidate** matching observed Chinese root layout.
- Candidate is labeled **TEST / CANDIDATE / NOT DEVICE-VERIFIED**. It is **not** a released or “working” theme.
- Full icon production remains **blocked** pending Global feasibility results.

If device testing shows native Global import impossible, treat full `.itz` path as **UNSUPPORTED** and proceed under FALLBACK-001 (reversible icons + wallpaper).
