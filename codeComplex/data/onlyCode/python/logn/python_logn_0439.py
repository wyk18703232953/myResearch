test=int(input())
while test:
	test=test-1
	n,k = input().split()
	n=int(n)
	k=int(k)
	if n==2 and k==3:
		print("NO")
		continue
	if n>=32:
		print("YES",n-1)
		continue
	val=[]
	val.append(0)
	for i in range(1,n+1):
		val.append(4*val[i-1]+1)
	if val[n]<k:
		print("NO")
		continue
	s=0
	t=2
	rem=0
	flag=0
	while s+t-1<=k and n>0:
		s=s+t-1
		t*=2
		n=n-1
	print("YES",n)