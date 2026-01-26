def power(x,y,p):
    res=1
    x=x%p
    if(x==0):
        return 0
    while(y>0):
        if(y&1):
            res=(res*x)%p
        y=y>>1
        x=(x*x)%p
    return res

x,k=map(int,input().split())
p=1000000007
if(x==0):
    print("0")
else:
    t=(((power(2,k,p))*((2*x-1)%p))%p+1)%p
    # t=(((power(2,k,p))*(((2*(x%p))%p-1)%p))%p+1)%p
    #t=((power(2,k,p)%p)*(((2*(x%p))%p-1)%p)%1000000007+1)%p
    print(t)