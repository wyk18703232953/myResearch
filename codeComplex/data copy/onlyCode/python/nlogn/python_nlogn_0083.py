n,k=map(int,input().split())
l,c=[],0
for _ in range(n):
	l.append(list(map(int,input().split())))
l.sort(reverse=True)
a,x,y=l[k-1][0],k-1,k-1
for i in range(k-2,-1,-1):
	if l[i][0]==a:
		x=i
	else:
		break
for i in range(k,n):
	if l[i][0]==a:
		y=i
	else:
		break
d=k-1-x
d=y-d
for i in range(y,x-1,-1):
	if l[i]==l[d]:
		c+=1
print(c)