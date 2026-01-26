x,k=map(int,input().split())
if x==0:print("0")
else:
    ans=(x*pow(2,k+1,10**9+7)-pow(2,k,10**9+7)+1)%(10**9+7)
    print(ans)
