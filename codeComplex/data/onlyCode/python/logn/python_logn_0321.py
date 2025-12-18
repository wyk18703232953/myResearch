q=input().split()

x=int(q[0])
k=int(q[1])

def po(a,p,m):
 if p==0:
  return 1
 x=po(a,p//2,m)%m
 x=(x%m*x%m)%m
 if p%2==1:
  x=(x%m*a%m)%m

 return int(x)

m=1000000007
if x==0:
 print(0)
else:
 print(((po(2,k+1,m)%m*x%m)%m-(po(2,k,m)%m-1)%m)%m)