import random

def main(n):
    # 生成测试数据：
    # 将 n 看作原程序中的 n
    # 生成 m, a, b 为与 n 同规模的正整数
    if n <= 0:
        raise ValueError("n must be positive")

    m = random.randint(1, max(1, n))          # 保证 m >= 1
    a = random.randint(1, max(1, n))
    b = random.randint(1, max(1, n))

    # 原始逻辑
    x = n % m
    result = min(a * (m - x), b * x)

    print(result)


if __name__ == "__main__":
    # 示例：可自行调整 n 的值做规模测试
    main(100)