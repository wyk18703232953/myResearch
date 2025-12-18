a,b=map(int,input().split())
ans=0
while a and b:
  ans+=a//b
  a,b=b,a%b
print(ans)