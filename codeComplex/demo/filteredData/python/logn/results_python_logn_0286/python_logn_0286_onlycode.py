M=10**9+7
def pw(x,y):
	r=1
	x=x%M
	while y:
		if y&1:
			r=(r*x)%M
		y=y>>1
		x=(x*x)%M
	return r
x,k=map(int,input().split())
ans=pw(2,k+1)*x-pw(2,k)+1+M
if x==0:
	ans=0
print(ans%M)
