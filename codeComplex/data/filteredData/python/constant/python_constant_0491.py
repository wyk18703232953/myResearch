import random

def main(n):
    # 生成测试数据：n 为规模，这里令 k 在 [1, n^2] 范围内随机
    if n <= 0:
        raise ValueError("n must be positive")
    k = random.randint(1, n * n)

    # 原逻辑：给定 n, k 输出 (k + n - 1) // n
    result = (k + n - 1) // n
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)