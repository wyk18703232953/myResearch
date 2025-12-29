import random


def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里不直接用 n 作为坐标值，而是用它来确定取值范围
    # 例如：坐标和时间在 [-n, n] 或 [1, n] 范围内随机生成
    x = random.randint(-n, n)
    y = random.randint(-n, n)
    z = random.randint(-n, n)
    t1 = random.randint(1, max(1, n))
    t2 = random.randint(1, max(1, n))
    t3 = random.randint(1, max(1, n))

    # 原逻辑
    if 3 * t3 + t2 * (abs(z - x) + abs(x - y)) <= t1 * abs(x - y):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：可以在此处指定规模 n 进行测试
    main(10)