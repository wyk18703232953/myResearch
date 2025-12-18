from sys import stdin, setrecursionlimit, stdout
#setrecursionlimit(1000000) #use "python" instead of "pypy" to avoid MLE
from collections import deque
from math import sqrt, floor, ceil, log, log2, log10, pi, gcd, sin, cos, asin
from heapq import heapify, heappop, heappush, heapreplace, heappushpop
from bisect import bisect_right, bisect_left
def ii(): return int(stdin.readline())
def fi(): return float(stdin.readline())
def mi(): return map(int, stdin.readline().split())
def fmi(): return map(float, stdin.readline().split())
def li(): return list(mi())
def si(): return stdin.readline().rstrip()
def lsi(): return list(si())
mod=1000000007
res=['NO', 'YES']


#######################################################################################
###########################    M Y     F U N C T I O N S    ###########################
#######################################################################################




#######################################################################################
###########################    M A I N     P R O G R A M    ###########################
#######################################################################################

aa=[9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]
a=[9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889, 98888888889, 1088888888889]

test=1
test_case=1
while test<=test_case:
    test+=1



    n=ii()
    if n in a:
        n=9
    if n<10:
        print(n)
        exit()
    x=1
    while a[x]<n:
        x+=1
    v=n-a[x-1]
    z=v//(x+1)
    z+=aa[x-1]
    v%=x+1
    #print(v, x, z)
    if not v:
        p=z%10
    else:
        z+=1
        p=int(str(z)[v-1])
    print(p)