import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 为了演示，这里设定：
    # l1 在 [0, 2^n - 1] 范围内
    # l2 在 [0, 2^n - 1] 范围内
    # 并保证至少含 1 个 bit（n >= 1）
    if n < 1:
        raise ValueError("n must be >= 1")

    l1 = random.randint(0, (1 << n) - 1)
    l2 = random.randint(0, (1 << n) - 1)

    x = l1 ^ l2
    y = 1
    while y <= x:
        y *= 2

    print(y - 1)


if __name__ == "__main__":
    # 示例：可修改 n 测试不同规模
    main(10)