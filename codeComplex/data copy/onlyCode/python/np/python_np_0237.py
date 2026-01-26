n, l, r, x = map(int, input().split())
c = list(map(int, input().split()))

from itertools import combinations
ways_to_choose = 0
for length in range(2, n + 1):
    for p in combinations(c, length):
        problemset = sorted(p)
        if l <= sum(problemset) <= r and problemset[-1] - problemset[0] >= x:
            ways_to_choose += 1

print(ways_to_choose)
