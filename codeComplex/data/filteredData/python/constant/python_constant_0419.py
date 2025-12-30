import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设 a, b 为 1..n 范围内的两个整数，并保证 a <= b
    a = random.randint(1, n)
    b = random.randint(a, n)

    # 原逻辑
    c, d = ((b + 1) // 2 - 1, (b - a - 1))
    result = c if d < 0 else c - d if c > d else 0

    print(result)

if __name__ == "__main__":
    # 示例：使用 n = 100 运行一次
    main(100)