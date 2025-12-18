x,k=map(int,input().split())
print(0 if x==0 else (x*pow(2,k+1,10**9+7)-pow(2,k,10**9+7)+1)%(10**9+7))