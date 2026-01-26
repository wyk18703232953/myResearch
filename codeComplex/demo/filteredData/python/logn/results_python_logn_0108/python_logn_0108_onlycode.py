l,r=[int(i) for i in input().split()]
LXR=l^r
msbPos = 0
while(LXR):
	msbPos+=1
	LXR>>=1
maxXOR, two = 0, 1
while (msbPos): 
	maxXOR += two 
	two <<= 1
	msbPos -= 1
print(maxXOR)
         	 	 	  				 	   	 	