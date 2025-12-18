MOD=1000000007

x,k=map(int,raw_input().split())

if x>0:
	ans=(pow(2,k+1,MOD)*x)%MOD
	ans=(ans-pow(2,k,MOD))%MOD
	ans=(ans+1)%MOD
else:
	ans=0

print(ans)