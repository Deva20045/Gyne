import sys, json
from rapidocr_onnxruntime import RapidOCR
ocr = RapidOCR()
out = {}
lines_all = []
for p in sys.argv[1:]:
    res, _ = ocr(p)
    items = []
    if res:
        for r in res:
            box, text, score = r
            xs = [pt[0] for pt in box]; ys = [pt[1] for pt in box]
            items.append((min(ys), min(xs), max(ys), max(xs), text, score))
        items.sort(key=lambda it: (round(it[0]/12), it[1]))
    out[p] = items
    lines_all.append(f'\n########## {p} ##########')
    prev_y = None
    line = []
    for it in items:
        y0, x0, y1, x1, t, s = it
        if prev_y is not None and y0 - prev_y > 14:
            lines_all.append(' | '.join(line)); line = []
        line.append(t)
        prev_y = y0
    if line: lines_all.append(' | '.join(line))
open('ocr_dump.txt','w').write('\n'.join(lines_all))
json.dump({k:[[round(a,1),round(b,1),t,round(s,2)] for a,b,c,d,t,s in v] for k,v in out.items()}, open('ocr_out.json','w'))
print('ok')
