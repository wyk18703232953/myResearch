from sys import stdin
from bisect import *

rints = lambda: [int(x) for x in stdin.readline().split()]
rints_2d = lambda n: [rints() for _ in range(n)]
n, mem, pos, power = int(input()), [1], [], []
a = sorted(rints_2d(n))

for x, y in a:
    pos.append(x)
    power.append(y)

for i in range(1, n):
    ix = bisect_left(pos, pos[i] - power[i]) - 1
    if ix == -1:
        mem.append(1)
    else:
        mem.append(mem[ix] + 1)

print(n - max(mem))
