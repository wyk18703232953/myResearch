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
INF = float('inf')
mod = int(1e9) + 7


def cal(l,r):
    if l==r:
        dp1[l][r]=1
        dp2[l][r]=a[l]
    if dp1[l][r]:
        return dp1[l][r]
    for i in range(l,r):
        if cal(l,i)==1 and cal(i+1,r)==1 and dp2[l][i]==dp2[i+1][r]:
            dp1[l][r]=1
            dp2[l][r]=dp2[l][i]+1
    if not dp2[l][r]:
        dp1[l][r]=2
    return dp1[l][r]

def cal2(l,r):
    if dp1[l][r]==1:
        dp3[l][r]=1
        return 1
    elif dp3[l][r]:
        return dp3[l][r]
    ans=INF
    for i in range(l,r):
        ans=min(cal2(l,i)+cal2(i+1,r),ans)
    dp3[l][r]=ans
    return ans


n=int(data())
a=mdata()
ans=[n]
dp1=[[0]*n for i in range(n)]
dp2=[[0]*n for i in range(n)]
dp3=[[0]*n for i in range(n)]
cal(0,n-1)
cal2(0,n-1)
out(dp3[0][n-1])