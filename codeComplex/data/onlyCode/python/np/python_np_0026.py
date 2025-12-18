from collections import defaultdict, Counter,deque
from math import sqrt, log10, log, floor, factorial,gcd
from bisect import bisect_left, bisect_right
from itertools import permutations,combinations
import sys, io, os
input = sys.stdin.readline
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# sys.setrecursionlimit(10000)
inf = float('inf')
mod = 10 ** 9 + 7
def yn(a): print("YES" if a else "NO")
ceil = lambda a, b: (a + b - 1) // b
lim=22
po=[1<<j for j in range(lim+1)]
maxbits=lim
masks=po[lim]
dp=[-1]*masks
t=1
for i in range(1):
    n=int(input())
    l=[int(i) for i in input().split()]
    for i in l:
        dp[i]=i
    for i in range(masks):
        for j in range(maxbits):
            if dp[i]==-1 and i&po[j]:
                dp[i]=dp[i-po[j]]
    ans=[dp[i^(masks-1)] for i in l]
    print(*ans)








