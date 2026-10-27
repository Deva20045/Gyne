#!/usr/bin/env python3
"""Extract the embedded scan image of each PDF page into .pages/pNNN.jpg.

usage: python3 tools/extract_pages.py OBG_Vol1_part_06_pages_226-270.pdf 226
The second argument is the book page number of the PDF's first page.
"""
import sys
from pathlib import Path

import pymupdf

OUT = Path(".pages")
OUT.mkdir(exist_ok=True)

pdf = sys.argv[1]
start = int(sys.argv[2])
doc = pymupdf.open(pdf)
for i in range(doc.page_count):
    page = doc[i]
    imgs = page.get_images(full=True)
    if not imgs:
        pix = page.get_pixmap(matrix=pymupdf.Matrix(3, 3))
        out = OUT / f"p{start + i:03d}.jpg"
        pix.save(out)
        print(out, "rendered")
        continue
    xref = imgs[0][0]
    info = doc.extract_image(xref)
    out = OUT / f"p{start + i:03d}.{info['ext']}"
    out.write_bytes(info["image"])
print("pages:", doc.page_count, "->", OUT)
