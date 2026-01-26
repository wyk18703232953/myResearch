n, s = map(int, input().split())
l = [0 for i in range(n)]
for i in range(n-1):
	a, b = map(int, input().split())
	l[a-1]+=1
	l[b-1]+=1
count = 0
for i in range(n):
	if(l[i]==1):
		count+=1
print((s/count)*2)