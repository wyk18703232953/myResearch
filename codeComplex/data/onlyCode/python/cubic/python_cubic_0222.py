#!/usr/bin/env python3
import sys
input = sys.stdin.readline
import heapq

R, G, B = map(int, input().split())
r = [int(item) for item in input().split()]
g = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]
r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)
nr = len(r)
ng = len(g)
nb = len(b)

dp = [[[0] * (nb+1) for _ in range(ng+1)] for _ in range(nr+1)]
ans = 0
for i in range(nr + 1):
    for j in range(ng + 1):
        for k in range(nb + 1):
            if (i + j + k) % 2 == 1:
                continue
            if i > 0 and j > 0:
                # Make RG
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k] + r[i-1] * g[j-1])
            if j > 0 and k > 0:
                # Make GB
                dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1] + g[j-1] * b[k-1])
            if i > 0 and k > 0:
                # Make BR
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1] + b[k-1] * r[i-1])
            ans = max(ans, dp[i][j][k])

print(ans)