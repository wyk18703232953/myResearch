from collections import defaultdict
from sys import setrecursionlimit,stdin
input=stdin.readline
setrecursionlimit(100000)

def dfs(r,g,b,rr,gg,bb):
    if r<0 or g<0 or b<0:
        return 0
    x=0
    y=0
    z=0
    
    if dp[r][g][b]!=-1:
        return dp[r][g][b]
    if r!=0 and g!=0:
        x=rr[r-1]*gg[g-1]+dfs(r-1,g-1,b,rr,gg,bb)
    if r!=0 and b!=0:
        y=rr[r-1]*bb[b-1]+dfs(r-1,g,b-1,rr,gg,bb)
    if b!=0 and g!=0:
        z=bb[b-1]*gg[g-1]+dfs(r,g-1,b-1,rr,gg,bb)
    dp[r][g][b]=max(x,y,z)
    return max(x,y,z)

r,g,b=map(int,input().split())
rr=list(map(int,input().split()))
gg=list(map(int,input().split()))
bb=list(map(int,input().split()))
rr.sort()
gg.sort()
bb.sort()
dp=[[[-1]*(b+1) for i in range(g+1)] for j in range(r+1)]

print(dfs(r,g,b,rr,gg,bb))





