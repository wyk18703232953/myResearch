n=int(input())
l=[int(x) for x in input().split()]
ans=0;
while len(l)>0:
	a=l[0]
	l=l[1:]
	ans+=l.index(a)
	l.remove(a)
print(ans)