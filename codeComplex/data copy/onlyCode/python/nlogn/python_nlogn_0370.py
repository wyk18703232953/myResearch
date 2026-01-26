n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
slow,fast=0,0
while fast<n:
    if a[slow]==a[fast]:
        fast+=1
    elif abs(a[slow]-a[fast])<=k:
        a[slow]=0
        slow+=1
    else:
        slow+=1
ans=0
for i in a:
    if i!=0:
        ans+=1
print(ans)