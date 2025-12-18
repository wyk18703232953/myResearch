R,G,B=map(int,input().split())
r=list(map(int,input().split()))
g=list(map(int,input().split()))
b=list(map(int,input().split()))
r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)
dp=[[[-1]*(B+1) for i in range(G+1)] for j in range(R+1)]
def calc(nr,ng,nb):
  if dp[nr][ng][nb]!=-1:
    return dp[nr][ng][nb]
  res=0
  if nr<R and ng<G:
    res=max(res,calc(nr+1,ng+1,nb)+r[nr]*g[ng])
  if nr<R and nb<B:
    res=max(res,calc(nr+1,ng,nb+1)+r[nr]*b[nb])
  if ng<G and nb<B:
    res=max(res,calc(nr,ng+1,nb+1)+g[ng]*b[nb])
  dp[nr][ng][nb]=res
  return res
print(calc(0,0,0))