n=int(input())
l=list(map(int,input().split()))
l.sort()
for x in range(1,n):
	if l[x]>l[0]:
		print(l[x])
		break
else:
	print('NO')