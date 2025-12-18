import sys,os,io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
from collections import defaultdict

n,m = [int(i) for i in input().split()]
a = []
mi = -1
ma = 10**9
for i in range (n):
    a.append([int(j) for j in input().split()])

ans = []
while(mi<ma):
    mid = (mi+ma+1)//2
    masks = {}
    for i in range (n):
        currMask = 0
        for j in range (m):
            if a[i][j] >= mid:
                currMask +=  1<<j
        masks[currMask] = i
    req = (1<<m) - 1
    possible = 0
    for i in masks:
        for j in masks:
            if i|j == req:
                possible = 1
                ans = [masks[i]+1,masks[j]+1]
                break
        if possible:
            break
    if possible:
        mi = mid
    else:
        ma = mid - 1
print(*ans)