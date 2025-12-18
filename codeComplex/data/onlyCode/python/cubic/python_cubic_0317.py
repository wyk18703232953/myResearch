def rec(r,g,b):
    if(dp[r][g][b]!=-1):
        return dp[r][g][b]
    ans=0
    if r<R and g<G:
        ans=max(ans, red[r]*green[g]+rec(r+1, g+1, b))
    if r<R and b<B:
        ans=max(ans, red[r]*blue[b]+rec(r+1, g, b+1))
    if b<B and g<G:
        ans=max(ans, blue[b]*green[g]+rec(r, g+1, b+1))
    dp[r][g][b]=ans
    return ans
R,G,B=map(int,input().split())
red=sorted(list(map(int, input().split())), reverse=True)
green=sorted(list(map(int, input().split())), reverse=True)
blue=sorted(list(map(int, input().split())), reverse=True)
dp=[[[-1]*(B+1) for _ in range(G+1)] for _ in range(R+1)]
print(rec(0,0,0))