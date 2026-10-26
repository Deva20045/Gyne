#!/usr/bin/env python3
import re, sys, json
from collections import Counter
from pathlib import Path

t = Path('obg-mastery-path.html').read_text(encoding='utf-8')
ids = re.findall(r"id: '([a-z0-9-]+-q\d+)'", t)
dups = [i for i, c in Counter(ids).items() if c > 1]
print('total questions:', len(ids))
print('duplicate ids:', dups[:20] or 'none')
# duplicate stems
stems = re.findall(r"q: '((?:[^'\\]|\\.)*)', options", t)
stems = [s.replace("\\'", "'") for s in stems]
sd = [s for s, c in Counter(stems).items() if c > 1]
print('duplicate stems:', len(sd))
for s in sd[:10]: print('   DUP:', s[:90])
# chapter numbers present
nums = sorted(int(x) for x in re.findall(r"    id: 'ch(\d\d)',", t))
print('chapters present:', nums)
# chapter-level answer distribution
blocks = re.split(r"\n  \{\n    id: 'ch(\d\d)',", t)
for i in range(1, len(blocks), 2):
    ch = int(blocks[i]); body = blocks[i+1]
    corr = [int(x) for x in re.findall(r"correct: (\d),", body)]
    c = Counter(corr)
    qn = len(corr)
    print(f'ch{ch:02d}: {qn} Qs  A-D {[c[i] for i in range(4)]}  pct {[round(100*c[i]/max(qn,1),1) for i in range(4)]}')
