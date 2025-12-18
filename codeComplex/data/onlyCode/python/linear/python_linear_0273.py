n,m,a,b=[int(x) for x in input().split()]
if n>m:
	if n%m==0:
		print(0)
	else:
		t1=n%m
		print(min(t1*b,(m-t1)*a))
elif n==m:
	print(0)
else:
	print(min(n*b,(m-n)*a))