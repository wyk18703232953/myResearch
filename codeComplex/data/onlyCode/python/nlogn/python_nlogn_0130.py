n,m,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
arr=arr+[k]
ans=0
s=0
while ans<n+1:
    s+=arr[-ans-1]
    if s>=m:
        break
    ans+=1
    s-=1
if s>=m:
    print(ans)
else:
    print("-1")
