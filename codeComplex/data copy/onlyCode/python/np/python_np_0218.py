from itertools import combinations
n, l, r, x = map(int, input().split())
a = [int(x) for x in input().split()]
ans = 0
for i in range(2, n+1):
    for p in combinations(a, i):
        if l<=sum(p)<=r and max(p)-min(p)>=x:
            ans += 1
print(ans)
