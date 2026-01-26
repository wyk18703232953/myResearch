n,k=input().split()
n=int(n)
k=int(k)

m = 1000000007
# z = (2**k)%m
z = pow(2,k,m)

ans = (((2*z)*(n%m))%m - (z-1))%m
if n==0:
	print(0)
else:
	print(ans)