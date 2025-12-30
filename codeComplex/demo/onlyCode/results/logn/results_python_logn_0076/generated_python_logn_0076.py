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
    """
    n 为规模参数，用于生成一组 (L, R) 测试数据，并输出其最大异或值。
    这里简单按以下方式生成：
    L = n
    R = 2 * n + 1 （保证 R >= L 且区间有一定宽度）
    """
    L = n
    R = 2 * n + 1
    print(maxXORInRange(L, R))


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)