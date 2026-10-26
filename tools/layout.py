import sys
from rapidocr_onnxruntime import RapidOCR
ocr = RapidOCR()
p = sys.argv[1]
res,_ = ocr(p)
items=[]
for r in res:
    bx,t,s = r
    xs=[q[0] for q in bx]; ys=[q[1] for q in bx]
    items.append((min(ys),min(xs),max(xs),t,round(s,2)))
items.sort(key=lambda it:(it[0], it[1]))
W = max(it[2] for it in items)
prev=None
for y,x0,x1,t,s in items:
    if prev is not None and y-prev>16: print()
    col = int((x0/W)*90)
    print(' '*col + t)
    prev=y
