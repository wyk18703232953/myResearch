a,k=map(int,input().split())
p=[]
for n in range(2,a+1):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			break
	else:
		p.append(n)
c=0
for i in range(0,len(p)-1):
	n=p[i]+p[i+1]+1
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			break
	else:
		if n<=a:
			c+=1
if c>=k:
	print("YES")
else:
	print("NO")
