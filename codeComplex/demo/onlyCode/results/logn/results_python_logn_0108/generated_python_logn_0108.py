def main(n):
    l = n
    r = 2 * n
    LXR = l ^ r
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

if __name__ == "__main__":
    print(main(5))