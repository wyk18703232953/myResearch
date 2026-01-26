import sys
input=sys.stdin.readline
from collections import defaultdict as dc
from collections import Counter
from bisect import bisect_right, bisect_left,bisect
import math
from operator import itemgetter
from heapq import heapify, heappop, heappush
n,k=map(int,input().split())
x,y=1,n
f=0
while(x<=y):
    m=(x+y)//2
    s=0
    p=m
    while(p>0):
        s+=p%10
        p=p//10
    m1=m-1
    s1=0
    p=m1
    while(p>0):
        s1+=p%10
        p=p//10
    if m==0 or (m-s>=k and m1-s1<k):
        f=1
        break
    elif m-s<k:
        x=m+1
    else:
        y=m-1
if f:
    print(n-m+1)
else:
    print(0)
        