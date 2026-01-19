n,l,r,x=map(int,input().split())
c=list(map(int,input().split()))
ans=0
for i in range(0,2**n):
    v=[]
    for j in range(n):
        if i & (1<<j):v.append(c[j])
    if sum(v)>=l and sum(v)<=r and (max(v)-min(v)>=x): ans+=1
print(ans)