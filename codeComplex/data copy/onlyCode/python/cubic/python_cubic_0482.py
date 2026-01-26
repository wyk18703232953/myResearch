# coding:utf-8
# @Author: 将立

n, m, K = map(int, input().split())
wh = [[0]*m for i in range(n)]
wv = [[0]*m for i in range(n)]

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(m-1):
        wh[i][j] = t[j]

for i in range(n-1):
    t = list(map(int, input().split()))
    for j in range(m):
        wv[i][j] = t[j]


f = [[[int(1e8)]* 11 for j in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        f[i][j][0] = 0

for k in range(1, K//2+1):
    for i in range(n):
        for j in range(m):
            if i > 0:
                f[i][j][k] = min(f[i][j][k], f[i-1][j][k-1]+wv[i-1][j])
            if j < m-1:
                f[i][j][k] = min(f[i][j][k], f[i][j+1][k-1]+wh[i][j])
            if i < n-1:
                f[i][j][k] = min(f[i][j][k], f[i+1][j][k-1]+wv[i][j])
            if j > 0:
                f[i][j][k] = min(f[i][j][k], f[i][j-1][k-1]+wh[i][j-1])

for i in range(n):
    for j in range(m):
        if K%2 == 1:
            print(-1)
        else:
            dp = [int(1e8)]*(K//2+1)
            dp[0] = 0
            for k in range(1, K//2+1):
                for l in range(0, k):
                    dp[k] = min(dp[k], dp[l]+f[i][j][k-l]*2)

            print(dp[K//2])
