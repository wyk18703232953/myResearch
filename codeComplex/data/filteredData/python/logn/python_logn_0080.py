import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里生成一个区间 [l, r]，满足 0 <= l < r <= n
    if n < 1:
        return 0  # 没有合法区间，直接返回 0

    l = random.randint(0, max(0, n - 1))
    r = random.randint(l + 1, n)

    # 下面是原逻辑：计算区间 [l, r] 中任意一对数的最大 XOR 值
    xor = l ^ r

    bms = 0
    while xor != 0:
        bms = bms + 1
        xor = xor >> 1

    maxxor = 0
    dois = 1
    while bms != 0:
        maxxor = maxxor + dois
        dois = dois << 1
        bms = bms - 1

    print(maxxor)
    return maxxor

if __name__ == "__main__":
    # 示例：使用 n = 100 运行一次
    main(100)