def maxXORInRange(L, R):
	LXR = L ^ R
	msbPos = 0
	while LXR:
		msbPos += 1
		LXR >>= 1
	maxXOR = (1 << msbPos) - 1
	return maxXOR

def main(n):
	l = n
	r = 2 * n
	result = maxXORInRange(l, r)
	# print(result)
	pass
if __name__ == "__main__":
	main(10)