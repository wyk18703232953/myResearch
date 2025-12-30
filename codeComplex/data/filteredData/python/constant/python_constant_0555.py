import random

def main(n: int):
    # 生成测试数据：
    # 约束：保证 0 ≤ k + l ≤ n，且 m ≥ 1
    if n <= 0:
        raise ValueError("n must be positive")

    m = random.randint(1, max(1, n))               # 1 ≤ m ≤ n
    k = random.randint(0, n)                       # 0 ≤ k ≤ n
    l = random.randint(0, n - k)                   # 0 ≤ l ≤ n - k，保证 k + l ≤ n

    # 原逻辑
    x = (k + l + m - 1) // m
    if x * m > n:
        result = -1
    else:
        result = x

    print(result)


if __name__ == "__main__":
    # 示例调用：可根据需要修改规模 n
    main(100)