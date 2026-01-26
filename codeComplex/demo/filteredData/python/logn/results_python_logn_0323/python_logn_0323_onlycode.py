x, k = map(int,input().split())
if x==0:
  print(0)
else:
  print((pow(2,k,1000000007)*(2*x-1)+1)%1000000007)