n = int(input())
d = {}
for _ in range(n):
  a, x = map(int, input().split())
  d[a] = x
m = int(input())
for _ in range(m):
  b, y = map(int, input().split())
  d[b] = max(d.get(b, 0), y)
print(sum(d.values()))