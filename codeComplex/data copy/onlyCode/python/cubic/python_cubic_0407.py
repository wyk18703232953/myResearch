input = __import__('sys').stdin.readline

n,m,k = map(int, input().split())
hor = [[int(x) for x in input().split()] for _ in ' ' * n]
ver = [[int(x) for x in input().split()] for _ in ' ' * (n - 1)]

if k % 2:
  for i in ' ' * n: print('-1 ' * m)
  exit()

mtx_old = [[0] * m for _ in ' ' * n]

def neighbours(x, y):
  a = 1e18
  b = 1e18
  c = 1e18
  d = 1e18
  if x > 0: a = hor[y][x - 1] * 2 + mtx_old[y][x - 1]
  if x < m - 1: b = hor[y][x] * 2 + mtx_old[y][x + 1]
  if y > 0: c = ver[y - 1][x] * 2 + mtx_old[y - 1][x]
  if y < n - 1: d = ver[y][x] * 2 + mtx_old[y + 1][x]
  return min(a, b, c, d)

for i in range(k // 2):
  mtx_new = [[0] * m for _ in ' ' * n]

  for x in range(m):
    for y in range(n):
      mtx_new[y][x] = neighbours(x, y)

  mtx_old = mtx_new

for row in mtx_old: print(*row)