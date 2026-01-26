# L = 8    R = 20
# L ^ R = (01000) ^ (10100) = (11100)
# Now as L ^ R is of form (1xxxx) we
# can get maximum XOR as (11111) by 
# choosing A and B as 15 and 16 (01111 
# and 10000)

# Examples 2:
# L = 16     R = 20
# L ^ R = (10000) ^ (10100) = (00100)
# Now as L ^ R is of form (1xx) we can 
# get maximum xor as (111) by choosing  
# A and B as 19 and 20 (10011 and 10100)

def maxXORInRange(L, R):
  
    # get xor of limits
    LXR = L ^ R
  
    # loop to get msb position of L^R
    msbPos = 0
    while(LXR):
      
        msbPos += 1
        LXR >>= 1
      
  
    # construct result by adding 1,
    # msbPos times
    maxXOR, two = 0, 1
      
    while (msbPos):
      
        maxXOR += two
        two <<= 1
        msbPos -= 1
  
    return maxXOR
  
L,R = map(int, input().split())
print(maxXORInRange(L, R))