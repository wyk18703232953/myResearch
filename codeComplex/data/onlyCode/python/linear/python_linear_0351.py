n,m=map(int,input().split())
arr=[]
for i in range(m):
  arr.append(list(map(int,input().split())))
k=0;ans=str()
for i in range(n):
  ans+=str(k^1)
  k=k^1
print(ans)
