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
    # 根据规模 n 生成测试数据：构造 n 组 (L, R)，并打印对应的最大异或值
    # 这里将 L, R 控制在 [0, 2*n] 范围内
    random.seed(0)
    results = []
    for _ in range(n):
        L = random.randint(0, 2 * n)
        R = random.randint(L, 2 * n)  # 保证 L <= R
        results.append(maxXORInRange(L, R))
    # 返回结果列表，或根据需要打印
    for val in results:
        print(val)

if __name__ == "__main__":
    # 示例：使用规模 10 运行
    main(10)