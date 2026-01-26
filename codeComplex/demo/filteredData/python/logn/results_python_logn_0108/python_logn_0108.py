def main(n):
    # 映射 n 为 l, r 的规模
    l = n
    r = 2 * n + 1

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
    # print(maxXOR)
    pass
if __name__ == "__main__":
    main(10)