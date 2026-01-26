def maxXORInRange(L, R):
	LXR = L ^ R
	msbPos = 0
	while(LXR):
		msbPos += 1
		LXR >>= 1

	maxXOR = (1<<msbPos)-1 
	return maxXOR

l,r=map(int,input().split())
print(maxXORInRange(l, r))
