#!/usr/bin/env python3
"""OCR scanned pages into a reading-order text dump.

usage: python3 tools/ocrdump.py <out.txt> <page1.jpg> [page2.jpg ...]
Each page is emitted in top-to-bottom, left-to-right reading order with a
########## marker. Progress lines go to stderr so the file stays clean.
"""
import sys
import time
from pathlib import Path

from rapidocr_onnxruntime import RapidOCR

out = Path(sys.argv[1])
pages = sys.argv[2:]
ocr = RapidOCR()
buf = []
for p in pages:
    t0 = time.time()
    res, _ = ocr(p)
    items = []
    if res:
        for box, text, score in res:
            xs = [q[0] for q in box]
            ys = [q[1] for q in box]
            items.append((min(ys), min(xs), max(ys), max(xs), text, score))
        items.sort(key=lambda it: (round(it[0] / 16), it[1]))
    buf.append(f"\n########## {p} ##########")
    prev = None
    line = []
    for y0, x0, y1, x1, t, s in items:
        if prev is not None and y0 - prev > 18:
            buf.append(" | ".join(line))
            line = []
        line.append(t)
        prev = y0
    if line:
        buf.append(" | ".join(line))
    out.write_text("\n".join(buf) + "\n", encoding="utf-8")
    print(f"{p}: {len(items)} boxes, {time.time() - t0:.1f}s", file=sys.stderr, flush=True)
print("DONE", file=sys.stderr, flush=True)
