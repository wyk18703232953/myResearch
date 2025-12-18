MOD=1000000007

def powr(n,N):
    temp=1
    while(N>0):
        if(N%2!=0):
            temp=(temp*n)%MOD
        n=(n*n)%MOD
        N=N//2
    return (temp%MOD)
 
"""def powr(n,N):
    if(N==1):
        ans=n
        return ans
    else:
        ans=powr(n,N//2)
        if(N%2==0):
            return ((ans*ans)%MOD)
        else:
            return ((((ans*ans)%MOD)*n)%MOD)"""
 
def MODI(a,b):
    ans=(powr(a,b)%MOD)
    return ans
 


x,k=map(int,input().split())
if(x==0):
    print(0)
else:
    t1=powr(2,k+1)%MOD
    t1=(t1*x)%MOD
    t2=powr(2,k)%MOD
    t2=(t2-1)%MOD
    ans=(t1-t2)%MOD
    print(ans)
