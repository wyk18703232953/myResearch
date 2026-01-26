# cook your dish here
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
    
d,n=map(int,input().split())
ans =power(2,n+1,1000000007);
ans1=power(2,n,1000000007);
if(d==0):
    print(0)
else:
    print(((ans*(d%1000000007))%1000000007 - ans1 +1)%1000000007)