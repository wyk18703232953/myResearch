import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
ej = [list(map(int, input().split())) for _ in range(n)]
ei = [list(map(int, input().split())) for _ in range(n - 1)]

if k % 2:
  for _ in range(n): print(*[-1] * m)
  exit(0)
inf = -1
dp = [[inf] * (n * m) for _ in range(k // 2 + 1)]
for t in range(n * m): dp[0][t] = 0
for c in range(k // 2):
  for i in range(n):
    for j in range(m):
      t = i * m + j

      tt = (i + 1) * m + j
      if i + 1 < n and (dp[c + 1][tt] == -1 or dp[c + 1][tt] > dp[c][t] + ei[i][j]): dp[c + 1][tt] = dp[c][t] + ei[i][j]

      tt = i * m + j + 1
      if j + 1 < m and (dp[c + 1][tt] == -1 or dp[c + 1][tt] > dp[c][t] + ej[i][j]): dp[c + 1][tt] = dp[c][t] + ej[i][j]

      tt = (i - 1) * m + j
      if i - 1 >= 0 and (dp[c + 1][tt] == -1 or dp[c + 1][tt] > dp[c][t] + ei[i - 1][j]): dp[c + 1][tt] = dp[c][t] + ei[i - 1][j]

      tt = i * m + j - 1
      if j - 1 >= 0 and (dp[c + 1][tt] == -1 or dp[c + 1][tt] > dp[c][t] + ej[i][j - 1]): dp[c + 1][tt] = dp[c][t] + ej[i][j - 1]

res = [[0] * m for _ in range(n)]
for i in range(n):
  for j in range(m): res[i][j] = dp[-1][i * m + j] * 2
  print(*res[i])
