#!/usr/bin/env python3
"""Downscale scanned pages for on-screen reading.

usage: python3 tools/preview.py <width> p246 p247 ...
Writes .pages/prev/pNNN.jpg (and prints the paths).
"""
import sys
from pathlib import Path

from PIL import Image

w = int(sys.argv[1])
out_dir = Path(".pages/prev")
out_dir.mkdir(parents=True, exist_ok=True)
for name in sys.argv[2:]:
    src = Path(f".pages/{name}.jpeg")
    if not src.exists():
        src = Path(f".pages/{name}.jpg")
    im = Image.open(src).convert("RGB")
    h = int(im.height * w / im.width)
    im.resize((w, h), Image.LANCZOS).save(out_dir / f"{name}.jpg", quality=88)
    print(out_dir / f"{name}.jpg")
