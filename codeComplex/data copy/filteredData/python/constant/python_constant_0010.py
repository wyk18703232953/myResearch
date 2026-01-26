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
        t1 = v / a
        if decimal.Decimal(0.5) * a * (t1 ** decimal.Decimal(2)) <= l:
            t2 = (l - decimal.Decimal(0.5) * a * (t1 ** decimal.Decimal(2))) / v

        else:
            t1 = (decimal.Decimal(2) * l / a) ** decimal.Decimal(0.5)
            t2 = decimal.Decimal(0)
        t = t1 + t2
        return '{t:.5f}'.format(t=t)

    if (w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t = getLastT(a, v, decimal.Decimal(0), l)
        return '{t:.5f}'.format(t=t)

    if (v ** decimal.Decimal(2) - 0) / (2 * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
        t2 = -w / a + ((w ** decimal.Decimal(2)) / (2 * (a ** decimal.Decimal(2))) + d / a) ** decimal.Decimal(0.5)
        t1 = w / a + t2
        t3 = getLastT(a, v, w, l - d)
        t = t1 + t2 + t3
        return '{t:.5f}'.format(t=t)

    t1 = v / a
    t3 = (v - w) / a
    t2 = (d - ((v ** decimal.Decimal(2) - 0) / (decimal.Decimal(2) * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a))) / v
    t4 = getLastT(a, v, w, l - d)
    t = t1 + t2 + t3 + t4
    return '{t:.5f}'.format(t=t)

def main(n):
    # n 决定规模：生成 n 组测试数据并顺序执行核心算法
    # 确定性构造参数，确保同一 n 下结果可复现
    results = []
    for i in range(1, n + 1):
        # 构造一些随 i 线性变化但保持合理关系的 Decimal 参数
        # 避免除零，并保证 a>0, v>0, l>0, d>=0, w>=0
        a = decimal.Decimal(1 + (i % 5))          # 1~5
        v = decimal.Decimal(5 + (i % 7))          # 5~11
        l = decimal.Decimal(50 + 3 * i)           # 递增路程
        d = decimal.Decimal((10 + 2 * i) % int(50 + 3 * i))  # 保证 d < l
        w = decimal.Decimal((i % 9) + 1)          # 1~9

        res = core(a, v, l, d, w)
        results.append(res)

    # 为了与原程序的行为相似，这里只打印最后一组的结果
    if results:
        # print(results[-1])
        pass
if __name__ == "__main__":
    main(10)