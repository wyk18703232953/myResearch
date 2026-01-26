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

from functools import lru_cache

n,l,r,x = ilele()
A = alele()
A.sort()

@lru_cache(None)
def fun(pos = 0,sm = -1,la = -1,tot = 0):
    if pos == n:
        if tot >= l and tot <= r and la  > 0 and  (la - sm) >= x:
            return 1
        return 0
    if sm == -1:
        return fun(pos+1,A[pos],-1,A[pos]) + fun(pos+1,sm,la,tot)
    elif la == -1:
        return fun(pos+1,sm,A[pos],tot + A[pos]) + fun(pos+1,sm,la,tot)
    else:
        return fun(pos+1,sm,A[pos],tot + A[pos]) + fun(pos+1,sm,la,tot)
    
print(fun())
