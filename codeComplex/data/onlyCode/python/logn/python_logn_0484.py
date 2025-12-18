import sys
#import random
from bisect import bisect_left as lb
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

for _ in range (1) :
    n = ii()

    x = 1
    i = 0

    while (x <= n) :
        x += (9*(i+1)*(10**i))
        i += 1

    x -= 9*i*(10**(i-1))

    y = str(10**(i-1) + (n-x)//i)

    #print(x,y)

    print(y[(n-x)%i])
