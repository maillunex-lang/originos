#!/usr/bin/env python3
"""Validate a candidate .itz archive against OBSERVED structural rules.

Exit 0 = structural checks passed (NOT proof of device compatibility).
Exit 1 = structural failure.
"""

from __future__ import annotations

import argparse
import struct
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

REQUIRED_ROOT_FILES = ("description.xml",)
REQUIRED_DIRS_OR_PREFIXES = (
    "icons/",
    "launcher/",
    "wallpaper/",
)
REQUIRED_WALLPAPERS = (
    "wallpaper/default_wallpaper.png",
    "wallpaper/default_lock_wallpaper.png",
)
MIN_ICONS = 3
EXPECTED_ICON_SIZE = (192, 192)
ALLOWED_ICON_SIZES = {(192, 192), (198, 198)}


def png_size(data: bytes) -> tuple[int, int]:
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG")
    w, h = struct.unpack(">II", data[16:24])
    return w, h


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    warnings: list[str] = []

    if not path.is_file():
        return [f"missing file: {path}"]

    if not zipfile.is_zipfile(path):
        return [f"not a ZIP archive (itz must be ZIP-based per observed samples): {path}"]

    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        # integrity
        bad = zf.testzip()
        if bad is not None:
            errors.append(f"CRC failure on entry: {bad}")

        for req in REQUIRED_ROOT_FILES:
            if req not in names:
                errors.append(f"missing required entry: {req}")

        for prefix in REQUIRED_DIRS_OR_PREFIXES:
            if not any(n.startswith(prefix) for n in names):
                errors.append(f"missing required path prefix: {prefix}")

        for wp in REQUIRED_WALLPAPERS:
            if wp not in names:
                errors.append(f"missing wallpaper: {wp}")

        icons = [n for n in names if n.startswith("icons/") and n.endswith(".png") and n.count("/") == 1]
        if len(icons) < MIN_ICONS:
            errors.append(f"need >= {MIN_ICONS} static icons/, found {len(icons)}")

        # description.xml parse
        if "description.xml" in names:
            try:
                root = ET.fromstring(zf.read("description.xml"))
                if root.tag != "theme":
                    errors.append(f"description.xml root tag must be theme, got {root.tag}")
                title = root.findtext("./titles/title")
                if not title:
                    errors.append("description.xml missing titles/title")
                elif "TEST" not in title.upper() and "TEST" not in (root.findtext("./descriptions/description") or "").upper():
                    warnings.append("candidate should be clearly labeled TEST in metadata")
            except ET.ParseError as e:
                errors.append(f"description.xml parse error: {e}")

        # icon dimensions + package-like names
        for name in icons:
            base = Path(name).name
            if not base.endswith(".png") or "." not in base[:-4]:
                warnings.append(f"icon name may not be package-like: {base}")
            try:
                wh = png_size(zf.read(name))
                if wh not in ALLOWED_ICON_SIZES:
                    errors.append(f"{name} size {wh}, expected one of {sorted(ALLOWED_ICON_SIZES)}")
            except ValueError as e:
                errors.append(f"{name}: {e}")

        for wp in REQUIRED_WALLPAPERS:
            if wp in names:
                try:
                    w, h = png_size(zf.read(wp))
                    if w < 720 or h < 1280:
                        warnings.append(f"{wp} unusually small: {w}x{h}")
                except ValueError as e:
                    errors.append(f"{wp}: {e}")

        if "key" not in names:
            warnings.append(
                "no 'key' entry — observed store themes include opaque 768-char key; "
                "Global Themes/VFont may reject (algorithm UNKNOWN)"
            )
        else:
            key = zf.read("key")
            if len(key) != 768:
                warnings.append(f"key length {len(key)} != 768 observed in samples")

        # Refuse labeling hints
        lower_names = " ".join(names).lower()
        if "release" in Path(path).name.lower() and "test" not in Path(path).name.lower():
            warnings.append("filename looks like a release; keep TEST labeling until device pass")

    for w in warnings:
        print(f"WARNING: {w}")
    return errors


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("itz", type=Path, help="path to .itz candidate")
    args = ap.parse_args()
    errors = validate(args.itz.resolve())
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        print("RESULT: FAIL (structural)")
        sys.exit(1)
    print("RESULT: PASS (structural only — device compatibility NOT proven)")
    sys.exit(0)


if __name__ == "__main__":
    main()
