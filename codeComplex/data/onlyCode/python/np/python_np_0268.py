import sys
#import random
from bisect import bisect_right as rb
from collections import deque
#sys.setrecursionlimit(10**8)
from queue import PriorityQueue
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

def bit(n) :
    if (n == 0) :return 0
    val = 1

    while (val&n) == 0 :
        val *= 2

    return val


n,q = il()
x = n+1

for i in range(q) :
    t1 = ii()

    for j in ip() :
        val = bit(t1)

        if (j == "U") :
            tem = (t1-val)|(val*2)
            if (tem < n) :
                t1 = tem
        elif (j == "L" and val>1) :
            t1 -= val//2
        elif (j == "R" and val>1) :
            t1 += val//2

    print(t1)
        
