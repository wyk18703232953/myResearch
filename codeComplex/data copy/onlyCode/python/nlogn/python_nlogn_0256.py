'''Author- Akshit Monga'''
from sys import stdin, stdout
import bisect
input = stdin.readline
t = 1
for _ in range(t):
    n,q=map(int,input().split())
    a=[int(x) for x in input().split()]
    pre=[]
    s=0
    for i in a:
        s+=i
        pre.append(s)
    lost=0
    val_lost=0
    ans=[]
    qu=[int(x) for x in input().split()]
    for i in qu:
        val=i+val_lost
        b=bisect.bisect_left(pre,val,lost,n)
        val_lost=min(val,pre[-1])
        if b==n:
            lost = 0
            val_lost = 0
            ans.append(n)
            continue
        if pre[b]==val:
            lost=b+1
        else:
            lost=b
        if lost==n:
            lost = 0
            val_lost = 0
        ans.append(n-lost)
    for i in ans:
        print(i)