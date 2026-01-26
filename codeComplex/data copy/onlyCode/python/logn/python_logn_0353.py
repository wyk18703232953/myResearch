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
            #res = (res * x)
 
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
        #x = (x * x)
         
    return res
p = 1000000007
x = [int(i) for i in raw_input().split()]
y = power(2,x[1],p)
#z = power(2,x[1],p)
#z = power(power(2,x[1],p),p-2,p)
if(x[0]>0):
    ans = 2 * y * x[0]%p - (y - 1)%p
else:
    ans = 0
print(ans%p)