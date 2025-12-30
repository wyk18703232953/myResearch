import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成区间 [l, r]
    # 这里我们令最大值为 2^n - 1，然后随机生成 l, r
    if n <= 0:
        return

    max_val = (1 << n) - 1
    l = random.randint(0, max_val)
    r = random.randint(l, max_val)

    # 原始逻辑：求区间 [l, r] 中任意两个数的最大异或值
    q = l ^ r
    a = 1
    while q:
        q //= 2
        a <<= 1
    print(a - 1)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)