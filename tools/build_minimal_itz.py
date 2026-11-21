#!/usr/bin/env python3
"""Build a minimal Liquid Graphite TEST .itz candidate from assets/test.

This produces a structural ZIP matching OBSERVED Chinese/legacy .itz layout.
It is NOT labeled working/released. OriginOS 7 Global acceptance is UNVERIFIED.
Opaque store `key` / md5result algorithms are UNKNOWN — omitted rather than faked.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets" / "test"
DIST = ROOT / "dist"
DEFAULT_OUT = DIST / "LiquidGraphite_TEST_minimal.itz"

DESCRIPTION_XML = """<?xml version="1.0" encoding="UTF-8"?>
<theme>
  <id>900001</id>
  <version><![CDATA[0.1.0-TEST]]></version>
  <uid>0</uid>
  <id3>900001</id3>
  <titles>
    <title locale="en_US"><![CDATA[Liquid Graphite TEST]]></title>
    <title locale="zh_CN"><![CDATA[Liquid Graphite TEST]]></title>
  </titles>
  <authors>
    <author locale="en_US"><![CDATA[maillunex-lang/originos T-001]]></author>
  </authors>
  <designers>
    <designer locale="en_US"><![CDATA[Liquid Graphite research]]></designer>
  </designers>
  <descriptions>
    <description locale="en_US"><![CDATA[
TEST CANDIDATE ONLY — not a released theme.
Built for OriginOS 7 Global feasibility spike (T-001).
Do not treat as installable/working until device smoke test passes.
Missing opaque key/md5 — format acceptance UNVERIFIED on Global firmware.
]]></description>
  </descriptions>
  <tool locale="en_US"><![CDATA[originos-tools]]></tool>
  <toolversion><![CDATA[t001-0.1]]></toolversion>
  <time>{time_ms}</time>
  <!-- md5result intentionally omitted: algorithm UNKNOWN; do not invent -->
  <edition>2</edition>
</theme>
"""

ICONSIZE_XML = """<?xml version="1.0" encoding="UTF-8"?>
<ICONSIZE>
  <width>52</width>
  <height>52</height>
  <calendar>false</calendar>
  <leftoffset>0</leftoffset>
  <topoffset>0</topoffset>
  <foldericonsize>46</foldericonsize>
  <version>1</version>
  <foldericonwidth>42</foldericonwidth>
  <foldericonheight>42</foldericonheight>
  <supporticonraduischange>1</supporticonraduischange>
  <iconsneedredraw>0</iconsneedredraw>
  <shape>1</shape>
</ICONSIZE>
"""

REQUIRED_ICONS = [
    "com.android.dialer.png",
    "com.android.mms.png",
    "com.android.settings.png",
    "com.vivo.gallery.png",
    "com.android.camera.png",
]


def add_file(zf: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    info = zipfile.ZipInfo(arcname)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.date_time = time.localtime(time.time())[:6]
    zf.writestr(info, data)


def build(out: Path) -> dict:
    missing = [n for n in REQUIRED_ICONS if not (ASSETS / "icons" / n).is_file()]
    for rel in (
        "wallpaper/default_wallpaper.png",
        "wallpaper/default_lock_wallpaper.png",
        "preview/preview_launcher_0.png",
        "thumbnail.png",
        "launcher/icon_mask.png",
        "launcher/icon_bg_default.png",
        "launcher/folder_icon.png",
    ):
        if not (ASSETS / rel).is_file():
            missing.append(rel)
    if missing:
        raise SystemExit(f"Missing TEST assets: {missing}")

    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        out.unlink()

    time_ms = int(time.time() * 1000)
    desc = DESCRIPTION_XML.format(time_ms=time_ms).encode("utf-8")

    with zipfile.ZipFile(out, "w") as zf:
        add_file(zf, "description.xml", desc)
        add_file(zf, "launcher/iconsize.xml", ICONSIZE_XML.encode("utf-8"))
        # TEST marker — not a store key
        add_file(
            zf,
            "TEST_README.txt",
            (
                "Liquid Graphite TEST candidate (T-001).\n"
                "NOT device-verified. NOT a released theme.\n"
                "Opaque vivo 'key' omitted (algorithm UNKNOWN).\n"
            ).encode("utf-8"),
        )
        for name in REQUIRED_ICONS:
            add_file(zf, f"icons/{name}", (ASSETS / "icons" / name).read_bytes())
        for rel in (
            "launcher/icon_mask.png",
            "launcher/icon_bg_default.png",
            "launcher/folder_icon.png",
            "wallpaper/default_wallpaper.png",
            "wallpaper/default_lock_wallpaper.png",
            "preview/preview_launcher_0.png",
            "preview/preview_lockscreen_0.png",
            "thumbnail.png",
        ):
            src = ASSETS / rel
            if src.is_file():
                add_file(zf, rel, src.read_bytes())

    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    meta = {
        "artifact": str(out.relative_to(ROOT)),
        "sha256": digest,
        "bytes": out.stat().st_size,
        "label": "TEST_CANDIDATE",
        "global_compatibility": "UNVERIFIED",
        "key_file": "OMITTED_UNKNOWN_ALGORITHM",
        "icons": REQUIRED_ICONS,
        "built_at_unix_ms": time_ms,
    }
    meta_path = out.with_suffix(out.suffix + ".sha256.json")
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return meta


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-o", "--output", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    meta = build(args.output.resolve())
    print(json.dumps(meta, indent=2))


if __name__ == "__main__":
    main()
