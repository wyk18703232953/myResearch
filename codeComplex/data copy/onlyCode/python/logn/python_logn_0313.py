x,k = map(int,input().split())
if(x==0):
    print(0)
    exit(0)
m = 10**9+7
p = pow(2,k+1,m)
q = pow(2,k,m)
a = (x*p-q+1)%m
print(a)
