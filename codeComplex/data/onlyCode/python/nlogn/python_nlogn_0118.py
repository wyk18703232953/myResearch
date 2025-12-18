n=int(input())
arr=list(map(int,input().split()))
arr2=sorted(arr)
count=0
a=0
for i in range(n):
   if arr[i]!=arr2[i]:
        count+=1
        k=arr[i]
        arr[i]=arr2[i]
        z=arr.index(arr2[i])
        arr[z]=k

   if count>2:
        a=1
        break
if a==0:
    print("YES")
else:
    print("NO")