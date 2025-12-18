import sys, math
import io, os
# data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
# from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
# from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')
from decimal import Decimal
# from fractions import Fraction
# sys.setrecursionlimit(100000)
INF = 10001
mod = int(1e9) + 7


def cal(l,r):
    if l==r:
        dp1[l][r]=a[l]
        dp3[l][r] = 1
        return dp1[l][r]
    if dp1[l][r]!=-1:
        return dp1[l][r]
    for i in range(l,r):
        if cal(l,i) == cal(i+1,r) != 0:
            dp1[l][r]=dp1[l][i]+1
            dp3[l][r]=1
        dp3[l][r]=min(dp3[l][r],dp3[l][i]+dp3[i+1][r])
    if dp1[l][r] == -1:
        dp1[l][r] = 0
    return dp1[l][r]


n=int(data())
a=mdata()
ans=[n]
dp1=[[-1]*n for i in range(n)]
dp3=[[10001]*n for i in range(n)]
cal(0,n-1)
out(dp3[0][n-1])