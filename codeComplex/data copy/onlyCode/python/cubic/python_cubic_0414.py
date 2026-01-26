import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
A = [[0] * (m) for _ in range(n)]
B = [[0] * (m) for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m - 1):
        A[i][j + 1] = tmp[j] # + A[i][j]
for i in range(n - 1):
    tmp = list(map(int, input().split()))
    for j in range(m):
        B[i + 1][j] = tmp[j] # + B[i][j]

if k % 2:
    ans = [[-1] * m for _ in range(n)]
    for a in ans:
        print(*a)
    sys.exit()
ans = [[0] * m for _ in range(n)]
lim = k // 2
dp = [[[float("inf")] * (lim + 1) for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j][0] = 0

for k in range(1, lim + 1):
    for i in range(n):
        for j in range(m):
            if i: dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k - 1] + B[i][j])
            if j: dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][k - 1] + A[i][j])
            if i < n - 1: dp[i][j][k] = min(dp[i][j][k], dp[i + 1][j][k - 1] + B[i + 1][j])
            if j < m - 1: dp[i][j][k] = min(dp[i][j][k], dp[i][j + 1][k - 1] + A[i][j + 1])
for i in range(n):
    for j in range(m):
        ans[i][j] = dp[i][j][-1] * 2
for a in ans:
    print(*a)