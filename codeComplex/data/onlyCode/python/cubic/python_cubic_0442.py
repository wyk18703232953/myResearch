import sys
import os.path
from collections import *
import math
import bisect

if (os.path.exists('input.txt')):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


############## Code starts here ##########################

n, m, k1 = [int(x) for x in input().split()]

arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = [int(x) for x in input().split()]

brr = [0 for i in range(n - 1)]
for i in range(n - 1):
    brr[i] = [int(x) for x in input().split()]

dp = [[[0 for k in range(11)] for j in range(m)] for i in range(n)]

for k in range(1, 11):
    for i in range(n):
        for j in range(m):
                dp[i][j][k] = 10 ** 9
                if i > 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k - 1] + brr[i - 1][j] * 2)
                if i < n - 1:
                    dp[i][j][k] = min(dp[i][j][k], dp[i + 1][j][k - 1] + brr[i][j] * 2)
                if j > 0:
                    dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][k - 1] + arr[i][j - 1] * 2)
                if j < m - 1:
                    dp[i][j][k] = min(dp[i][j][k], dp[i][j + 1][k - 1] + arr[i][j] * 2)

for i in range(n):
    for j in range(m):
        if(k1 % 2):
            print(-1,end=" ")
        else:
            print(dp[i][j][k1 // 2],end=" ")
    print()

############## Code ends here ############################
