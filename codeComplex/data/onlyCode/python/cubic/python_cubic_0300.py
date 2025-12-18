# Author: S Mahesh Raju
# Username: maheshraju2020
# Date: 19/08/2020

from sys import stdin, stdout, setrecursionlimit
from math import gcd, ceil, sqrt
from collections import Counter, deque
from bisect import bisect_left, bisect_right
ii1 = lambda: int(stdin.readline().strip())
is1 = lambda: stdin.readline().strip()
iia = lambda: list(map(int, stdin.readline().strip().split()))
isa = lambda: stdin.readline().strip().split()
setrecursionlimit(100000)
mod = 1000000007

R, G, B = iia()
r, g, b = sorted(iia()), sorted(iia()), sorted(iia())
dp = [[[0 for i in range(B + 1)] \
    for j in range(G + 1)] for k in range(R + 1)]

for i in range(R + 1):
    for j in range(G + 1):
        for k in range(B + 1):
            if i > 0 and j > 0:
                dp[i][j][k] = max(dp[i][j][k], \
                    dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
            if i > 0 and k > 0:
                dp[i][j][k] = max(dp[i][j][k], \
                    dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
            if j > 0 and k > 0:
                dp[i][j][k] = max(dp[i][j][k], \
                    dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])
print(dp[-1][-1][-1])
