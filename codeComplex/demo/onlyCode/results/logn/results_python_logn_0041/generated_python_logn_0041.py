import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假定：l 和 r 在 [0, 2^n - 1] 范围内随机生成，且 l <= r
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(l, max_val)

    # 原始逻辑
    x = l ^ r
    pow2 = 1
    while pow2 <= x:
        pow2 *= 2

    print(pow2 - 1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)