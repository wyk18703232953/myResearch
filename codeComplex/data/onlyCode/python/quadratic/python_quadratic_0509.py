n,m=map(int,raw_input().split())
arr=[]
arr1=[]
for i in range(n):
	arr2=str(raw_input())
	arr.append(arr2)
	x1=[0]*m
	arr1.append(x1)
for i in range(n):
	for j in range(m):
		if(arr[i][j]=='#' and i<n-2 and j<m-2):
			if(arr[i][j+1]=='#' and arr[i][j+2]=='#' and arr[i+1][j]=='#' and arr[i+2][j]=='#' and arr[i+2][j+1]=='#' and arr[i+2][j+2]=='#' and arr[i+1][j+2]=='#'):
				arr1[i][j]=1
				arr1[i+1][j]=1
				arr1[i+2][j]=1
				arr1[i+2][j+1]=1
				arr1[i+2][j+2]=1
				arr1[i+1][j+2]=1
				arr1[i][j+1]=1
				arr1[i][j+2]=1
flag=0
#print(arr1)
for i in range(n):
	for j in range(m):
		if(arr[i][j]=="#" and arr1[i][j]==0):
			flag=1
			break
	if(flag==1):
		break
if(flag==1):
	print("NO")
else:
	print("YES")