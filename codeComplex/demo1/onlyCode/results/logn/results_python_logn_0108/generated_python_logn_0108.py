import random

def main(n: int):
    # 1. 生成测试数据：根据规模 n 生成 l, r
    # 这里简单设定范围为 [0, 2^n - 1]，
    # 再随机生成 l <= r
    if n <= 0:
        l = 0
        r = 0
    else:
        upper = (1 << n) - 1
        l = random.randint(0, upper)
        r = random.randint(l, upper)

    # 2. 保留原有逻辑
    LXR = l ^ r
    msbPos = 0
    while LXR:
        msbPos += 1
        LXR >>= 1

    maxXOR, two = 0, 1
    while msbPos:
        maxXOR += two
        two <<= 1
        msbPos -= 1

    print(maxXOR)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)