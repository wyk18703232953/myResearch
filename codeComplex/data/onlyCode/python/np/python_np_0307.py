import sys
input = sys.stdin.readline
import math
import copy
import collections
from collections import deque
import heapq
import itertools
from collections import defaultdict
from collections import Counter

n,k = map(int,input().split())
mod = 998244353
dp = [[[0 for z in range(2)] for j in range(k+1)] for i in range(n)]
# z= 0: bb, 1:bw, 2:wb, 3=ww
dp[0][1][0] = 1
if k>=2:
    dp[0][2][1] = 1
for i in range(1,n):
    for j in range(1,k+1):
        dp[i][j][0] += dp[i-1][j-1][0]+dp[i-1][j][0]+2*dp[i-1][j][1]
        dp[i][j][0]%=mod
        if j-2>=0:
            dp[i][j][1] += 2*dp[i-1][j-1][0]+dp[i-1][j][1]+dp[i-1][j-2][1]
        else:
            dp[i][j][1] += dp[i-1][j-1][0]+dp[i-1][j][1]+dp[i][j-1][0]
        dp[i][j][1]%=mod
ans = 0
for z in range(2):
    ans+=dp[n-1][k][z]
ans*=2
print(ans%mod)
# for row in dp:
#     print(row)