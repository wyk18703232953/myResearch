n,k=list(map(int,input().split()))

arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
ans=0

new_arr=[0]*n

for i in range(n):
    if arr2[i]==0:
        new_arr[i]=arr1[i]
    else:
        ans+=arr1[i]

total=sum(new_arr[:k])
mx=total

j=0
for i in range(k,n):
    total-=new_arr[j]
    total+=new_arr[i]
    mx=max(mx,total)
    j+=1
        
    
print(mx+ans)
    