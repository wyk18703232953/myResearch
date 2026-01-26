import os
import sys
import math
import heapq
from decimal import *
from io import BytesIO, IOBase
from collections import defaultdict, deque

def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))

r,g,b = rm()
R = rl()
G = rl()
B = rl()
R.sort()
G.sort()
B.sort()
dp = [[[0]*(b+1) for j in range(g+1)] for i in range(r+1)]
for i in range(r+1):
    for j in range(g+1):
        for k in range(b+1):
            if i and j:
                dp[i][j][k]=max(dp[i][j][k], dp[i-1][j-1][k]+R[i-1]*G[j-1])
            if j and k:
                dp[i][j][k]=max(dp[i][j][k], dp[i][j-1][k-1]+G[j-1]*B[k-1])
            if k and i:
                dp[i][j][k]=max(dp[i][j][k], dp[i-1][j][k-1]+B[k-1]*R[i-1])
print(dp[r][g][b])