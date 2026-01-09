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
    # 根据规模 n 生成测试数据：
    # 这里约定：生成一对 (L, R)，满足 0 <= L < R <= n
    # 若 n < 2，则退化为 L=0, R=n
    if n < 2:
        L, R = 0, max(1, n)

    else:
        # 简单策略：取 L = n // 3, R = n
        L, R = n // 3, n

    result = maxXORInRange(L, R)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可在此修改 n 的值进行测试
    main(10)