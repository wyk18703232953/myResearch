n=int(input())
l=list(map(int,input().split()))
l.sort()
v=[False for i in range(n)]
ans=0
i=0
while i<n:
	if v[i]==False:
		ans+=1
		for j in range(i+1,n):
			if l[j]%l[i]==0:
				v[j]=True
	i+=1
print(ans)