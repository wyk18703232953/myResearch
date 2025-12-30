import random

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
    n 为规模参数，这里用来限定生成随机数的大小范围：
    0 <= L, R < 2^n
    """
    if n <= 0:
        L, R = 0, 0
    else:
        upper = (1 << n) - 1
        L = random.randint(0, upper)
        R = random.randint(0, upper)
        if L > R:
            L, R = R, L  # 保证 L <= R

    result = maxXORInRange(L, R)
    print(result)

if __name__ == "__main__":
    # 示例：使用 n = 5 进行测试
    main(5)