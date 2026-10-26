import sys, json, os
from rapidocr_onnxruntime import RapidOCR
ocr = RapidOCR()
out = {}
pages = sys.argv[1:]
for p in pages:
    res, _ = ocr(p)
    boxes = []
    if res:
        # sort by y then x of top-left
        items = []
        for r in res:
            box, text, score = r
            xs = [pt[0] for pt in box]; ys = [pt[1] for pt in box]
            items.append((min(ys), min(xs), max(ys), max(xs), text, score))
        items.sort(key=lambda it: (round(it[0]/12), it[1]))
        boxes = [(it[1], it[0], it[4], round(it[5],2)) for it in items]
    out[p] = boxes
    print('=== ', p)
    prev_y = None
    for x, y, t, s in boxes:
        if prev_y is not None and y - prev_y > 14:
            print()
        print(f'{t}', end=' | ')
        prev_y = y
    print()
json.dump(out, open('ocr_out.json','w'))
