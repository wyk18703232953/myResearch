import sys
#import random
#import bisect
from collections import deque
#sys.setrecursionlimit(10**6)
from queue import PriorityQueue
from math import gcd
from math import log
from math import ceil
from math import pi
input_ = lambda: sys.stdin.readline().strip("\r\n")
ii = lambda : int(input_())
il = lambda : list(map(int, input_().split()))
ilf = lambda : list(map(float, input_().split()))
ip = lambda : input_()
fi = lambda : float(input_())
ap = lambda ab,bc,cd : ab[bc].append(cd)
li = lambda : list(input_())
pr = lambda x : print(x)
prinT = lambda x : print(x)
f = lambda : sys.stdout.flush()
mod = 10**9 + 7

n,mod = il()
N = 406

fact = [1 for i in range (N)]
inver = [1 for i in range (N)]
power2 = [1 for i in range (N)]
ncr = [[1 for i in range (N)] for j in range (N)]
dp = [[0 for i in range (N)] for j in range (N)]

def precom() :

    fact[0] = 1
    inver[0] = 1

    for i in range (1,N) :
        fact[i] = (fact[i-1]*i)%mod
        inver[i] = pow(fact[i],mod-2,mod)

    for i in range (N) :
        for j in range (i+1) :
            ncr[i][j] = (((fact[i]*inver[j])%mod)*inver[i-j])%mod

    for i in range(1,N) :
        power2[i] = (power2[i-1]*2)%mod

precom()

dp[0][0] = 1

for i in range (n) :
    for j in range (i+1) :
        k = 1
        while (k+i <= n) :

            dp[i+k+1][j+k] = (dp[i+k+1][j+k] + ((dp[i][j]*power2[k-1])%mod*ncr[j+k][k])%mod)%mod
            
            k += 1

ans = 0

for i in range (n+1) :
    ans = (ans + dp[n+1][i])%mod

print(ans)

    
