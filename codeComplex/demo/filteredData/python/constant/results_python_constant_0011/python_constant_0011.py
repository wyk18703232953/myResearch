import decimal
decimal.getcontext().prec = 100

def DecimalPow(a, b):
    return decimal.Decimal(a) ** decimal.Decimal(b)

def getLastT(a, v, v1, dist):
    t1 = (v - v1) / a
    d1 = v1 * t1 + decimal.Decimal(0.5) * a * DecimalPow(t1, 2)
    if d1 >= dist:
        return (-v1 + (v1 ** decimal.Decimal(2) + 2 * a * dist) ** decimal.Decimal(0.5)) / a
    t2 = (dist - d1) / v
    return t1 + t2

def core(a, v, l, d, w):
    if w >= v:
        t = getLastT(a, v, decimal.Decimal(0), l)
        return '{t:.5f}'.format(t=t)
    elif (w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t = getLastT(a, v, decimal.Decimal(0), l)
        return '{t:.5f}'.format(t=t)
    elif (v ** decimal.Decimal(2) - 0) / (2 * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t2 = -w / a + ((w ** decimal.Decimal(2)) / (2 * (a ** decimal.Decimal(2))) + d / a) ** decimal.Decimal(0.5)
        t1 = w / a + t2
        t3 = getLastT(a, v, w, l - d)
        t = t1 + t2 + t3
        return '{t:.5f}'.format(t=t)

    else:
        t1 = v / a
        t3 = (v - w) / a
        t2 = (d - ((v ** decimal.Decimal(2) - 0) / (decimal.Decimal(2) * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a))) / v
        t4 = getLastT(a, v, w, l - d)
        t = t1 + t2 + t3 + t4
        return '{t:.5f}'.format(t=t)

def main(n):
    # 将 n 映射为确定性的测试规模
    # 构造一组参数 (a, v, l, d, w)，与 n 线性相关但保持物理意义
    # 使用 decimal.Decimal 保持与原程序一致
    a = decimal.Decimal(1 + (n % 5))         # 加速度在 1 到 5 之间
    v = decimal.Decimal(10 + (n % 10))       # 最大速度在 10 到 19 之间
    l = decimal.Decimal(100 + 3 * n)         # 总路程随 n 增长
    d = decimal.Decimal(20 + (2 * n) % 80)   # 区间长度保持在 [20, 99]
    # 保证 w 不为负，且有时大于 v，有时小于 v
    w = decimal.Decimal((5 + n) % 25)        # 0 到 24 之间

    result = core(a, v, l, d, w)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)