from sys import stdin
input=stdin.readline
from collections import defaultdict
def f(d,n):
    res=0
    prev=None
    ans=[0]*(n+1)
    for i in sorted(d.keys()):
        # print(res,ans,prev,i)
        if prev==None:
            prev=i
        else:
            ans[res]+=i-prev
            prev=i
        res+=d[i]
    return ans[1:]

n=int(input())
d=defaultdict(int)
for i in range(n):
    x,y=map(int,input().strip().split())
    d[x]+=1
    d[y+1]-=1
print(*f(d,n))