import sys, math
import io, os
#data = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
#from itertools import permutations,combinations
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var) : sys.stdout.write('\n'.join(map(str, var))+'\n')
def out(var) : sys.stdout.write(str(var)+'\n')
from decimal import Decimal
from fractions import Fraction
#sys.setrecursionlimit(100000)
INF = float('inf')
mod = int(1e9)+7


def recur(r,g,b):
    if (r+b+g)==r or (r+b+g)==g or (r+b+g)==b:
        return 0
    if dp[r][g][b]:
        return dp[r][g][b]
    if r>0 and g>0:
        dp[r][g][b]=max(dp[r][g][b],R[r-1]*G[g-1]+recur(r-1,g-1,b))
    if r>0 and b>0:
        dp[r][g][b]=max(dp[r][g][b],R[r-1]*B[b-1]+recur(r-1,g,b-1))
    if b>0 and g>0:
        dp[r][g][b]=max(dp[r][g][b],B[b-1]*G[g-1]+recur(r,g-1,b-1))
    return dp[r][g][b]

r,g,b=mdata()
R=sorted(mdata())
G=sorted(mdata())
B=sorted(mdata())
dp=[[[0]*(b+1) for i in range(g+1)] for i in range(r+1)]
out(recur(r,g,b))
