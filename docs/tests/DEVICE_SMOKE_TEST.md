# Device smoke test — iQOO 15R / OriginOS 7 Global

**Status of automation:** nothing in this repository installs or pushes to the phone.  
All steps below are **USER ACTION REQUIRED**.  
Record results in `docs/reviews/T-001_REPORT.md` (or a follow-up note). Until you run them, every component row stays **NOT TESTED**.

---

## Before you start

1. Confirm device: **iQOO 15R**, firmware **OriginOS 7 Global** (not Chinese ROM).
2. Charge > 50%; note you can unlock and open Themes / Settings.
3. Prefer Wi‑Fi; do **not** unlock bootloader or root.
4. Artifact (if built): `dist/LiquidGraphite_TEST_minimal.itz` — labeled **TEST CANDIDATE**, Global compatibility **UNVERIFIED**.
5. Optional SHA-256: see `dist/LiquidGraphite_TEST_minimal.itz.sha256.json`.

### Transfer only (no auto-install)

- USB file copy / MTP, or
- cloud/Files share you control  

Do **not** ask the agent to ADB-install themes or APKs unless you separately approve that later (VFont path).

---

## Step 0 — Inventory (no theme change)

| # | Action | Record |
| --- | --- | --- |
| 0.1 | Settings → About phone → model | |
| 0.2 | OriginOS / Android version | |
| 0.3 | Full **build number** | |
| 0.4 | Open Themes app → App info → **version name/code** | |
| 0.5 | Screenshot home + lock (baseline) | filenames |
| 0.6 | Note whether Themes has **Import / Local theme / Open .itz** | YES / NO / UNCLEAR |

If 0.6 = NO → native Method A import is likely **UNSUPPORTED**; skip to Step 6 fallback notes; still fill the results table.

---

## Step 1 — Backup / restore path

| # | Action | Record |
| --- | --- | --- |
| 1.1 | In Themes, locate current theme / default restore | path described |
| 1.2 | If “save current” exists, save or screenshot “My themes” | |
| 1.3 | Do **not** clear Themes or Launcher data | |

---

## Step 2 — Import TEST candidate

| # | Action | PASS / FAIL / NOT TESTED | Notes |
| --- | --- | --- | --- |
| 2.1 | Copy `.itz` to phone storage | | |
| 2.2 | Import via stock Themes (or document missing UI) | | |
| 2.3 | Preview shows TEST labeling / icons / wallpaper | | |

---

## Step 3 — Apply

Apply only what the UI offers. Prefer icons+wallpaper if component picker exists.

| Component | After apply | Notes / screenshots |
| --- | --- | --- |
| Icons (5 TEST apps) | PASS / FAIL / NOT TESTED / UNSUPPORTED | |
| Home wallpaper | | |
| Lockscreen wallpaper / lock theme | | |
| AOD | | |
| Notification shade | | |
| Control center | | |
| Status bar | | |
| Settings UI | | |

---

## Step 4 — Home inspection

- [ ] Dialer / Phone icon changed as expected (or package mismatch noted)
- [ ] Messages
- [ ] Settings
- [ ] Gallery
- [ ] Camera
- [ ] Unlisted apps unchanged (expected for minimal pack)

Package names on Global may differ (e.g. Google Dialer). If icons do not map, record actual package names from App info — do not force hacks.

---

## Step 5 — Reboot persistence

1. Reboot phone.
2. Recheck the component table → **reboot persistence** PASS/FAIL.
3. Screenshot home + lock after reboot.

---

## Step 6 — Rollback

1. Restore previous / default theme via Themes.
2. Confirm icons + wallpaper restored.
3. **Rollback** PASS / FAIL.
4. If native restore fails, use Method C: set prior wallpaper manually; re-apply prior icon style if any.

---

## Step 7 — Optional Method B (STOP unless you approve)

Only if you **explicitly** approve installing Shizuku + VFont:

1. Install Shizuku; start Wireless debugging; grant shell.
2. Install VFont from its GitHub release.
3. Device support check → save report.
4. Preview TEST `.itz` → apply selected components → restore.

Record separately; Global remains experimental per VFont docs.

---

## Results matrix (copy into report)

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

**Overall feasibility:** PENDING OWNER DEVICE RUN  
**Full icon generation:** still **blocked** until import/apply feasibility is decided.
