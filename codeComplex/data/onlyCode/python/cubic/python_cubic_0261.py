nr, ng, nb = map(int, input().split())
r = sorted([int(i) for i in input().split()])
g = sorted([int(i) for i in input().split()])
b = sorted([int(i) for i in input().split()])

dp = [[[0 for _ in range(nb + 1)] for _ in range(ng + 1)] for _ in range(nr + 1)]
for i in range(nr + 1):
    for j in range(ng + 1):
        for k in range(nb + 1):
            val = 0
            if i - 1 >= 0 and j - 1 >= 0:
                val = max(val, r[i - 1] * g[j - 1] + dp[i - 1][j - 1][k])
            if i - 1 >= 0 and k - 1 >= 0:
                val = max(val, r[i - 1] * b[k - 1] + dp[i - 1][j][k - 1])
            if j - 1 >= 0 and k - 1 >= 0:
                val = max(val, g[j - 1] * b[k - 1] + dp[i][j - 1][k - 1])
            dp[i][j][k] = val

print(dp[nr][ng][nb])
