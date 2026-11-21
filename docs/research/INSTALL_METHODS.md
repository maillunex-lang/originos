# Installation methods — OriginOS 7 Global (iQOO 15R)

**Date:** 2026-11-21  
**Policy:** SAFETY-001 — no root, bootloader unlock, firmware downgrade, system-app replacement, or protection bypass.  
**Owner actions on device require explicit permission.** This document does not install anything on the phone.

---

## Comparison

| Method | Root? | Components (claimed/typical) | Global OS7 evidence | Risk | Status for T-001 |
| --- | --- | --- | --- | --- | --- |
| **A. Native Themes app import** | No | Depends on firmware; China deep themes vs Global often wallpaper/icons only | **UNVERIFIED** on iQOO 15R | Low if stock UI only | **PRIMARY** — try first; USER ACTION |
| **B. VFont + Shizuku** | No (shell UID 2000) | Fonts, icons, local `.itz` components when APIs exist | Verified CN OriginOS 7; **Global experimental** | Medium (ADB/wireless debugging, app trust) | **OPTIONAL** — only with separate owner approval |
| **C. Fallback icons + wallpaper** | No | Home icons (launcher/icon pack or manual), static wallpaper | Feasible on virtually all Android | Low; reversible | **APPROVED FALLBACK** if A/B fail |
| ~~CN iTheme downgrade / Docs overwrite tricks~~ | Often needs old APKs / file replace | Full themes on **Chinese** ROM guides | Explicitly **not for Global** | High; violates SAFETY-001 spirit | **OUT OF SCOPE** |

---

## Method A — Native Themes (preferred)

### Intent
Use only the stock Themes / iTheme-equivalent UI on OriginOS 7 Global to import or apply a local `.itz`, if the UI exposes that path.

### Supported components (expected ranges)
- **Possible:** wallpaper, lock wallpaper, subset of icons.
- **Uncertain on Global:** notification shade, control center, status bar, settings chrome, AOD, full System UI.
- Community iQOO Global wishlist reports deep UI themes as China-only feature gap — treat as **hypothesis**, confirm on device.

### Steps (manual — USER ACTION REQUIRED)
1. Record **Settings → About phone**: model, OriginOS version, build number, Themes app version.
2. Screenshot current home + lock (backup reference).
3. Prefer stock “restore default / previous theme” before experimenting.
4. Copy candidate `.itz` to device storage (USB/MTP/Files) — **do not** auto-install from this agent.
5. Open Themes → look for **Import / Local / My themes / Open file**. If absent, record **UNSUPPORTED** for native import UI.
6. If import exists: import → preview → apply selected components only if offered.
7. Inspect home, lock, shade, control center, status bar, settings; reboot; check persistence; restore.

### Risks
- Partial apply leaving mixed look.
- Store account / theme license prompts.
- No import affordance on Global → method fails cleanly (preferred over hacks).

---

## Method B — VFont + Shizuku (optional)

### Sources
- https://github.com/SubmitCodes/VFont — physically verified **Chinese** OriginOS 7 (Vivo X200 Ultra); Global **experimental**.
- Requires [Shizuku](https://shizuku.rikka.app/) shell mode (UID 2000), stock Vivo services, ARM64, Android 14+ for native writes.

### What it can do (per upstream docs)
- Preview/apply local `.itz` components when native APIs allow.
- Per-component apply/restore; keeps first backup for theme restore.
- Rejects themes with bundled fonts; validates ZIP + `description.xml`.

### Risks
- Experimental on Global: features may be blocked by capability checks.
- Requires enabling wireless debugging / ADB authorization.
- Trust boundary: third-party APK + shell privileges.
- Must keep VFont data intact for restore.

### Policy
Do **not** run Method B until the owner separately approves installing VFont/Shizuku and authorizing shell access on the iQOO 15R.

---

## Method C — Reversible icons + wallpaper fallback (FALLBACK-001)

If full `.itz` fails or Global blocks system theming:

1. Set Liquid Graphite **TEST** wallpaper via stock Wallpaper picker (from `assets/test/wallpaper/`).
2. For icons, prefer stock Themes icon styles **or** a reversible third-party launcher / icon pack **only** if owner accepts leaving stock launcher animations.
3. Keep originals: screenshot + note prior wallpaper; avoid clearing launcher data.
4. Preserve Liquid Graphite look (smoked graphite, rounded-square glass) within whatever the OS allows.

This path satisfies GDD “safe icons+wallpaper fallback” without claiming unsupported System UI changes.

---

## Explicitly disallowed (this project)

- Root / Magisk / LSPosed for themes.
- Bootloader unlock.
- Firmware downgrade or China ROM flash to gain themes.
- Replacing/signing system Themes APKs or exploiting Docs/iTheme overwrite chains from Chinese tutorials.
- Automatic push/install to the phone from CI or this agent.

---

## Recommended order on iQOO 15R

1. Inventory firmware + Themes UI (Method A discovery) — **no theme apply yet**.
2. If local import exists → smoke-test minimal **TEST** candidate.
3. If import missing or apply fails → document **UNSUPPORTED** components.
4. Owner decides: approve Method B exploration **or** adopt Method C fallback.
5. Only after a positive feasibility gate → GDD-03 full icon pipeline.
