n=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=0
mark=0
for i in range(len(arr)-2):
	if(arr[i]==arr[i+1]==arr[i+2]):
		print('cslnb')
		exit(0)
	elif(arr[i+1]==arr[i+2] and arr[i]+1==arr[i+1]):
		print('cslnb')
		exit(0)

countcopy=0
for i in range(len(arr)-1):
	if(arr[i]==arr[i+1] and arr[i]==0):
		print('cslnb')
		exit(0)
	if(arr[i]==arr[i+1]):
		countcopy+=1
if(countcopy>1):
	print('cslnb')
	exit(0)

for i in range(len(arr)):
	if(arr[i]>=mark):
		ans+=(arr[i]-mark)
		mark+=1

#print(ans)
if(ans%2==0):
	print('cslnb')
else:
	print('sjfnb')

