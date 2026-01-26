import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
# from math import *
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
import copy
import time
# import numpy as np
starttime = time.time()
# import numpy as np
mod = int(pow(10, 9) + 7)
mod2 = 998244353
def data(): return sys.stdin.readline().strip()
def out(*var, end="\n"): sys.stdout.write(' '.join(map(str, var))+end)
def L(): return list(sp())
def sl(): return list(ssp())
def sp(): return map(int, data().split())
def ssp(): return map(str, data().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(n, val) for j in range(m)]

try:
    # sys.setrecursionlimit(int(pow(10,6)))
    sys.stdin = open("input.txt", "r")
    # sys.stdout = open("../output.txt", "w")
except:
    pass
global ans
ans=0

def rec(i,j,k):
    if dp[i][j][k]!=-1:
        return dp[i][j][k]
    x1=x2=x3=0
    if i<R and j<G:
        x1=r[i]*g[j]+rec(i+1,j+1,k)
    if i<R and k<B:
        x2=r[i]*b[k]+rec(i+1,j,k+1)
    if j<G and k<B:
        x3=g[j]*b[k]+rec(i,j+1,k+1)
    dp[i][j][k]=max(x1,x2,x3)
    global ans
    ans=max(ans,dp[i][j][k])
    return dp[i][j][k]

for _ in range(1):
    R,G,B=L()
    r=L()
    g=L()
    b=L()
    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)
    dp=[[[-1 for k in range(B+1)] for j in range(G+1)] for i in range(R+1)]
    rec(0,0,0)
    print(ans)



endtime = time.time()
# print(f"Runtime of the program is {endtime - starttime}")

