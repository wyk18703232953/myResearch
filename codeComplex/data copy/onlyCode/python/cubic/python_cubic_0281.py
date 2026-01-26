import math
import time
from collections import defaultdict,deque,Counter
from sys import stdin,stdout
from bisect import bisect_left,bisect_right
from queue import PriorityQueue 
import sys
t=1
# t=int(input())
for _ in range(t):
    r,g,b=map(int,stdin.readline().split())
    ra=list(map(int,stdin.readline().split()))
    ga=list(map(int,stdin.readline().split()))
    ba=list(map(int,stdin.readline().split()))
    ra.sort()
    ga.sort()
    ba.sort()
    dp=[[[0]*201 for _ in range(201)]for _ in range(201)]
    for i in range(r+1):
        for j in range(g+1):
            for k in range(b+1):
                if(i and j>0):
                    dp[i][j][k]=max(dp[i][j][k], dp[i-1][j-1][k]+ra[i-1]*ga[j-1])
                if(i and k>0):
                    dp[i][j][k]=max(dp[i][j][k], dp[i-1][j][k-1]+ra[i-1]*ba[k-1])
                if(k and j>0):
                    dp[i][j][k]=max(dp[i][j][k], dp[i][j-1][k-1]+ga[j-1]*ba[k-1])
    print(dp[r][g][b])
