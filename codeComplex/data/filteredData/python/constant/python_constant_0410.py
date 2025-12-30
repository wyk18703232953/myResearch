import random


def main(n: int):
    # n 为规模参数，这里用它控制随机数范围
    # 例如：坐标在 [-n, n] 区间内随机生成
    lo, hi = -n, n

    # 生成测试数据：16 个整数，对应 a,b,...,p
    a = random.randint(lo, hi)
    b = random.randint(lo, hi)
    c = random.randint(lo, hi)
    d = random.randint(lo, hi)
    e = random.randint(lo, hi)
    f = random.randint(lo, hi)
    g = random.randint(lo, hi)
    h = random.randint(lo, hi)

    i = random.randint(lo, hi)
    j = random.randint(lo, hi)
    k = random.randint(lo, hi)
    l = random.randint(lo, hi)
    m = random.randint(lo, hi)
    n_ = random.randint(lo, hi)
    o = random.randint(lo, hi)
    p = random.randint(lo, hi)

    s1 = [[a, b], [c, d], [e, f], [g, h]]
    s1.sort()
    bleft = s1[0]
    tr = s1[3]
    u, v, w, x = bleft[0], bleft[1], tr[0], tr[1]

    def check(xd, dx, u, v, w, x):
        return (u <= xd <= w and v <= dx <= x)

    god = [(i + k + m + o) / 4, (j + l + n_ + p) / 4]
    nani = 0
    for moo in [[i, j], [k, l], [m, n_], [o, p]]:
        if check(moo[0], moo[1], u, v, w, x):
            print("Yes")
            return

    if check(god[0], god[1], u, v, w, x):
        nani += 1

    i, j = i + j, i - j
    k, l = k + l, k - l
    m, n_ = m + n_, m - n_
    o, p = o + p, o - p

    a, b = a + b, a - b
    c, d = c + d, c - d
    e, f = e + f, e - f
    g, h = g + h, g - h

    a, b, c, d, e, f, g, h, i, j, k, l, m, n_, o, p = (
        i, j, k, l, m, n_, o, p, a, b, c, d, e, f, g, h
    )

    s1 = [[a, b], [c, d], [e, f], [g, h]]
    s1.sort()
    bleft = s1[0]
    tr = s1[3]
    u, v, w, x = bleft[0], bleft[1], tr[0], tr[1]

    def check2(xd, dx, u, v, w, x):
        return (u <= xd <= w and v <= dx <= x)

    god = [(i + k + m + o) / 4, (j + l + n_ + p) / 4]

    for moo in [[i, j], [k, l], [m, n_], [o, p]]:
        if check2(moo[0], moo[1], u, v, w, x):
            print("Yes")
            return

    if check2(god[0], god[1], u, v, w, x):
        nani += 1
    if nani == 2:
        print("Yes")
        return

    print("No")


if __name__ == "__main__":
    # 示例：调用 main(100) 生成坐标范围在 [-100, 100] 的随机数据
    main(100)