from math import *
from collections import *
from random import *
from decimal import Decimal
from heapq import *
from bisect import *
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
def lis():
    return list(map(int,input().split()))
def ma():
    return map(int,input().split())
def inp():
    return int(input())
def st1():
    return input().rstrip('\n')
t=1
while(t):
    t-=1
    r,g,b=ma()
    rl=lis()
    gl=lis()
    bl=lis()
    rl.sort()
    bl.sort()
    gl.sort()
    dp= [[[0]*(b+1)for i in range(g+1)] for j in range(r+1)]
    for i in range(r+1):
        for j in range(g+1):
            for k in range(b+1):
                if(i+j+k<2):
                    continue
                if(i and j):
                    dp[i][j][k]=max(dp[i][j][k],dp[i-1][j-1][k]+rl[i-1]*gl[j-1])
                if(j and k):
                    dp[i][j][k]=max(dp[i][j][k],dp[i][j-1][k-1]+gl[j-1]*bl[k-1])
                if(i and k):
                    dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k-1]+rl[i-1]*bl[k-1])
    print(dp[r][g][b])
    
        
