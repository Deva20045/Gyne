#!/usr/bin/env python3
"""Crop a fractional box out of a scanned page, optionally rotate, and upscale.

usage: python3 tools/rcrop.py pNNN x0 y0 x1 y1 [scale] [rotate]
Fractional coords (0-1) relative to the full page; rotate in degrees
counter-clockwise (90 / 270 for sideways text). Writes .pages/crop/out.jpg.
"""
import sys
from pathlib import Path

from PIL import Image

name, x0, y0, x1, y1 = sys.argv[1:6]
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 1.0
rot = float(sys.argv[7]) if len(sys.argv) > 7 else 0.0
src = Path(f".pages/{name}.jpeg")
if not src.exists():
    src = Path(f".pages/{name}.jpg")
im = Image.open(src).convert("RGB")
w, h = im.size
box = (int(float(x0) * w), int(float(y0) * h), int(float(x1) * w), int(float(y1) * h))
c = im.crop(box)
if rot:
    c = c.rotate(rot, expand=True, fillcolor=(255, 255, 255))
if scale != 1.0:
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
out = Path(".pages/crop")
out.mkdir(parents=True, exist_ok=True)
p = out / f"{name}_{x0}_{y0}.jpg"
c.save(p, quality=92)
print(p, c.size)
