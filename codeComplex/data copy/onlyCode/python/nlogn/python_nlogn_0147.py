n,k=map(int,input().split())
a=list(map(int,input().split()))
d={}
for i in range(n):
    d[a[i]]=1
a.sort(reverse=True)
ans=0
for i in range(n):
    if d[a[i]]>0:
        if a[i]%k==0:
            x=a[i]//k
            if x in d:
                d[x]-=1
        ans+=1
print(ans)