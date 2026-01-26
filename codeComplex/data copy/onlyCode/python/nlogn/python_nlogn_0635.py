from collections import namedtuple
import sys

HS = namedtuple('HS', 'x1 x2 y')

n, m = [int(w) for w in input().split()]
vs = [int(input()) for _ in range(n)]
hs = [HS(*[int(w) for w in input().split()]) for _ in range(m)]

vs.sort()

hr = len([s for s in hs if s.x1 == 1 and s.x2 == 10**9])
hs = [s.x2 for s in hs if s.x1 == 1 and s.x2 < 10**9]
hs.sort()

r = hc = len(hs)
hi = vi = 0
for hi in range(hc):
    while vi < n and hs[hi] >= vs[vi]:
        vi += 1
    c = (hc - hi - 1) + vi
    if c < r:
        r = c

print(r + hr)
