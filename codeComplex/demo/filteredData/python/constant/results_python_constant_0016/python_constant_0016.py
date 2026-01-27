from math import sqrt

def main(n):
    # 根据 n 构造确定性的输入规模
    # a 加速度，v 最大速度
    # l 总路程长度，d 前半段路程长度，w 限速
    a = max(1, n % 10 + 1)          # 1 到 11 之间
    v = max(1, (n * 3) % 50 + 10)   # 10 到 59 之间
    l = max(2, n * 5)               # 总长度随 n 线性增长
    d = max(1, l // 3)              # 前段长度约占 1/3
    w = max(1, (n * 7) % 40 + 5)    # 5 到 44 之间

    w = min(v, w)
    lowtime = (v - w) / a
    lowdist = v * lowtime - a * lowtime**2 / 2
    startdist = v**2 / (2 * a)
    if startdist + lowdist <= d:
        ans = v / a + (d - startdist - lowdist) / v + lowtime
    elif w**2 <= 2 * d * a:
        u = sqrt(a * d + w**2 / 2)
        ans = (2 * u - w) / a

    else:
        ans = sqrt(2 * d / a)
        w = ans * a
    hightime = (v - w) / a
    highdist = w * hightime + a * hightime**2 / 2
    if highdist <= l - d:
        ans += hightime + (l - d - highdist) / v

    else:
        disc = sqrt(w**2 + 2 * a * (l - d))
        ans += (disc - w) / a
    # print('%.7f' % ans)
    pass
if __name__ == "__main__":
    main(100)