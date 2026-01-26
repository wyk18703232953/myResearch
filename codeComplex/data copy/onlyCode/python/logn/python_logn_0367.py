X, K = map(int, input().split())
mod = 1000000007
res = X*pow(2, K+1, mod)-pow(2, K, mod)+1;
while(res < 0):
   res += mod
if(X == 0):
   print(0)
else:
   print(res%mod)