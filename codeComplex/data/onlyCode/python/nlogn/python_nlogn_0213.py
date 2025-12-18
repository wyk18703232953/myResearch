n,m=map(int,input().split())
a=list(map(int,input().split()))
k=0
ans=-1
for i in range(n-1):
    while k<n-1 and a[k+1] - a[i]<=m:
        k+=1
    if i<k-1:
        ans=max(ans,(a[k]-a[i+1]) / (a[k]-a[i]))
print(ans)