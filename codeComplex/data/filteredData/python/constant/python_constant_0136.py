import random

def main(n: int):
    # 生成测试数据：随机生成 1 ≤ m ≤ n 的整数
    # 为避免除以 0，确保 m >= 1
    if n <= 0:
        raise ValueError("n must be a positive integer")
    m = random.randint(1, n)

    a, b = n, m
    s = 0
    while b:
        s += a // b
        a, b = b, a % b
    print(s)

if __name__ == "__main__":
    # 示例：调用 main(100)
    main(100)