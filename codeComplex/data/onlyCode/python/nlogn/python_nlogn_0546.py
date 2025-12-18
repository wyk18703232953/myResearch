n=int(raw_input())

l=list(map(int,raw_input().split()))

index = []
ans=[]
for i in range(n):
	index.append(i+1)
	ans.append(0)

l1,index1 = zip(*sorted(zip(l, index),reverse=True))
#print('l1',l1)
#print('index1',index1)
for i in range(n):
	#print("i",i)
	k=1
	flag=False
	while (index1[i]-k*l1[i])>0:
		if l[index1[i]-k*l1[i]-1]>l[index1[i]-1]:
			if ans[index1[i]-k*l1[i]-1]=="B":
				ans[index1[i]-1]="A"
				flag=True
				break
		k+=1

	k=1
	if flag==False:
		while (index1[i]+k*l1[i])<=n:
			if l[index1[i]+k*l1[i]-1]>l[index1[i]-1]:
				if ans[index1[i]+k*l1[i]-1]=="B":
					ans[index1[i]-1]="A"
					flag=True
					break
			k+=1


	if flag==False:
		ans[index1[i]-1]="B"

print(''.join(ans))


