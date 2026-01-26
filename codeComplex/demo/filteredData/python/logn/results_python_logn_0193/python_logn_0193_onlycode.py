import sys
#import random
from bisect import bisect_right as lb
from collections import deque
#sys.setrecursionlimit(10**8)
from queue import PriorityQueue as pq
from math import *
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
inv =lambda x:pow(x,mod-2,mod)
mod = 10**9 + 7

n,s = il()

l = s
h = n
ans = n+1

while (l<=h) :
    m = (l+h)//2

    t = 0

    for i in str(m) :
        t += int(i)

    if (m-t >= s) :
        ans = m
        h = m-1
    else :
        l = m+1

print(n-ans+1)
    
