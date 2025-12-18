n, m, k = map(int, input().split())
 
h = []
for i in range(n):
  h.append(list(map(int, input().split())))
 
v = []
for i in range(n - 1):
  v.append(list(map(int, input().split())))
 
if k % 2 == 0:
  d = [[0] * m for i in range(n)]
  for t in range(k // 2):
    dt = [[0] * m for i in range(n)]
    for i in range(n):
      for j in range(m):
        x = float('inf')
        if i - 1 >= 0:
          x = min(x, d[i - 1][j] + v[i - 1][j] * 2)
        if i + 1 < n:
          x = min(x, d[i + 1][j] + v[i][j] * 2)
        if j - 1 >= 0:
          x = min(x, d[i][j - 1] + h[i][j - 1] * 2)
        if j + 1 < m:
          x = min(x, d[i][j + 1] + h[i][j] * 2)
        dt[i][j] = x
    d = dt.copy()
else:
  d = [[-1] * m for i in range(n)]
for i in d:
    print(*i)