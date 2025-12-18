import sys
from collections import defaultdict
 
input = sys.stdin.readline
 
n, m = map(int, input().split())
# n, m = 3 * 10 ** 5, 8
vals = set()
locs = defaultdict(list)
for i in range(n):
    inp = map(int, input().split())
    for pos, v in enumerate(inp):
        vals.add(v)
        locs[v].append((pos, i))

masks = [0] * n
full = (1<<m) - 1
met = {0:0}
for v in sorted(vals, reverse=True):
    for pos, i in locs[v]:
        curr_mask = masks[i] = masks[i] | (1<<pos)
        met[curr_mask] = i
        complement = full ^ curr_mask
        if complement in met:
            print(i+1, met[complement]+1)
            sys.exit()