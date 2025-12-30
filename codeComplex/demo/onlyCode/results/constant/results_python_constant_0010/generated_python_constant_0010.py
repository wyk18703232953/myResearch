import decimal
import random

decimal.getcontext().prec = 100


def DecimalPow(a, b):
    return decimal.Decimal(a) ** decimal.Decimal(b)


def getLastT(a, v, v1, dist):
    t1 = (v - v1) / a
    d1 = v1 * t1 + decimal.Decimal("0.5") * a * DecimalPow(t1, 2)
    if d1 >= dist:
        return (-v1 + (v1 ** decimal.Decimal("2") + 2 * a * dist) ** decimal.Decimal("0.5")) / a
    t2 = (dist - d1) / v
    return t1 + t2


def solve(a, v, l, d, w):
    if w >= v:
        t1 = v / a
        if decimal.Decimal("0.5") * a * (t1 ** decimal.Decimal("2")) <= l:
            t2 = (l - decimal.Decimal("0.5") * a * (t1 ** decimal.Decimal("2"))) / v
        else:
            t1 = (decimal.Decimal("2") * l / a) ** decimal.Decimal("0.5")
            t2 = decimal.Decimal("0")
        t = t1 + t2
        return t

    if (w ** decimal.Decimal("2")) / (decimal.Decimal("2") * a) >= d:
        t = getLastT(a, v, decimal.Decimal("0"), l)
        return t

    if (v ** decimal.Decimal("2") - decimal.Decimal("0")) / (2 * a) + (
        v ** decimal.Decimal("2") - w ** decimal.Decimal("2")
    ) / (decimal.Decimal("2") * a) >= d:
        t2 = -w / a + ((w ** decimal.Decimal("2")) / (2 * (a ** decimal.Decimal("2"))) + d / a) ** decimal.Decimal(
            "0.5"
        )
        t1 = w / a + t2
        t3 = getLastT(a, v, w, l - d)
        t = t1 + t2 + t3
        return t

    t1 = v / a
    t3 = (v - w) / a
    t2 = (
        d
        - (
            (v ** decimal.Decimal("2") - decimal.Decimal("0")) / (decimal.Decimal("2") * a)
            + (v ** decimal.Decimal("2") - w ** decimal.Decimal("2")) / (decimal.Decimal("2") * a)
        )
    ) / v
    t4 = getLastT(a, v, w, l - d)
    t = t1 + t2 + t3 + t4
    return t


def generate_test_case(n):
    # n 控制规模，这里简单用来放大距离和速度的范围
    # 保证加速度和距离为正，速度非负
    scale = max(1, n)
    a = decimal.Decimal(random.uniform(0.1, 5.0))  # 加速度
    v = decimal.Decimal(random.uniform(1.0, 50.0 * scale))  # 最大速度
    l = decimal.Decimal(random.uniform(10.0 * scale, 1000.0 * scale))  # 总路程
    # 保证 d 不大于 l
    d = decimal.Decimal(random.uniform(0.0, float(l)))
    w = decimal.Decimal(random.uniform(0.0, float(v) * 1.5))  # 限速区速度，可大于 v
    return a, v, l, d, w


def main(n):
    a, v, l, d, w = generate_test_case(n)
    t = solve(a, v, l, d, w)
    print("{t:.5f}".format(t=t))


if __name__ == "__main__":
    # 示例：用 n = 10 运行一次
    main(10)