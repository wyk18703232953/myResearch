import sys, math
from sys import stdin, stdout

rem = 10 ** 9 + 7
inf=10**18
sys.setrecursionlimit(10 ** 6 + 7)
#from resource import *; setrlimit(RLIMIT_STACK, (RLIM_INFINITY, RLIM_INFINITY))
take = lambda: map(int, stdin.readline().split())
from heapq import heappush, heappop, heapify
from collections import deque
from bisect import *


n,m=take()
arr=take()
check=take()
cnt=[0 for i in range(n+m)]

left=[-1 for i in range(n+m)]
right=[-1 for i in range(n+m)]
prev=-1
for i in range(n+m):
    if check[i]==0:
        left[i]=prev
    else:
        prev=i
prev=-1
for i in range(n+m-1,-1,-1):
    if check[i]==0:
        right[i]=prev
    else:
        prev=i
for i in range(n+m):
    if check[i]==1:
        continue
    a=left[i]
    b=right[i]
    if a==-1 and b==-1:
        continue
    if a==-1 and b!=-1:
        cnt[b]+=1
    if a!=-1 and b==-1:
        cnt[a]+=1
    if a!=-1 and b!=-1:
        if abs(arr[i]-arr[a])<=abs(arr[i]-arr[b]):
            cnt[a]+=1
        else:
            cnt[b]+=1
ans=[]
for i in range(n+m):
    if check[i]==1:
        ans.append(str(cnt[i]))
stdout.write(' '.join(ans))


