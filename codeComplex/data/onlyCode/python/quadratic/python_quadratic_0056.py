import sys,math,itertools
from collections import Counter,deque,defaultdict
from bisect import bisect_left,bisect_right 
from heapq import heappop,heappush,heapify, nlargest
from copy import deepcopy
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_1(): return list(map(lambda x:int(x)-1, sys.stdin.readline().split()))
def inps(): return sys.stdin.readline()
def inpsl(x): tmp = sys.stdin.readline(); return list(tmp[:x])
def err(x): print(x); exit()

n = inp()
a = inpl()
res = 0
for i in range(n):
    for j in range(i+1,n):
        if a[i] > a[j]:
            res = 1-res
for _ in range(inp()):
    l,r = inpl(); m = r-l+1
    swap = m*(m-1)//2
    if swap%2: res = 1-res
    print('odd' if res else 'even')