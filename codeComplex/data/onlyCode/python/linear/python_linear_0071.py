n,s=map(int,input().split())
arr=[]
for i in range(n):
    arr.append([])
    arr[i]=[int(i) for i in input().split()]
arr=sorted(arr,reverse=True,key=lambda x:x[0])
ans,c=0,0
for i in range(n):
    if i!=0:
       c=arr[i-1][0]
    if i==0:
       ans=ans+s-arr[i][0]
    else:
       ans=ans+c-arr[i][0]
    if arr[i][1]>=ans:
        ans=ans+(arr[i][1]-ans)
ans=ans+arr[n-1][0]
print(ans)
    