def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def main(n):
    # 生成确定性的点集 a，大小为 n
    # 第一个点固定为 (0,0)
    # 后续点按照简单算术规则生成，保证可规模化且确定
    a = []
    for i in range(n):
        x = i
        y = (i * i + i) // 2
        a.append([x, y])

    if n == 0:
        # print('YES')
        pass
        return

    if n == 1:
        # print('YES')
        pass
        return

    d = {}
    vis = [0] * n

    for i in range(1, n):
        num = abs(a[i][1] - a[0][1])
        den = abs(a[i][0] - a[0][0])
        k = 1
        k = gcd(num, den)
        if k != 0:
            num //= k
            den //= k
        if ((a[i][1] - a[0][1]) * (a[i][0] - a[0][0])) < 0:
            num *= -1
        if (num, den) in d:
            d[(num, den)].append(i)

        else:
            d[(num, den)] = [i]

    maxx = 0
    ki = None
    for key in d.keys():
        if len(d[key]) > maxx:
            maxx = len(d[key])
            ki = key

    if ki is None:
        # print('YES')
        pass
        return

    vis[0] = 1
    for i in d[ki]:
        vis[i] = 1

    t = []
    for i in range(n):
        if not vis[i]:
            t.append(i)

    f = 1
    if len(t) > 1:
        num = abs(a[t[0][1]] - a[t[1]][1])
        den = abs(a[t[0]][0] - a[t[1]][0])
        k = 1
        k = gcd(num, den)
        if k != 0:
            num //= k
            den //= k
        if (a[t[0]][1] - a[t[1]][1]) * (a[t[0]][0] - a[t[1]][0]) < 0:
            num *= -1
        m = (num, den)
        for i in range(2, len(t)):
            num = abs(a[t[i]][1] - a[t[0]][1])
            den = abs(a[t[i]][0] - a[t[0]][0])
            k = gcd(num, den)
            if k != 0:
                num //= k
                den //= k
            if (a[t[0]][1] - a[t[i]][1]) * (a[t[0]][0] - a[t[i]][0]) < 0:
                num *= -1
            if (num, den) != m:
                f = 0

    if f:
        # print('YES')
        pass

    else:
        d = {}
        if n == 1:
            # print('YES')
            pass
            return
        vis = [0] * n
        a[0], a[1] = a[1], a[0]
        for i in range(1, n):
            num = abs(a[i][1] - a[0][1])
            den = abs(a[i][0] - a[0][0])
            k = 1
            k = gcd(num, den)
            if k != 0:
                num //= k
                den //= k
            if ((a[i][1] - a[0][1]) * (a[i][0] - a[0][0])) < 0:
                num *= -1
            if (num, den) in d:
                d[(num, den)].append(i)

            else:
                d[(num, den)] = [i]
        maxx = 0
        ki = None
        for key in d.keys():
            if len(d[key]) > maxx:
                maxx = len(d[key])
                ki = key

        if ki is None:
            # print('YES')
            pass
            return

        vis[0] = 1
        for i in d[ki]:
            vis[i] = 1
        t = []
        for i in range(n):
            if not vis[i]:
                t.append(i)
        f = 1
        if len(t) > 1:
            num = abs(a[t[0]][1] - a[t[1]][1])
            den = abs(a[t[0]][0] - a[t[1]][0])
            k = 1
            k = gcd(num, den)
            if k != 0:
                num //= k
                den //= k
            if (a[t[0]][1] - a[t[1]][1]) * (a[t[0]][0] - a[t[1]][0]) < 0:
                num *= -1
            m = (num, den)
            for i in range(2, len(t)):
                num = abs(a[t[i]][1] - a[t[0]][1])
                den = abs(a[t[i]][0] - a[t[0]][0])
                k = 1
                k = gcd(num, den)
                if k != 0:
                    num //= k
                    den //= k
                if (a[t[0]][1] - a[t[i]][1]) * (a[t[0]][0] - a[t[i]][0]) < 0:
                    num *= -1
                if (num, den) != m:
                    f = 0
        if f:
            # print('YES')
            pass

        else:
            # print('NO')
            pass
if __name__ == "__main__":
    main(10)