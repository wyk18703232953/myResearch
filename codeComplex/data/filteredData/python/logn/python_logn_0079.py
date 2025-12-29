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
    # 根据规模 n 生成测试数据：
    # 让 L, R 落在 [0, 2^n - 1]，并保证 L <= R
    upper = (1 << n) - 1
    L = random.randint(0, upper)
    R = random.randint(L, upper)
    print(maxXORInRange(L, R))

if __name__ == "__main__":
    # 示例：n = 10，可根据需要修改
    main(10)