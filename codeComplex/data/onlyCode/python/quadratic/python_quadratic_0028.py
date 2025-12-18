n=int(input())
f=[input().strip()=="f" for ii in range(n)]
mod=10**9+7
def summ(a,b):
 return (a+b)%mod
dp=[1]
for ii in range(1,n):
 pf=f[ii-1]
 if pf:
  dp.insert(0,0)
 else:
  for jj in reversed(range(1,len(dp))):
   dp[jj-1]=summ(dp[jj-1],dp[jj])
ans=0
for vv in dp:
 ans=summ(ans,vv)
print(ans)
	 		       		 	 	 	 					  		