n, m, v = map(lambda x: int(x) + 1, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = []
for i in range(n):
    dp.append([])
    for j in range(m):
        dp[i].append([0] * v)
a.sort(reverse=1)
b.sort(reverse=1)
c.sort(reverse=1)
a = [0] + a
b = [0] + b
c = [0] + c
ans = 0
for i in range(n):
    for j in range(m):
        for k in range(v):
            if i == j == k == 0:
                continue
            if i == j == 0 or i == k == 0 or j == k == 0:
                continue
            if i == 0:
                dp[i][j][k] = dp[i][j - 1][k - 1] + \
                              b[j] * c[k]
            elif j == 0:
                dp[i][j][k] = dp[i - 1][j][k - 1] + \
                              a[i] * c[k]
            elif k == 0:
                dp[i][j][k] = dp[i - 1][j - 1][k] + \
                              a[i] * b[j]
            else:
                dp[i][j][k] = max(dp[i - 1][j - 1][k] + a[i] * b[j],
                                  dp[i - 1][j][k - 1] + a[i] * c[k],
                                  dp[i][j - 1][k - 1] + b[j] * c[k])
            ans = max(ans, dp[i][j][k])
print(ans)
