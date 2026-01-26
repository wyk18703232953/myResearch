n=int(input())
l=list(map(int,input().split()))
l.sort()
vis=[0]*n
ans=0
for i in range(n):
    if(vis[i]==0):
        ans+=1
        x=l[i]
        for j in range(n):
            if l[j]%x==0:
                vis[j]=1
print(ans)