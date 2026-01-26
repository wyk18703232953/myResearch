import math,sys,bisect,heapq
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache
#sys.setrecursionlimit(200000000)
int1 = lambda x: int(x) - 1
#def input(): return sys.stdin.readline().strip()m
input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
aj = lambda: list(map(int, input().split()))
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
#MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])

def fun(A):
    for i in range(len(A)):
        if A[i] == 0:
            return i
    return 1
    
    
dp = [0]*10
A = aj();A.sort()
k1,k2,k3 = A
for i in range(0,10,k1):
    dp[i] = 1
for i in range(fun(dp),10,k2):
    dp[i] = 1
for i in range(fun(dp),10,k3):
    dp[i] = 1
Y(0 not in dp)
    
    