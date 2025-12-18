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
def BS(arr, l, r, x):
    if r >= l:
        mid = l + (r - l)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return BS(arr, l, mid-1, x)
        else:
            return BS(arr, mid+1, r, x)
    else:n -1
from bisect import bisect_left as bl
from bisect import bisect_right as br
import itertools
import math
from Queue import Queue as Q
import heapq
from random import randint as rn
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
"""---------------------------------------------------------------------"""
q=[]
for _ in range(input()):
    a=int(stdin.readline())
    b=map(int,stdin.readline().split())
    w={}
    for i in range(a):
        if(w.has_key(b[i])):
            w[b[i]]+=1
        else:
            w[b[i]]=1
    s=-1
    l=0
    mi=2325234324324234
    d=[]
    for i in w:
        if(w[i]>=4):
            t=[str(i),str(i),str(i),str(i)]
            q.append(" ".join(t))
            l=1
            break
        if(w[i]>=2):
            d.append(i)
    if(l==1):
        continue
    d.sort()
    for i in range(len(d)):
        if(s==-1):
            s=d[i]
        else:
            r=float(s)/float(d[i])
            r+=float(d[i])/float(s)
            if(r<mi):
                p=[str(d[i]),str(s)]
                mi=r
            s=d[i]
    p=p*2
    q.append(" ".join(p))
stdout.write("\n".join(q))
