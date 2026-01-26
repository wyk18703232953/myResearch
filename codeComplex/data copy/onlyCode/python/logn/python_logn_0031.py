l, r=map(int, input().split())
def cntbit(n):
  ans=0
  while(n):
    ans+=1
    n//=2
  return ans
c1=cntbit(l)
c2=cntbit(r)
if(c2>c1):
  print(2**c2-1)
else:
  x=l^r
  c=cntbit(x)
  print(2**c-1)