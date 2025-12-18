from itertools import combinations
n, l, r, x = map(int,input().split())
c = [*map(int, input().split())]
print(sum([sum([1 if max(j) - min(j) >= x and l <= sum(j) <= r else 0 for j in combinations(c, i)]) for i in range(1, n + 1)]))
