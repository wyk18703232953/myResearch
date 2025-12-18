from collections import *
from itertools import *
from random import  *
from bisect import *
from string import *
from queue import *
from heapq import *
from math import *
from sys import *
from re import *
def fast(): return stdin.readline().strip()
def zzz(): return [int(i) for i in fast().split()]


z, zz = input, lambda: list(map(int, z().split()))
szz, graph, mod, szzz = lambda: sorted(
    zz()), {}, 10**9 + 7, lambda: sorted(zzz())


def lcd(xnum1, xnum2): return (xnum1 * xnum2 // gcd(xnum1, xnum2))
def output(answer): stdout.write(str(answer))


dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]


###########################---Test-Case---#################################
"""
 If you Know me , Then you probably don't know me !
"""
###########################---START-CODING---##############################


n,l,r,x = zzz()
arr = zzz()
cnt=0
for i in range(2,2**n):
    b = bin(i)[2:]
    b='0'*(n-len(b))+b
    s,mx,mi =0, float('-inf'),float('inf')
    for j in range(n):
        if b[j]=='1':
            mx=max(mx,arr[j])
            mi=min(mi,arr[j])
            s+=arr[j]
    if s>=l and s<=r and mx-mi>=x:
        cnt+=1
print(cnt)
