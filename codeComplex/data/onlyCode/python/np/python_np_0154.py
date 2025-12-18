from itertools import combinations
n,l,r,x=map(int,input().split())
arr=list(map(int,input().split()))
ans=0
for i in range(2,n+1):
	brr=list(combinations(arr,i))
	for j in brr:
		s=sum(j)
		if l<=s<=r and max(j)-min(j)>=x:
			ans+=1
print(ans)
