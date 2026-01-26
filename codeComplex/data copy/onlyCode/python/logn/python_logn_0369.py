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
    
x,k = map(int,input().split())
if x==0:
    print(0)
else:
    ans = power(2,k,1000000007)
    ans = ans * ((2*x)-1)
    ans = ans+1
    ans=ans%1000000007
    print(ans)