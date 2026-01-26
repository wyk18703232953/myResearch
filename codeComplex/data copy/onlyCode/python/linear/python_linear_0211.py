import sys
import io, os
input = sys.stdin.buffer.readline
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

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
    for x, vx, vy in XV:
        k = -a*vx+vy
        ans += max(0, d[k]-dvx[(k, vx)])
        d[k] += 1
        dvx[(k, vx)] += 1
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
