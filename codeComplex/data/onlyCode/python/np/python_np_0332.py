import math,sys,bisect,heapq
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
ilele = lambda: map(int,input().split())
alele = lambda: list(map(int, input().split()))
ilelec = lambda: map(int1,input().split())
alelec = lambda: list(map(int1, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
#MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])
    
MOD = 998244353

N,K = ilele()
if K == 1 or K == 2*N:
    print(2)
    exit(0)
dp = list3d(N+1,4,K+1,0)
dp[1][0][1] = 1
dp[1][3][1] = 1
dp[1][1][2] = 1
dp[1][2][2] = 1

for n in range(2,N+1):
    for k in range(1,K+1):
        dp[n][0][k] = ((dp[n-1][0][k]+dp[n-1][1][k])%MOD+(dp[n-1][2][k]+dp[n-1][3][k-1])%MOD)%MOD
        dp[n][3][k] = ((dp[n-1][0][k-1]+dp[n-1][1][k])%MOD+(dp[n-1][2][k]+dp[n-1][3][k])%MOD)%MOD
        if k > 1:
            dp[n][1][k]=((dp[n-1][0][k-1]+dp[n-1][1][k])%MOD+(dp[n-1][2][k-2] +dp[n-1][3][k-1])%MOD)%MOD
            dp[n][2][k]=((dp[n-1][0][k-1]+dp[n-1][1][k-2])%MOD+(dp[n-1][2][k]+dp[n-1][3][k-1])%MOD)%MOD
        else:
            dp[n][1][k]=((dp[n-1][0][k-1]+dp[n-1][1][k])%MOD+(dp[n-1][3][k-1])%MOD)%MOD
            dp[n][2][k]=((dp[n-1][0][k-1])%MOD+(dp[n-1][2][k]+dp[n-1][3][k-1])%MOD)%MOD

print(((dp[N][0][K]+dp[N][1][K])%MOD+(dp[N][2][K]+dp[N][3][K])%MOD)%MOD)
            