from sys import stdin, stdout
from math import floor, gcd, fabs, factorial, fmod, sqrt, inf, log
from collections import defaultdict as dd, deque
from heapq import merge, heapify, heappop, heappush, nsmallest
from bisect import bisect_left as bl, bisect_right as br, bisect
        
mod = pow(10, 9) + 7
mod2 = 998244353
        
def inp(): return stdin.readline().strip()
def iinp(): return int(inp())
def out(var, end="\n"): stdout.write(str(var)+"\n")
def outa(*var, end="\n"): stdout.write(' '.join(map(str, var)) + end)
def lmp(): return list(mp())
def mp(): return map(int, inp().split())
def smp(): return map(str, inp().split())
def l1d(n, val=0): return [val for i in range(n)]
def l2d(n, m, val=0): return [l1d(m, val) for j in range(n)]
def remadd(x, y): return 1 if x%y else 0
def ceil(a,b): return (a+b-1)//b
S1 = 'abcdefghijklmnopqrstuvwxyz'
S2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def isprime(x):
    if x<=1: return False
    if x in (2, 3): return True
    if x%2 == 0: return False
    for i in range(3, int(sqrt(x))+1, 2):
        if x%i == 0: return False
    return True
 
n, m, k = mp()
hor = [lmp() for i in range(n)]
ver = [lmp() for i in range(n-1)]
if k%2:
    ml = l2d(n, m, -1)
    for i in ml: print(*i)
    exit()
k//=2
dp = [l2d(n, m) for i in range(k+1)]
for f in range(1, k+1):
    for i in range(n):
        for j in range(m):
            a = inf
            if i!=0:
                a = min(a, 2*ver[i-1][j]+dp[f-1][i-1][j])
            if i!=n-1:
                a = min(a, 2*ver[i][j]+dp[f-1][i+1][j])
            if j!=0:
                a = min(a, 2*hor[i][j-1]+dp[f-1][i][j-1])
            if j!=m-1:
                a = min(a, 2*hor[i][j]+dp[f-1][i][j+1])
            dp[f][i][j] = a
for i in dp[-1]:
    print(*i)