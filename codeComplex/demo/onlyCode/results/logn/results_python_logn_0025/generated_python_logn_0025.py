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
    # 依据规模 n 生成测试数据，这里设定数值范围到 2^n - 1
    if n <= 0:
        # 若 n 非正，给一个默认的简单范围
        L, R = 0, 1
    else:
        max_val = (1 << n) - 1
        L = random.randint(0, max_val)
        R = random.randint(0, max_val)
        if L > R:
            L, R = R, L

    result = maxXORInRange(L, R)
    print(result)

if __name__ == "__main__":
    # 示例：可自行修改 n 测试规模
    main(10)