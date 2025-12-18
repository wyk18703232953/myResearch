def maxXORInRange(L, R):
    LXR = L ^ R

    
    msbPos = 0
    while (LXR):
        msbPos += 1
        LXR >>= 1

    maxXOR, two = 0, 1

    while (msbPos):
        maxXOR += two
        two <<= 1
        msbPos -= 1

    return maxXOR



L, R = map(int, input().split())
print(maxXORInRange(L, R))

 				       	  	     	 		    		