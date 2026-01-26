import itertools

n, l, r, x = map(int, input().split())
C = list(map(int, input().split()))

ans = 0
for i in range(2, n+1):
  for c in itertools.combinations(C, i):
    d = sum(c)
    if d < l or d > r:
      continue
    if max(c) - min(c) < x:
      continue
    ans += 1

print(ans)