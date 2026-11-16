#!/usr/bin/env python3
"""Measure shared 6-word phrases between a draft folder and one or more source folders.

  python3 Story/Revision/Experiments/tools/overlap.py --draft Story/Revision/Experiments/Wild \
      --against Story/Chapters --against Story/Revision/Experiments/Garden [--show 8]

Prints per-chapter percentages, then each draft paragraph sharing at least --show
phrases with any source, with the shared spans. Shows draft-side text only, so it
can be run without reading the sources (the "fresh soil" rule).
"""
import argparse, glob, os, re
def words(t): return re.findall(r"[a-z']+", t.lower())
def shingles(t, n=6):
    w = words(t); return {' '.join(w[i:i+n]) for i in range(len(w) - n + 1)}
ap = argparse.ArgumentParser()
ap.add_argument('--draft', required=True); ap.add_argument('--against', action='append', required=True)
ap.add_argument('--show', type=int, default=8)
a = ap.parse_args()
pools = {}
for src in a.against:
    s = set()
    for f in glob.glob(os.path.join(src, 'Chapter_*.txt')): s |= shingles(open(f, encoding='utf-8').read())
    pools[os.path.basename(src.rstrip('/'))] = s
tot = {k: 0 for k in pools}; n_all = 0
for f in sorted(glob.glob(os.path.join(a.draft, 'Chapter_*.txt'))):
    t = open(f, encoding='utf-8').read(); B = shingles(t); n_all += len(B)
    row = []
    for k, s in pools.items():
        c = len(B & s); tot[k] += c; row.append(f'{k} {100*c/max(len(B),1):.1f}%')
    print(os.path.basename(f), '  '.join(row))
    for p in re.split(r'\n\s*\n', t):
        w = words(p)
        for k, s in pools.items():
            hits = [i for i in range(len(w) - 5) if ' '.join(w[i:i+6]) in s]
            if len(hits) >= a.show:
                spans = []
                for i in hits:
                    if spans and i <= spans[-1][1]: spans[-1][1] = i + 6
                    else: spans.append([i, i + 6])
                print(f'   [{k} {len(hits)}] ' + ' / '.join(' '.join(w[x:y]) for x, y in spans))
print('TOTAL', '  '.join(f'{k} {100*v/max(n_all,1):.1f}%' for k, v in tot.items()))
