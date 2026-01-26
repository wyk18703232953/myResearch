import sys
import math
input = sys.stdin.readline

n,q=map(int,input().split())

arr=list(map(int,input().split()))
for i in range(n):
	arr.append(0)
maxx=0

ind=arr.index(max(arr))
ans=[]
ptr1=0
ptr2=n
for i in range(ind):
	ans.append([arr[ptr1],arr[ptr1+1]])
	if arr[ptr1]>arr[ptr1+1]:
		arr[ptr2]=arr[ptr1+1]
		arr[ptr1+1]=arr[ptr1]
	else:
		arr[ptr2]=arr[ptr1]
	ptr1+=1
	ptr2+=1
#print(arr)
for i in range(q):
	m=int(input())

	if m<=ind:
		print(*ans[m-1])
	else:
		m-=ind
		m=m%(n-1)
		if m==0:
			m+=n-1
		print(arr[ind],arr[ind+m])