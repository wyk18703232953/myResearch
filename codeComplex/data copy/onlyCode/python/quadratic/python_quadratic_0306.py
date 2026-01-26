def mp():return map(int,input().split())
def it():return int(input())

n,k=mp()
l=list(mp())
ans=0
for i in range(n):
	avg,count=0,0
	for j in range(i,n):
		count+=l[j]
		if j-i+1>=k:
			avg=count/(j-i+1)
		ans=max(avg,ans)
print(ans)
