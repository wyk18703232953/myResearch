
n,s=map(int,input().split())

def ver(i):
	t=str(i)
	ans=0
	for j in t:
		ans+=int(j)
	return(ans)
l=len(str(s))
if n<s:
	print(0)
	exit()
if s+10*(l**2+1)<=n:
	ans=n-s+1-10*(l**2+1)
	for i in range(s,s+10*(l**2+1)):
		if s+ver(i)<=i:ans+=1
else:
	ans=0
	for i in range(s,n+1):
		if s+ver(i)<=i:ans+=1
print(ans)