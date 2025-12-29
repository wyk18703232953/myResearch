import decimal
import random

decimal.getcontext().prec = 100


def DecimalPow(a, b):
    return decimal.Decimal(a) ** decimal.Decimal(b)


def solve_case(a, v, l, d, w):
    def getLastT(v1, dist):
        t1 = (v - v1) / a
        d1 = v1 * t1 + decimal.Decimal('0.5') * a * DecimalPow(t1, 2)
        if d1 >= dist:
            return (-v1 + (v1 ** decimal.Decimal(2) + 2 * a * dist) ** decimal.Decimal('0.5')) / a
        t2 = (dist - d1) / v
        return t1 + t2

    if w >= v:
        t = getLastT(decimal.Decimal('0'), l)
        return '{t:.5f}'.format(t=t)

    if (w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t = getLastT(decimal.Decimal('0'), l)
        return '{t:.5f}'.format(t=t)

    if (v ** decimal.Decimal(2)) / (2 * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t2 = -w / a + ((w ** decimal.Decimal(2)) / (2 * (a ** decimal.Decimal(2))) + d / a) ** decimal.Decimal('0.5')
        t1 = w / a + t2
        t3 = getLastT(w, l - d)
        t = t1 + t2 + t3
        return '{t:.5f}'.format(t=t)

    t1 = v / a
    t3 = (v - w) / a
    t2 = (d - ((v ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) +
               (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a))) / v
    t4 = getLastT(w, l - d)
    t = t1 + t2 + t3 + t4
    return '{t:.5f}'.format(t=t)


def main(n: int):
    """
    生成 n 组测试数据并输出对应结果。
    这里简单生成一些合理范围内的随机数据：
      a: [0.1, 5]
      v: [1, 50]
      l: [10, 1000]
      d: [0, l]
      w: [0, 50]
    """
    random.seed(0)
    for _ in range(n):
        # 生成测试数据（浮点转为字符串再转 Decimal，避免二进制误差）
        a = decimal.Decimal(str(round(random.uniform(0.1, 5.0), 3)))
        v = decimal.Decimal(str(round(random.uniform(1.0, 50.0), 3)))
        l = decimal.Decimal(str(round(random.uniform(10.0, 1000.0), 3)))
        d = decimal.Decimal(str(round(random.uniform(0.0, float(l)), 3)))
        w = decimal.Decimal(str(round(random.uniform(0.0, 50.0), 3)))

        ans = solve_case(a, v, l, d, w)
        print(ans)


if __name__ == "__main__":
    # 示例：生成 3 组测试
    main(3)