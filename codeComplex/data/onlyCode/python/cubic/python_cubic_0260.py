R,G,B=map(int,input().split())
r=list(map(int,input().split()))
g=list(map(int,input().split()))
b=list(map(int,input().split())) 
r.sort(reverse=True) 
g.sort(reverse=True) 
b.sort(reverse=True) 
#print(r,g,b)
dp=[[[-1 for i in range(205)] for j in range(205)] for k in range(205)]
def recurser(x,y,z):
    if (x>=R and y>=G) or (y>=G and z>=B) or (z>=B and x>=R):
        return 0 
    if dp[x][y][z]!=-1:
        return dp[x][y][z] 
    maxi=0 
    if x<R and y<G:
        maxi=max(maxi,r[x]*g[y]+recurser(x+1,y+1,z)) 
    if y<G and z<B:
        maxi=max(maxi,g[y]*b[z]+recurser(x,y+1,z+1)) 
    if z<B and x<R:
        maxi=max(maxi,r[x]*b[z]+recurser(x+1,y,z+1))
    dp[x][y][z]=maxi
    return maxi 
print(recurser(0,0,0)) 