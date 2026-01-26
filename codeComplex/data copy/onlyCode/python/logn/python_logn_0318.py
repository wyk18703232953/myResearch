x,k=map(int,input().split())
mod=1000000007
if x==0: print(0)
else:
    print((x*pow(2,(k+1),mod)-pow(2,k,mod)+1)%mod)

