n,k=map(int,input().split())
arr=list(map(int,input().split()))
d={}
for i in arr:
	if i in d:
		d[i]+=1
	else:
		d[i]=1
flag=True
for i in range(100,0,-1):
	t2=0
	for j in d.values():
		t2+=j//i
	if(t2>=n):
		print(i)
		flag=False
		break
if(flag):
	print(0)