r, g, b = map(int, input().split(' '))
R = list(map(int, input().split(' ')))
G = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))
dp = [[[-1 for i in range(b+1)] for i in range(g+1)] for i in range(r+1)]
R.sort(reverse=True)
G.sort(reverse=True)
B.sort(reverse=True)
R.insert(0, 0)
G.insert(0, 0)
B.insert(0, 0)
dp[0][0][0], ans = 0, 0
for i in range(0, r+1):
    for j in range(0, g+1):
        for k in range(0, b+1):
            if i == 0 and j == 0 and k == 0:continue
            if i and j and dp[i - 1][j - 1][k] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + R[i] * G[j])
            if k and j and dp[i][j - 1][k - 1] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + B[k] * G[j])
            if i and k and dp[i - 1][j][k - 1] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + R[i] * B[k])
            ans = max(ans,dp[i][j][k])
print(ans)