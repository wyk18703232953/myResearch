n,k=map(int,input().split())
arr=list(map(int,input().split()))
par=[i for i in range(260)]
path=[-1 for i in range(260)]
for i in range(n):
    j=arr[i]
    if path[j] >=0:
        par[j] =par[path[j]]
        continue
    jump=1
    while j>0 and path[j] ==-1 and jump <k:
        path[j] =arr[i]
        j-=1
        jump +=1
    if arr[i] -par[j] +1 <=k:
            par[arr[i]] =par[j]
            path[j] =arr[i]
    else:
        par[arr[i]] =par[j+1]
for i in range(n):
    print(par[arr[i]],end=' ')
print()