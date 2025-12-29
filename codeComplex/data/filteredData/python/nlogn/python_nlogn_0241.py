import random


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def f(v, i1, i2):
    d = [v[i2][i] - v[i1][i] for i in range(len(v[i1]))]

    res = []
    for x in v:
        d2 = [x[i] - v[i1][i] for i in range(len(v[i1]))]
        if cross(d, d2) != 0:
            res.append(x)

    return res


def main(n):
    # 生成 n 个二维整点，坐标范围可自行调整
    # 为了覆盖一般情况，随机生成在 [-10^6, 10^6] 区间
    LIM = 10**6
    v = [[random.randint(-LIM, LIM), random.randint(-LIM, LIM)] for _ in range(n)]

    if n <= 4:
        print("YES")
        return

    ok = False
    for first in range(3):
        if ok:
            break

        for second in range(first + 1, 3):
            other = f(v, first, second)

            if len(other) <= 2:
                ok = True
                break

            remainder = f(other, 0, 1)

            if not remainder:
                ok = True

    if ok:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：运行 main(10)
    main(10)