#import resource
#import sys
#resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])
#import threading
#threading.stack_size(2**26)
#sys.setrecursionlimit(0x1000000)
from sys import stdin, stdout
mod=(10**9)+7
mod1=mod-1
def modinv(n,p):
    return pow(n,p-2,p)
def ncr(n,r,p):
    t=((fact[n])*(modinv(fact[r],p)%p)*(modinv(fact[n-r],p)%p))%p
    return t
def GCD(x, y):
   while(y):
       x, y = y, x % y
   return x
"""def BS(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BS(arr, l, mid-1, x)
        else:
            return BS(arr, mid+1, r, x)
    else:n -1
"""
from bisect import bisect_left as bl
from bisect import bisect_right as br
import itertools
import math
import heapq
from random import randint as rn
from Queue import Queue as Q
def comp(x,y):
    if(x[0]<y[0]):
        return -1
    elif(x[0]==y[0]):
        if(x[1]<y[1]):
            return -1
        else:
            return 1
    else:
        return 1
import heapq
k=[(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2)]
def gg(i,j):
    if(i<n-2 and j<m-2):
        f=0
        for g in range(8):
            if(w[i+k[g][0]][j+k[g][1]]=="."):
                f=1
        if(f!=1):
            for g in range(8):
                p[i+k[g][0]][j+k[g][1]]=1
"""*********************************************************************************"""
n=input()
w=n
d=1
p=[]
while(n!=1):
    t=(n+1)/2
    for i in range(t):
        p.append(str(d))
    n-=t
    if(n==1):
        break
    d*=2
if(w%d==0):
    p.append(str(w))
else:
    g=w/d
    r=d*g
    p.append(str(r))
stdout.write(" ".join(p))
