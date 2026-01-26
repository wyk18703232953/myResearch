from sys import stdin,stdout
from collections import Counter
nmbr=lambda:int(stdin.readline())
lst = lambda: list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr()):
    n,k=lst()
    a=lst()
    d={};r=l=-2
    for i in range(n):
        d[a[i]]=d.get(a[i],0)+1
        if len(d)==k:
            r=i
            break
    for i in range(r+1):
        if d[a[i]]==1:
            l=i
            break
        d[a[i]]-=1
    print(l+1,r+1)