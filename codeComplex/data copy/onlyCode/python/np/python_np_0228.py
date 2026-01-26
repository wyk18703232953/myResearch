def combinations(arr,n):
    if(n==0):
        return([[]])
    l=[]
    for i in range(len(arr)):
        m=arr[i]
        rem=arr[i+1:]
        for j in combinations(rem,n-1):
            l.append([m]+j)
    return l

        
def solve(arr,n,l,r,x):
    subset=[]
    for i in range(2,n+1):
        for j in combinations(arr,i):
            if(sum(j)>=l and sum(j)<=r):
                subset.append(j)
    count=0
    for i in subset:
        mn=min(i)
        mx=max(i)
        if(mx-mn>=x):
            count+=1
                
    return(count)
            
n,l,r,x=map(int,input().split())
arr=list(map(int,input().split()))
print(solve(arr,n,l,r,x))
