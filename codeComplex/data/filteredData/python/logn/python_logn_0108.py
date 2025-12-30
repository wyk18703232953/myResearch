import random

def main(n: int):
    # 生成测试数据：随机生成 l, r，保证 0 <= l <= r < 2^n
    if n <= 0:
        return

    upper_bound = 1 << n
    l = random.randint(0, upper_bound - 1)
    r = random.randint(l, upper_bound - 1)

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
    # 示例：n = 10，可以根据需要修改
    main(10)