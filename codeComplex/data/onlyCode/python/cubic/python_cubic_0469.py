'''input

'''
import sys
import math
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd


# sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

mod=1000000007

#main code
#!Q4
n,m,k=mul()

dp=[[[0 for l in range(k//2+1)]for j in range(m)]for i in range(n)]
h=[]
v=[]
for i in range(n):
    h.append(seq())
for i in range(n-1):
    v.append(seq())

def sol(n,m,k):
    for l in range(1,k//2+1):
        for i in range(n):
            for j in range(m):
                dp[i][j][l]=float("inf")
                if j-1>=0:
                    dp[i][j][l]=min(dp[i][j][l],dp[i][j-1][l-1]+h[i][j-1])
                if i-1>=0:
                    dp[i][j][l]=min(dp[i][j][l],dp[i-1][j][l-1]+v[i-1][j])
                if j+1<m:
                    dp[i][j][l]=min(dp[i][j][l],dp[i][j+1][l-1]+h[i][j])
                if i+1<n:
                    dp[i][j][l]=min(dp[i][j][l],dp[i+1][j][l-1]+v[i][j])
    return dp
if k%2:
    for i in range(n):
        for j in range(m):
            print(-1,end=" ")
        print()
else:
    ans=sol(n,m,k)
    for i in range(n):
        for j in range(m):
            print(2*ans[i][j][k//2],end=" ")
        print()
