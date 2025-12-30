import random

def main(n: int):
    # 根据 n 生成测试数据
    # 为了避免除零，保证 m >= 1
    m = max(1, n)

    # 随机生成 a, b，这里设置一个相对合理的范围
    a = random.randint(1, 10**6)
    b = random.randint(1, 10**6)

    # 原逻辑：n, m, a, b 已直接使用
    result = min(n % m * b, (m - n % m) * a)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)