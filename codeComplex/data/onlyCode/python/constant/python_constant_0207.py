import sys,os,io
import math,bisect,operator
inf,mod = float('inf'),10**9+7
# sys.setrecursionlimit(10 ** 6)
from itertools import groupby,accumulate
from heapq import heapify,heappop,heappush
from collections import deque,Counter,defaultdict
input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
Neo = lambda : list(map(int,input().split()))
# test, = Neo()
A = sorted(Neo())
B = [0]*100
for i in A:
    j = 0
    for c in range(100):
        if B[c] == 0:
            j = c
            break
            
    while j < 100:
        B[j] = 1
        j += i  
if B.count(0) == 0:
    print('YES')
else:
    print('NO')
