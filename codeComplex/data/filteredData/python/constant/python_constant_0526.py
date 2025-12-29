import random

def main(n):
    # n 不直接用于循环，仅作为规模参数参与数据生成范围控制
    # 根据 n 设置坐标和时间参数的上限
    coord_limit = max(1, n)
    time_limit = max(1, n)

    # 随机生成测试数据
    x = random.randint(0, coord_limit)
    y = random.randint(0, coord_limit)
    z = random.randint(0, coord_limit)
    t1 = random.randint(1, time_limit)
    t2 = random.randint(1, time_limit)
    t3 = random.randint(1, time_limit)

    elev = t3 * 3 + t2 * (abs(z - x) + abs(x - y))
    stairs = t1 * abs(x - y)
    if elev <= stairs:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：用规模 n=10 运行
    main(10)