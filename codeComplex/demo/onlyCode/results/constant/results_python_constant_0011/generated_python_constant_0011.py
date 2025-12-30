import decimal
import random

decimal.getcontext().prec = 100


def DecimalPow(a, b):
    return decimal.Decimal(a) ** decimal.Decimal(b)


def getLastT(a, v, v1, dist):
    # time to accelerate from v1 to v with constant acceleration a and cover dist
    t1 = (v - v1) / a
    d1 = v1 * t1 + decimal.Decimal("0.5") * a * DecimalPow(t1, 2)
    if d1 >= dist:
        # does not reach max speed v
        return (-v1 + (v1 ** decimal.Decimal(2) + 2 * a * dist) ** decimal.Decimal("0.5")) / a
    # reaches v, then cruise
    t2 = (dist - d1) / v
    return t1 + t2


def main(n):
    """
    n 用作测试规模参数，这里简单用 n 生成一组确定的测试数据。
    你可以根据需要修改生成规则。
    """
    # 为了可重复，这里不用 random，而是根据 n 构造一组数
    # 保证 a>0, v>0, l>0, d>0, w>=0 且范围大致合理
    a = decimal.Decimal(0.1 + (n % 50) * 0.1)          # [0.1, 5.0]
    v = decimal.Decimal(1 + (n % 100))                 # [1, 100]
    l = decimal.Decimal(50 + (n % 300))                # [50, 349]
    d = decimal.Decimal(10 + (n % 40))                 # [10, 49]
    w = decimal.Decimal((n * 3) % 120)                 # [0, 119]

    # 确保 d 不超过 l（必要时截断）
    if d > l:
        d = l / 2

    # 下面是原逻辑，只是改为使用局部变量而不是 input()
    if w >= v:
        t = getLastT(a, v, decimal.Decimal(0), l)
        print("{t:.5f}".format(t=t))

    elif (w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t = getLastT(a, v, decimal.Decimal(0), l)
        print("{t:.5f}".format(t=t))

    elif (v ** decimal.Decimal(2) - 0) / (2 * a) + (
        v ** decimal.Decimal(2) - w ** decimal.Decimal(2)
    ) / (decimal.Decimal(2) * a) >= d:
        t2 = -w / a + (
            (w ** decimal.Decimal(2)) / (2 * (a ** decimal.Decimal(2))) + d / a
        ) ** decimal.Decimal("0.5")
        t1 = w / a + t2
        t3 = getLastT(a, v, w, l - d)
        t = t1 + t2 + t3
        print("{t:.5f}".format(t=t))

    else:
        t1 = v / a
        t3 = (v - w) / a
        t2 = (
            d
            - (
                (v ** decimal.Decimal(2) - 0) / (decimal.Decimal(2) * a)
                + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2))
                / (decimal.Decimal(2) * a)
            )
        ) / v
        t4 = getLastT(a, v, w, l - d)
        t = t1 + t2 + t3 + t4
        print("{t:.5f}".format(t=t))


if __name__ == "__main__":
    # 示例：用 n=10 调用一次
    main(10)