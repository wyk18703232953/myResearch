from sys import stdin
input=stdin.readline
from collections import defaultdict
def f(q):
    q.sort()
    d=defaultdict(int)
    for l,r in q:
        d[l]+=1
        d[r+1]-=1
    res=0
    prev=None
    ans=[0]*(len(q)+1)
    for i in sorted(d.keys()):
        # print(res,ans,prev,i)
        if prev==None:
            # ans[1]+=1
            prev=i
        else:
            ans[res]+=i-prev
            prev=i
        res+=d[i]
        # res+=d[i]
    return ans[1:]

n=int(input())
q=[]
for i in range(n):
    x,y=map(int,input().strip().split())
    q.append((x,y))
print(*f(q))