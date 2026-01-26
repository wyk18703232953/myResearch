import sys
import math
import collections
import bisect
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
for t in range(1):
    n,m=get_ints()
    space=0
    saved=[]
    for i in range(n):
        a,b=get_ints()
        space+=a
        saved.append(a-b)
    saved.sort(reverse=True)
    if space-sum(saved)>m:
        print(-1)
        continue
    i=0
    count=0
    if space<=m:
        print(0)
        continue
    while i<n:
        count+=1
        space-=saved[i]
        if space<=m:
            print(count)
            break
        i+=1