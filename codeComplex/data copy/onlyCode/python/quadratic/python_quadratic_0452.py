n=int(raw_input())
arr=list(map(int,raw_input().split()))
dict1={}
arr1=[0]*n
for i in range(n):
	arr1[arr[i]-1]=i
for i in range(n):
	dict1[i+1]=[]
for i in range(n):
	for j in range(i-arr[i],-1,-arr[i]):
		if(arr[j]>arr[i]):
			dict1[arr[i]].append(arr[j])
	for j in range(i+arr[i],n,arr[i]):
		if(arr[j]>arr[i]):
			dict1[arr[i]].append(arr[j])
strarr=['.']*n
#print(dict1)
for i in range(n-1,-1,-1):
	if(len(dict1[arr[arr1[i]]])==0):
		strarr[arr1[i]]='B'
	else:
		if(len(dict1[arr[arr1[i]]])==1 and len(dict1[dict1[arr[arr1[i]]][0]])==0):
			strarr[arr1[i]]='A'
		else:
			flag=0
			for j in dict1[arr[arr1[i]]]:
				#print(j)
				#print(arr1[j-1])
				if(strarr[arr1[j-1]]=='B'):
					flag=1
					break
			if(flag==1):
				strarr[arr1[i]]='A'
			else:
				strarr[arr1[i]]='B'
	#print(*strarr)
print("".join(x for x in strarr))

