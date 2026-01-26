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
s = []
for _ in range(4):
    tmp = [input() for i in range(n)]
    if _<3: input()
    s.append(tmp)
res = INF
for pt in itertools.combinations(range(4),2):
    cnt = 0
    for k in range(4):
        f = 1 if k in pt else 0
        for i in range(n):
            for j in range(n):
                if (i+j+f)%2 != int(s[k][i][j]): cnt += 1
    res = min(res, cnt)
print(res)