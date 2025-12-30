def maxXORInRange(L, R):
    # get xor of limits
    LXR = L ^ R

    # loop to get msb position of L^R
    msbPos = 0
    while LXR:
        msbPos += 1
        LXR >>= 1

    # construct result by adding 1, msbPos times
    maxXOR, two = 0, 1
    while msbPos:
        maxXOR += two
        two <<= 1
        msbPos -= 1

    return maxXOR


def main(n):
    """
    使用规模 n 生成测试数据：
    这里约定：
      - L = 0
      - R = n
    即在 [0, n] 区间上求最大异或值。
    你可以根据需要修改 L, R 的生成策略。
    """
    L = 0
    R = n
    ans = maxXORInRange(L, R)
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 20 运行
    main(20)