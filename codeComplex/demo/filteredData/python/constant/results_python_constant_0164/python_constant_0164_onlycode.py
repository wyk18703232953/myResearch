l,r=map(int,input().split())
j=r-l+1

if j==3:
	if l%2==0:
		print(l,l+1,l+2)
	else:
		print(-1)
elif j>3:
	if l%2==0:print(l,l+1,l+2)
	else:print(l+1,l+2,l+3)
else:print(-1)