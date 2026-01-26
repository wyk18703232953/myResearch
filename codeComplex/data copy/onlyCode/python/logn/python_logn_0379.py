import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def power(a,b,z):
    if b==0:
        return 1
    temp=power(a,b//2,z)
    if b%2==0:
        return (temp*temp)%z
    return (a*temp*temp)%z
x,k=list(map(int,input().split()))
if x==0:
    print(0)
else:
    z=(10**9)+7
    n=(power(2,k+1,z)*x)%z
    m=power(2,k,z)
    print((n-m+1)%z)