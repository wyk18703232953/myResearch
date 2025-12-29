import random

def main(n: int):
    # 根据规模 n 生成测试数据 (m, a)
    # 这里简单设置：1 <= m <= n，0 <= a <= n^2
    m = random.randint(1, max(1, n))
    a = random.randint(0, max(1, n * n))

    # 原逻辑：计算 a / m 的向上取整
    if a % m == 0:
        print(a // m)
    else:
        print(a // m + 1)

if __name__ == "__main__":
    # 示例：使用 n=10 运行
    main(10)