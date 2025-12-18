a,b,c,n= [int(c) for c in input().split()]
u=a+b-c
if a<c or b<c:
	print(-1)
else:
	if n-u>=1:
		print(n-u)
	else:
		print(-1)
