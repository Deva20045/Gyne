import sys
from rapidocr_onnxruntime import RapidOCR
ocr = RapidOCR()
def rev(s): return s[::-1]
for p in sys.argv[1:]:
    res, _ = ocr(p)
    items = []
    if res:
        for r in res:
            box, text, score = r
            xs=[pt[0] for pt in box]; ys=[pt[1] for pt in box]
            items.append((min(ys), min(xs), max(ys), max(xs), text, score))
        items.sort(key=lambda it:(round(it[0]/16), it[1]))
    print(f'\n########## {p}')
    prev=None; line=[]
    for it in items:
        y0,x0,y1,x1,t,s = it
        if prev is not None and y0-prev>18:
            print(' | '.join(line)); line=[]
        line.append(f'{t}')
        prev=y0
    if line: print(' | '.join(line))
