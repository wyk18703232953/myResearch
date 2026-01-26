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
    # 根据规模 n 生成测试数据：
    # 生成 L, R，保证 L < R 且数值规模与 n 相关
    # 这里简单设定：L = n，R = 2*n（n>=1）
    if n < 1:
        raise ValueError("n 必须为正整数")
    L = n
    R = 2 * n
    # 计算并输出结果
    # print(maxXORInRange(L, R))
    pass
if __name__ == "__main__":
    # 示例：使用 n=8 运行
    main(8)