a,b,c,n=list(map(int,input().split()))
p=(a+b-c)
f=n-p
if p>=n or c>a or c>b:
	print("-1")
else:
	print(f)