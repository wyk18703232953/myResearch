n,k=map(int,input().split())
a=list(map(int,input().split()))
t=list(map(int,input().split()))
ans=0
m=0
for i in range(n):
    if t[i]:
        ans+=a[i]
        a[i]=0
cf=[0]*(n+1)
for i in range(1,n+1):
    cf[i]=cf[i-1]+a[i-1]
for i in range(n-k+1):
    m=max(m,cf[i+k]-cf[i])
print(ans+m)