mod=1000000007 
import math
def powm(a, n, m):
    if a == 1 or n == 0:
        return 1
    if n % 2 == 0:
        s = powm(a, n // 2, m)
        return s * s % m
    else:
        return a * powm(a, n - 1, m) % m
def modInverse(b,m): 
    g = math.gcd(b, m)  
    if (g != 1): 
        # print("Inverse doesn't exist")  
        return -1
    else:  
        # If b and m are relatively prime,  
        # then modulo inverse is b^(m-2) mode m  
        return pow(b, m - 2, m) 
  
  
# Function to compute a/b under modulo m  
def modDivide(a,b,m): 
    a = a % m 
    inv = modInverse(b,m)
    a=(a*inv)%m
    return a
n,k=map(int,input().split())
ans=(powm(4,k,mod)*n)%mod
r=powm(2,k,mod)
r=(powm(r,2,mod)-r)%mod
w=modDivide(r,2,mod)    
ans=(ans-w)
er=powm(2,k,mod)
ans=modDivide(ans,er,mod)
ans=(ans*2)%mod
if n==0:
    ans=0
print(ans)