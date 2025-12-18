from sys import stdin,stdout
from itertools import accumulate
nmbr=lambda:int(stdin.readline())
lst=lambda:list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr())
    n,x=lst()
    a=lst()
    ans=0
    s=set(a)
    if len(s) != n:
        print(0)
        continue
    for i in range(n):
        v=a[i]
        a[i]&=x
        if a[i] in s and v!=a[i]:
            # print(s,a[i])
            ans=1
            break
    if ans==1:print(1)
    elif len(set(a))==n:print(-1)
    else:print(2)