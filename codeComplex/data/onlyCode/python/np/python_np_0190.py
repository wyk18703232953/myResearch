from itertools import combinations
n, mn, mx, diff = map(int, input().split())
arr = list(map(int, input().split()))
print(sum(sum(1 for x in combinations(arr, i) if sum(x)>= mn and sum(x) <= mx and max(x)-min(x)>=diff) for i in range(2, n+1)))

