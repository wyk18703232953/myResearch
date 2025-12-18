t=int(input())
for _ in range(t):
	n,k=list(map(int,input().split()))
	if n>=32:
		print("YES "+str(n-1))
	else:
		ans=-1
		for i in range(1,n+1):
			p=(4**i)-(2**(i+1))+1
			p*=(((4**(n-i))-1)//3)
			g=(((4**i)-1)//3)
			p+=(((4**i)-1)//3)
			g=(((4**i)-1)//3)-(((4**(i-1))-1)//3)
			if g<=k and p>=k:
				ans=n-i
				break
		if ans!=-1:
			print("YES "+str(ans))
		else:
			print("NO")