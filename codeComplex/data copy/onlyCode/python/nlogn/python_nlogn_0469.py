n,m=map(int,input().split())
lst=list(map(int,input().split()))
arr=lst.copy()
arr.sort(reverse=True)
vis=[0]*n
summ=0
for i in range(m):
    temp=arr[i]
    summ+=temp
    for j in range(n):
        if vis[j]==0 and lst[j]==temp:
            vis[j]=1
            
            break

print(summ)
cnt=0
ans=[]
for i in range(n):
    if vis[i]==1:
        ans.append(cnt+1)
        cnt=0
    else:
        cnt+=1
ans[-1]+=cnt
print(*ans)