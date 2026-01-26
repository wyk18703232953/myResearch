x,k=map(int,input().split())
if x==0:
  print(0)
else:
    u=(pow(2,k,1000000007)*(2*x-1)+1)%1000000007
    print(int(u))
