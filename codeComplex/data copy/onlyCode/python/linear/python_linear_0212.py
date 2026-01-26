import sys
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

from collections import defaultdict

n, a, b = map(int, input().split())
XV = []
for i in range(n):
    x, vx, vy = map(int, input().split())
    XV.append((x, vx, vy))
if a != 0:
    ans = 0
    d = defaultdict(lambda:0)
    dvx = defaultdict(lambda:0)
    dvy = defaultdict(lambda:0)
    dvxy = defaultdict(lambda:0)
    for x, vx, vy in XV:
        k = -a*vx+vy
        ans += max(0, d[k]-(dvx[(k, vx)]+dvy[(k, vy)]-dvxy[(k, vx, vy)]))
        d[k] += 1
        dvx[(k, vx)] += 1
        dvy[(k, vy)] += 1
        dvxy[(k, vx, vy)] += 1
    print(ans*2)
else:
    ans = 0
    d = defaultdict(lambda:defaultdict(lambda:0))
    ds = defaultdict(lambda:0)
    for x, vx, vy in XV:
        ans += max(0, ds[vy]-d[vy][vx])
        d[vy][vx] += 1
        ds[vy] += 1
    print(ans*2)
