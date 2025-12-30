import random

def maxXORInRange(L, R):
    LXR = L ^ R
    msbPos = 0
    while LXR:
        msbPos += 1
        LXR >>= 1
    maxXOR = (1 << msbPos) - 1
    return maxXOR

def main(n):
    # 根据规模 n 生成两个非负整数 L, R（范围可根据需要调整）
    # 这里设置最大值为 2^n - 1
    max_val = (1 << n) - 1
    L = random.randint(0, max_val)
    R = random.randint(0, max_val)
    if L > R:
        L, R = R, L

    result = maxXORInRange(L, R)
    print(L, R)
    print(result)

if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(10)