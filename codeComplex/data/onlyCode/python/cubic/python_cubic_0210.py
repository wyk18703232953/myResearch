import sys

input = sys.stdin.readline

r, g, b = map(int, input().split())
sticks = [sorted([int(i) for i in input().split()], reverse = True) for j in range(3)]
dp, ans = [[[0 for i in range(b + 1)] for j in range(g + 1)] for k in range(r + 1)], 0 # dp[i][j][k] is i largest red, j largest green, k largest blue
for i in range(r + 1):
    for j in range(g + 1):
        for k in range(b + 1):
            if i < r and j < g:
                dp[i + 1][j + 1][k] = max(dp[i + 1][j + 1][k], dp[i][j][k] + sticks[0][i] * sticks[1][j])
            if i < r and k < b:
                dp[i + 1][j][k + 1] = max(dp[i + 1][j][k + 1], dp[i][j][k] + sticks[0][i] * sticks[2][k])
            if j < g and k < b:
                dp[i][j + 1][k + 1] = max(dp[i][j + 1][k + 1], dp[i][j][k] + sticks[1][j] * sticks[2][k])
            ans = max(ans, dp[i][j][k])
print(ans)
