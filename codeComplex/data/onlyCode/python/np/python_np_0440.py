import sys
from collections import defaultdict
 
reader = (map(int, line.split()) for line in sys.stdin)
input = reader.__next__
 
n, m = input()
# n, m = 3 * 10 ** 5, 8
vals = set()
locs = defaultdict(list)
for i in range(n):
    for pos, v in enumerate(input()):
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