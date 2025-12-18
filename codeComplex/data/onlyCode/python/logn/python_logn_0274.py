x,n=map(int,input().split())
mod=10**9+7
if x>0: ans=pow(2,n+1,mod)*x-pow(2,n,mod)+1
else: ans=0
print(ans%mod)