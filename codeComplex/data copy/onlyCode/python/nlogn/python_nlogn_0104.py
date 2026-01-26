n=int(input())
l=[int(x) for x in input().split()]
if l==sorted(l):
	print("Yes")
else:
	cnt=0;
	g=sorted(l)
	for i in range(len(l)):
		if l[i]!=g[i]:
			cnt+=1
	if cnt<=2:
		print("Yes")
	else:
		print("No")