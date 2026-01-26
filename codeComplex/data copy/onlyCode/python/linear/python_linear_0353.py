n,m=map(int,input().split())
c=0;ans=str()
for i in range(n):
  ans+=str(c^1)
  c=c^1
print(ans)
