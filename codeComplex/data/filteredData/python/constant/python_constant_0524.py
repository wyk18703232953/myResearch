import random

def main(n: int):
    # 根据 n 生成测试数据
    # 这里将楼层坐标和时间参数控制在与 n 相关的合理范围内
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)
    t1 = random.randint(1, max(1, n))
    t2 = random.randint(1, max(1, n))
    t3 = random.randint(1, max(1, n))

    stairs = abs(x - y) * t1
    lift = abs(z - x) * t2 + t3 + t3 + abs(x - y) * t2 + t3

    print('YES' if lift <= stairs else 'NO')


if __name__ == "__main__":
    # 示例：可以在此处指定规模 n
    main(10)