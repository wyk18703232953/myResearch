MOD=1000000007
def pow2(n):
    if n==0:
        return 1
    t=pow2(n//2)%MOD
    m=(t*t)%MOD
    if n%2==1:
        m=(m*2)%MOD
    return m
x,k=map(int,input().split())
if x==0:
    print(0)
    exit()
t=pow2(k)*(2*x-1)%MOD
print((t+1)%MOD)
