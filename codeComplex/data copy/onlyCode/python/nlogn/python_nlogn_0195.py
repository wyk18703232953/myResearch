import sys
input=sys.stdin.readline
from collections import defaultdict as dc
from collections import Counter
from bisect import bisect_right, bisect_left,bisect
import math
from operator import itemgetter
from heapq import heapify, heappop, heappush
n=int(input())
l=list(map(int,input().split()))
x=dc(int)
y=dc(int)
z=dc(int)
p=dc(int)
q=dc(int)
r=dc(int)
x[l[-1]]+=1
y[l[-1]]+=1
z[l[-1]]+=1
for i in range(n-2,-1,-1):
    p[i]=x[l[i]]
    q[i]=y[l[i]+1]
    r[i]=z[l[i]-1]
    x[l[i]]+=1
    y[l[i]]+=1
    z[l[i]]+=1
#print(p)
#print(q)
#print(r)
x=[0]*n
for i in range(n-2,-1,-1):
    x[i]=l[i+1]+x[i+1]
#print(x)
s=0
for i in range(n-2,-1,-1):
    #print(x[i],p[i]*l[i],q[i]*(l[i]+1),r[i]*(l[i]-1))
    c=x[i]-(p[i]*l[i])-(q[i]*(l[i]+1))-(r[i]*(l[i]-1))
    d=n-i-1-p[i]-q[i]-r[i]
    e=c-l[i]*d
    #print(i,c,d,e)
    s+=e
print(s)