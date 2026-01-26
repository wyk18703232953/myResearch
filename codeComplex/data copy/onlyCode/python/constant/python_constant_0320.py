l=list(map(int,input().split()))
ans=0
for i in range(14):
	a=[]
	m=0
	a.extend(l)
	c=a[i]//14
	d=a[i]%14
	a[i]=0
	j=1
	while(j<=d):
		k=(i+j)%14
		a[k]+=1
		j+=1
	for j in range(14):
		a[j]+=c
		if a[j]%2==0:
			m+=a[j]
	ans=max(ans, m)
print(ans)