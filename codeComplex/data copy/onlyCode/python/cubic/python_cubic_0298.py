import sys
sys.setrecursionlimit(200000)
input=sys.stdin.readline
 
def solve(r,g,b,R,G,B):
    if (r==0 and g==0) and (r==0 and b==0) and (g==0 and b==0):
        return 0
    if z[r][g][b]!=-1:
        return z[r][g][b]
    d,e,f=0,0,0
    if r!=0 and g!=0:
        d=R[r-1]*G[g-1]+solve(r-1,g-1,b,R,G,B)
    if r!=0 and b!=0:
        e=R[r-1]*B[b-1]+solve(r-1,g,b-1,R,G,B)
    if b!=0 and g!=0:
        f=B[b-1]*G[g-1]+solve(r,g-1,b-1,R,G,B)
    z[r][g][b]=max(d,e,f)
    return z[r][g][b]
 
r,g,b=map(int,input().rstrip().split())
R=sorted(map(int,input().rstrip().split()))
G=sorted(map(int,input().rstrip().split()))
B=sorted(map(int,input().rstrip().split()))
z=[[[ -1 for i in range(b+1)] for j in range(g+1)] for k in range(r+1)]
print(solve(r,g,b,R,G,B))