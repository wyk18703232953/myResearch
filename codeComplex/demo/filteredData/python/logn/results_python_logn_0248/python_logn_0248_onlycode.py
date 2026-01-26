x,k=map(int,input().split())
if x==0:
  print(0)
  exit()
mod=10**9+7
p=pow(2,k,mod)
print((2*p*x-p+1)%mod)