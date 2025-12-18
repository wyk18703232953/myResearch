n = int(input())
d1 = {}
for _ in range(n):
  a, x = map(int, input().split())
  d1[a] = x
d2 = {}
m = int(input())
for _ in range(m):
  b, y = map(int, input().split())
  d2[b] = y
ans = 0
for key in set(d1.keys()) | set(d2.keys()):
  ans += max(d1.get(key, 0), d2.get(key, 0))
print(ans)