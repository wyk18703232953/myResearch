from math import pow
def modularExponentiation(x,n,M):
    
    if n==0:
        return 1
    elif n%2 == 0: 
        return modularExponentiation((x*x)%M,n//2,M)
    else:              
        return (x%M*modularExponentiation((x*x)%M,(n-1)//2,M)%M)%M


c=10**9+7
n,k=map(int,input().split())
a=(n%c*(modularExponentiation(2,k+1,c))%c)%c
b=(modularExponentiation(2,k,c)%c-1%c+c)%c
if n==0:
    print("0")
else:
    print((a%c-b%c+c)%c)