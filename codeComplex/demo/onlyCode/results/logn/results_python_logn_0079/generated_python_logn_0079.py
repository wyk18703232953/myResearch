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
    # 生成规模为 n 的测试数据：随机生成 L, R，保证 L <= R
    # n 用作数值规模的上界（位数规模），这里设定为最大值 2^n - 1
    if n <= 0:
        n = 1
    max_val = (1 << n) - 1

    L = random.randint(0, max_val)
    R = random.randint(0, max_val)
    if L > R:
        L, R = R, L

    print(maxXORInRange(L, R))

if __name__ == "__main__":
    # 示例：以 n=10 作为规模运行
    main(10)