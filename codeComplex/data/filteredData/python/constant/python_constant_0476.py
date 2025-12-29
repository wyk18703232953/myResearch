import random

def main(n: int):
    # 生成测试数据：n 为规模，k 在 1 到 n^2 范围内
    k = random.randint(1, max(1, n * n))
    # 原逻辑：输出 (k + n - 1) // n
    print((k + n - 1) // n)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)