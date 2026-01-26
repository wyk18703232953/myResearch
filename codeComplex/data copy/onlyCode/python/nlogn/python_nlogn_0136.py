n, m, k = map(int, input().split())
a = sorted(map(int, input().split()))
r = [x for x in range(n + 1) if sum(a[n - x :]) + k >= m + x]
print(min(r) if r else -1)
