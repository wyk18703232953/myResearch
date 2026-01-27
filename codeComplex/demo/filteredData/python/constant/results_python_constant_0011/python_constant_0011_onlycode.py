import decimal
decimal.getcontext().prec = 100

a, v = map(decimal.Decimal, input().split())
l, d, w = map(decimal.Decimal, input().split())

def DecimalPow(a, b):
    return decimal.Decimal(a) ** decimal.Decimal(b)

def getLastT(v1, dist):
    t1 = (v - v1) / a
    d1 = v1 * t1 + decimal.Decimal(0.5) * a * DecimalPow(t1, 2)
    if d1 >= dist:
        return (-v1 + (v1 ** decimal.Decimal(2) + 2 * a * dist) ** decimal.Decimal(0.5)) / a
    t2 = (dist - d1) / v
    return t1 + t2

if w >= v:
    t = getLastT(0, l)
    print('{t:.5f}'.format(t = t))


elif (w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
    t = getLastT(0, l)
    print('{t:.5f}'.format(t = t))

elif (v ** decimal.Decimal(2) - 0) / (2 * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a) >= d:
    t2 = -w / a + ((w ** decimal.Decimal(2)) / (2 * (a ** decimal.Decimal(2))) + d / a) ** decimal.Decimal(0.5)
    t1 = w / a + t2
    t3 = getLastT(w, l - d)
    t = t1 + t2 + t3
    print('{t:.5f}'.format(t = t))

else:
    t1 = v / a
    t3 = (v - w) / a
    t2 = (d - ((v ** decimal.Decimal(2) - 0) / (decimal.Decimal(2) * a) + (v ** decimal.Decimal(2) - w ** decimal.Decimal(2)) / (decimal.Decimal(2) * a))) / v
    t4 = getLastT(w, l - d)
    t = t1 + t2 + t3 + t4
    print('{t:.5f}'.format(t = t))