test=int(input())
while test:
	test=test-1
	n,k = input().split()
	n=int(n)
	k=int(k)
	s=0
	curr=1
	ct=0
	while s<k:
		s=s+curr
		curr=4*curr
		ct=ct+1
	if n>=35:
		print("YES",n-1)
		continue
	val=[]
	val.append(0)
	for i in range(1,n):
		val.append(1+4*val[i-1])
	s=0
	t=2
	rem=0
	while n>0:
		s=s+t-1
		t*=2
		p=3
		rem=rem+(t-3)*(val[n-1])
		rem=int(rem)
		if rem+s>=k and s<=k:
			print("YES",n-1)
			n=-2
			break
		n=n-1
	if n != -2:
		print("NO")