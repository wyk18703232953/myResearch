n, K = map(int, input().split())
dp = [[[0] * 4 for j in range(K + 2)] for i in range(n)]
MOD = 998244353
dp[0][1][0] = 1
dp[0][1][1] = 1
dp[0][2][2] = 1
dp[0][2][3] = 1
for i in range(n - 1):
    for j in range(1, K + 1):
        if j < K + 1:
            for k in range(4):
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j][k] %= MOD

            for k in range(2):
                dp[i + 1][j][k] += dp[i][j][2]
                dp[i + 1][j][k] %= MOD

            for k in range(2):
                dp[i + 1][j][k] += dp[i][j][3]
                dp[i + 1][j][k] %= MOD

    for j in range(1, K):
        for k in range(4):
            if k != 0:
                dp[i + 1][j + 1][k] += dp[i][j][0]
                dp[i + 1][j + 1][k] %= MOD

        for k in range(4):
            if k != 1:
                dp[i + 1][j + 1][k] += dp[i][j][1]
                dp[i + 1][j + 1][k] %= MOD

        if j + 2 < K + 1:
            dp[i + 1][j + 2][2] += dp[i][j][3]
            dp[i + 1][j + 2][2] %= MOD
            dp[i + 1][j + 2][3] += dp[i][j][2]
            dp[i + 1][j + 2][3] %= MOD

num = 0
for i in range(4):
    num += dp[n - 1][K][i]
    num %= MOD

print(num)