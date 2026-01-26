#from collections import defaultdict
#DPL=[[[-1]*(B+1) for i in range(G+1)] for j in range(R+1)]
ri,gi,bi=map(int,input().split())
rr=sorted(list(map(int,input().split())))
gr=sorted(list(map(int,input().split())))
br=sorted(list(map(int,input().split())))
dp=[[[-1]*(bi+1) for i in range(gi+1)] for j in range(ri+1)]
def area(r,g,b):
	if dp[r+1][g+1][b+1]!=-1:
		return dp[r+1][g+1][b+1]
	ans=0
	if r>=0 and g>=0:
		ans=max(ans,rr[r]*gr[g]+area(r-1,g-1,b))
	if r>=0 and b>=0:
		ans=max(ans,rr[r]*br[b]+area(r-1,g,b-1))	
	if b>=0 and g>=0:
		ans=max(ans,br[b]*gr[g]+area(r,g-1,b-1))	
	dp[r+1][g+1][b+1]=ans
	return ans
print(area(ri-1,gi-1,bi-1))