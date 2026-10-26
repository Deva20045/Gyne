import sys
from PIL import Image
from rapidocr_onnxruntime import RapidOCR
ocr = RapidOCR()
path, out = sys.argv[1], sys.argv[2]
x0,y0,x1,y1 = (float(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv)>7 else 1.0
im = Image.open(path)
w,h = im.size
box = (int(x0*w), int(y0*h), int(x1*w), int(y1*h))
c = im.crop(box)
if scale != 1.0:
    c = c.resize((int(c.width*scale), int(c.height*scale)), Image.LANCZOS)
c.save(out)
res,_ = ocr(out)
items=[]
if res:
    for r in res:
        bx,t,s = r
        xs=[p[0] for p in bx]; ys=[p[1] for p in bx]
        items.append((min(ys),min(xs),t,round(s,2)))
    items.sort(key=lambda it:(round(it[0]/16), it[1]))
prev=None; line=[]
for it in items:
    y,x,t,s = it
    if prev is not None and y-prev>18: print(' | '.join(line)); line=[]
    line.append(t); prev=y
if line: print(' | '.join(line))
