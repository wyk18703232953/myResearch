arr1=str(input())
arr2=str(input())
arr1=arr1.encode()
arr2=arr2.encode()
arr1=bytearray(arr1)
arr2=bytearray(arr2)
n, tot=len(arr1), 0
for i in range(n-1):
	if arr1[i]==48 and arr1[i+1]==48 and arr2[i]==48:
		tot+=1
		arr1[i]=49
		arr1[i+1]=49
		arr2[i]=49
	elif arr1[i]==48 and arr2[i]==48 and arr2[i+1]==48:
		tot+=1
		arr1[i]=49
		arr2[i]=49
		arr2[i+1]=49
	elif arr2[i]==48 and arr2[i+1]==48 and arr1[i+1]==48:
		tot+=1
		arr2[i]=49
		arr2[i+1]=49
		arr1[i+1]=49
	elif arr1[i]==48 and arr1[i+1]==48 and arr2[i+1]==48:
		tot+=1
		arr1[i]=49
		arr1[i+1]=49
		arr2[i+1]=49
print(tot)