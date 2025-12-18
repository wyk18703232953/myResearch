n=int(input())
arr=list(map(int,input().split()));ans=0
while len(arr)!=0:
 e=arr.pop(0)
 ans+=arr.index(e)
 arr.remove(e)
print(ans)
 

  
