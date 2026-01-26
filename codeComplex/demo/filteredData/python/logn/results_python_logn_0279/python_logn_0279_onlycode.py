import sys
def power(x, y, p) :
    res = 1     # Initialize result
 
    # Update x if it is more
    # than or equal to p
    x = x % p 
 
    while (y > 0) :
         
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
         
    return res
mod=(10**9)+7
r,k=map(int,input().split())
if r==0:
    print(0)
    sys.exit()
print((((((power(2,k+1,mod)%mod)*(r%mod))%mod)-power(2,k,mod)+1))%mod)
