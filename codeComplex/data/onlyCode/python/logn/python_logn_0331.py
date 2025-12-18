f1, f2 = map(int,input().split(" "))
if f1==0:
  print(0)
else:
  print((pow(2,f2,1000000007)*(2*f1-1)+1)%1000000007)