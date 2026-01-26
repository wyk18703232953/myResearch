from decimal import *
ar = [list(map(float, input().split())) for i in range(int(input()))]
dp = [[0 for i in range(1 << 18)] for j in range(18)]
n, ans = len(ar), 0
dp[0][(1 << n) - 1] = 1
for i in range((1 << n) - 1, 0, -1):
    for j in range(n):
        if i & (1 << j) == 0:
            continue
        for k in range(n):
            if i & (1 << k) != 0 or j == k:
                continue
            dp[j][i] = max(dp[j][i], dp[k][i ^ (1 << k)] * ar[k][j] + dp[j][i ^ (1 << k)] * ar[j][k])
for i in range(n):
    ans = max(ans, dp[i][1 << i])
print('{:.6f}'.format(ans))