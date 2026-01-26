n,s = [int(x) for x in input().split()]
v=[ [] ]
for i in range(n):
	v.append([])
	
for i in range(n-1):
	a, b =[int(x) for x in input().split()]
	v[a].append(b)
	v[b].append(a)

ans =0
for i in range(1,n+1):
	if len(v[i])==1:
		ans+=1
	
print(2*s/ans)
