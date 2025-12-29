import random


def main(n):
    # 生成规模为 n 的测试数据：
    # 原程序需要两个长度为 8 的整数序列，每两个数构成一个点，共 4 个点。
    # 这里的 n 表示点的数量（必须 >= 4），多余的点不参与原逻辑，仅用于扩展规模。
    # 为兼容原逻辑，我们仍然只取前 4 个点参与计算。

    if n < 4:
        n = 4

    # 生成 n 个点，每个坐标在 [-10, 10] 范围内
    points_one = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(n)]
    points_two = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(n)]

    # 只取前 4 个点，转换为原代码所需的长度为 8 的列表形式
    one = []
    for x, y in points_one[:4]:
        one.extend([x, y])
    two = []
    for x, y in points_two[:4]:
        two.extend([x, y])

    one_ = sorted([(one[i], one[i + 1]) for i in range(0, 8, 2)],
                  key=lambda x: (x[1], x[0]))
    two_ = sorted([(two[i], two[i + 1]) for i in range(0, 8, 2)],
                  key=lambda x: (x[1], x[0]))

    ones = [one_[0], one_[2], one_[3], one_[1]]
    twos = [two_[1], two_[3], two_[2], two_[0]]

    L, D, U, R = ones[0][0], ones[0][1], ones[2][1], ones[2][0]

    def in_one(point):
        x, y = point
        return L <= x <= R and D <= y <= U

    def in_two(point):
        x_0, y_0 = twos[0]

        def U_p(x_):
            return x_ + y_0 - x_0

        def D_m(x_):
            return -x_ + y_0 + x_0

        x_1, y_1 = twos[2]

        def U_m(x_):
            return -x_ + y_1 + x_1

        def D_p(x_):
            return x_ + y_1 - x_1

        x, y = point
        return D_m(x) <= y <= U_p(x) and D_p(x) <= y <= U_m(x)

    c_one = ((L + R) / 2, (U + D) / 2)
    c_two = ((twos[0][0] + twos[2][0]) / 2,
             (twos[1][1] + twos[3][1]) / 2)

    ones.append(c_one)
    twos.append(c_two)

    for p in ones:
        if in_two(p):
            print('YES')
            return

    for p in twos:
        if in_one(p):
            print('YES')
            return

    print('NO')


if __name__ == "__main__":
    # 示例调用，n 可自行修改
    main(10)