r, g, b = map(int, input().split())
a = [[], [], []]
dp = [[[0 for i in range(b + 1)] for j in range(g + 1)] for k in range(r + 1)]
for x in range(3):
    a[x] = sorted([int(x) for x in input().split()])
odp = 0
for i in range(r + 1):
    for j in range(g + 1):
        for k in range(b + 1):
            if i < r and j < g:
                dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k] + a[0][i] * a[1][j])
            if i < r and k < b:
                dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k] + a[0][i] * a[2][k])
            if j < g and k < b:
                dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k] + a[1][j] * a[2][k])
            odp = max(odp, dp[i][j][k])
print(odp)