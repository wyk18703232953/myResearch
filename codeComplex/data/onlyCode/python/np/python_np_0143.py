ii=lambda:int(input())
kk=lambda:map(int, input().split())
ll=lambda:list(kk())

n,k=kk()
pre,post = [],[]
k-=1
v = 1
for i in range(n-2,-1,-1):
	if k&(2**i):
		post.append(v)
	else:
		pre.append(v)
	v+=1
print(*pre,n,*reversed(post))