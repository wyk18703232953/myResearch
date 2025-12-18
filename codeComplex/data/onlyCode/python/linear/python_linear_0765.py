#import resource
import sys
#resource.setrlimit(resource.RLIMIT_STACK, [0x100000000, resource.RLIM_INFINITY])
#import threading
#threading.Thread(target=main).start()
#threading.stack_size(2**26)
#sys.setrecursionlimit(10**6)
mod=(10**9)+7
#fact=[1]
#for i in range(1,100001):
#    fact.append((fact[-1]*i)%mod)
#ifact=[0]*100001
#ifact[100000]=pow(fact[100000],mod-2,mod)
#for i in range(100000,0,-1):
#    ifact[i-1]=(i*ifact[i])%mod
from sys import stdin, stdout
import bisect
from bisect import bisect_left as bl
from bisect import bisect_right as br
import itertools
import collections
import math
import heapq
from random import randint as rn
from Queue import Queue as Q
def modinv(n,p):
    return pow(n,p-2,p)
def ncr(n,r,p):
    t=((fact[n])*((ifact[r]*ifact[n-r])%p))%p
    return t
def ain():
    return map(int,sin().split())
def sin():
    return stdin.readline().strip()
def GCD(x,y):
    while(y):
        x, y = y, x % y
    return x
def isprime(x):
    if(x==1):
        return False
    elif(x<4):
        return True
    for i in range(2,int(math.sqrt(x))+1):
        if(x%i==0):
            return False
    return True
"""**************************************************************************"""
n,q=ain()
a=ain()
g=max(a)
d=collections.deque(a)
f=0
an1=[]
while(d[0]!=g):
    f+=1
    x=d.popleft()
    y=d.popleft()
    an1.append(str(x)+" "+str(y))
    if(y==g):
        d.appendleft(y)
        d.append(x)
        break
    if(x<y):
        d.appendleft(y)
        d.append(x)
    else:
        d.appendleft(x)
        d.append(y)
r=[]
ans=[]
for i in range(n):
    r.append(str(d.popleft()))
for i in range(q):
    b=int(sin())
    if(b<=f):
        ans.append(an1[b-1])
    else:
        b-=f
        b-=1
        b%=(n-1)
        ans.append(r[0]+" "+r[b+1])
stdout.write("\n".join(ans))
