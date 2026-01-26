n, t = map(int, input().split())
l = []
for _ in range(n):
  x, a = map(int, input().split())
  l.append((x-a/2, x+a/2))
l.sort()
res = 2
# print(l)
for i in range(n-1):
  if l[i+1][0] - l[i][1] == t:
    res += 1
  elif l[i+1][0] - l[i][1] > t:
    res += 2

print(res)
