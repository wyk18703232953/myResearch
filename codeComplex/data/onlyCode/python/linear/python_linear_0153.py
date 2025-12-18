n, p=map(int, input().split())
arr=list(map(int, input().split()))
su=0
for i in range(n):
	su+=arr[i]
maxi, f=0, 0
for i in range(n-1):
	f+=arr[i]
	maxi=max(maxi, f%p+(su-f)%p)
print(maxi)