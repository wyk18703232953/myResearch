import decimal
import random

decimal.getcontext().prec = 100


def DecimalPow(a, b):
    return decimal.Decimal(a) ** decimal.Decimal(b)


def getLastT(a, v, v1, dist):
    t1 = (v - v1) / a
    d1 = v1 * t1 + decimal.Decimal('0.5') * a * DecimalPow(t1, 2)
    if d1 >= dist:
        return (-v1 + (v1 ** decimal.Decimal(2) + 2 * a * dist) ** decimal.Decimal('0.5')) / a
    t2 = (dist - d1) / v
    return t1 + t2


def solve(a, v, l, d, w):
    if w >= v:
        t1 = v / a
        if decimal.Decimal('0.5') * a * (t1 ** decimal.Decimal(2)) <= l:
            t2 = (l - decimal.Decimal('0.5') * a * (t1 ** decimal.Decimal(2))) / v
        else:
            t1 = (decimal.Decimal(2) * l / a) ** decimal.Decimal('0.5')
            t2 = decimal.Decimal(0)
        t = t1 + t2
        return '{t:.5f}'.format(t=t)

    if (w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t = getLastT(a, v, decimal.Decimal(0), l)
        return '{t:.5f}'.format(t=t)

    if (v ** decimal.Decimal(2) - 0) / (2 * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (
        decimal.Decimal(2) * a
    ) >= d:
        t2 = -w / a + (
            (w ** decimal.Decimal(2)) / (2 * (a ** decimal.Decimal(2))) + d / a
        ) ** decimal.Decimal('0.5')
        t1 = w / a + t2
        t3 = getLastT(a, v, w, l - d)
        t = t1 + t2 + t3
        return '{t:.5f}'.format(t=t)

    t1 = v / a
    t3 = (v - w) / a
    t2 = (d - ((v ** decimal.Decimal(2) - 0) / (decimal.Decimal(2) * a) +
               (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a))) / v
    t4 = getLastT(a, v, w, l - d)
    t = t1 + t2 + t3 + t4
    return '{t:.5f}'.format(t=t)


def main(n):
    # 根据规模 n 生成测试数据：
    # n 用作不同参数的放大因子，使规模随 n 增长
    # 保证 a > 0, v > 0, l > 0, d >= 0, w >= 0
    random.seed(n)

    # 生成 decimal 参数
    # a: 加速度，范围 (0.1, 5*n]
    a_val = decimal.Decimal(str(random.uniform(0.1, 5.0 * max(1, n))))
    # v: 最大速度，范围 (1, 50*n]
    v_val = decimal.Decimal(str(random.uniform(1.0, 50.0 * max(1, n))))
    # l: 总路程，范围 (10, 1000*n]
    l_val = decimal.Decimal(str(random.uniform(10.0, 1000.0 * max(1, n))))
    # d: 特殊区间长度，范围 [0, l)
    d_val = decimal.Decimal(str(random.uniform(0.0, float(l_val) * 0.9)))
    # w: 区间内限速，范围 [0, 1.5*v]
    w_val = decimal.Decimal(str(random.uniform(0.0, float(v_val) * 1.5)))

    ans = solve(a_val, v_val, l_val, d_val, w_val)
    print(ans)


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)