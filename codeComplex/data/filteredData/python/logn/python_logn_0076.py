def maxXORInRange(L, R):
    LXR = L ^ R
    msbPos = 0
    while LXR:
        msbPos += 1
        LXR >>= 1
    maxXOR, two = 0, 1
    while msbPos:
        maxXOR += two
        two <<= 1
        msbPos -= 1
    return maxXOR


def main(n):
    L = n
    R = 2 * n + 1
    result = maxXORInRange(L, R)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)