import sys
from collections import defaultdict

reader = (map(int, line.split()) for line in sys.stdin)
input = reader.__next__

n, m = input()
# n, m = 3 * 10 ** 5, 8
elems = set()
vals = defaultdict(list)
for i in range(n):
    for pos, v in enumerate(input()):
        elems.add(v)
        vals[v].append((pos, i))

elems = sorted(elems, reverse=True)

masks = [0] * n
full = (1<<m) - 1
met = {0:0}
for v in elems:
    for pos, i in vals[v]:
        curr_mask = masks[i] = masks[i] | (1<<pos)
        met[curr_mask] = i
        complement = full ^ curr_mask
        if complement in met:
            print(i+1, met[complement]+1)
            sys.exit()
