import sys
input=sys.stdin.readline
from collections import defaultdict as dc
from collections import Counter
from bisect import bisect_right, bisect_left
import math
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import PriorityQueue as pq
n,m=map(int,input().split())
l=list(map(int,input().split()))
x=dc(int)
c=0
p=0
#print(l)
for i in l:
    x[i]+=1
    f=1
    for i in range(1,n+1):
        if x[i]==0:
            f=0
            break
    if f:
        p+=1
        for i in range(1,n+1):
            x[i]-=1
        
print(p)