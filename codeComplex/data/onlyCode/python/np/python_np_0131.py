from collections import defaultdict
from math import gcd
from heapq import heappop, heappush
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hp = [(0, 0)]
dis = {0: 0}
seen = set()
while hp:
    _, x = heappop(hp)
    if x == 1:
        print(dis[x])
        break
    if x in seen: continue
    seen.add(x)
    for a, b in zip(A, B):
        y = gcd(x, a)
        if y not in dis or dis[y] > dis[x] + b:
            dis[y] = dis[x] + b
            heappush(hp, (dis[y], y))
else:
    print(-1)