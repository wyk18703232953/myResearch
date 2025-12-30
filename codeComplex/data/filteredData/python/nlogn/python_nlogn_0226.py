import random
from collections import Counter


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def generate_test_data(n):
    # 生成 n 个点坐标 (x, y)
    # 为了更有意义，随机在 [-10^6, 10^6] 内取值
    coords = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        coords.append([x, y])
    return coords


def solve(a):
    n = len(a)
    if n == 1:
        print('YES')
        return

    d = {}
    vis = [0] * n

    # 以点0为基准统计斜率
    for i in range(1, n):
        num = abs(a[i][1] - a[0][1])
        den = abs(a[i][0] - a[0][0])
        if den == 0 and num == 0:
            # 重合点，视为同一直线，给一个固定key
            key = ('same', 0)
        else:
            k = gcd(num, den)
            num //= k
            den //= k
            if (a[i][1] - a[0][1]) * (a[i][0] - a[0][0]) < 0:
                num *= -1
            key = (num, den)
        d.setdefault(key, []).append(i)

    maxx = 0
    ki = None
    for k in d.keys():
        if len(d[k]) > maxx:
            maxx = len(d[k])
            ki = k

    vis[0] = 1
    for i in d[ki]:
        vis[i] = 1
    t = [i for i in range(n) if not vis[i]]

    f = 1
    if len(t) > 1:
        num = abs(a[t[0]][1] - a[t[1]][1])
        den = abs(a[t[0]][0] - a[t[1]][0])
        if den == 0 and num == 0:
            m = ('same', 0)
        else:
            k = gcd(num, den)
            num //= k
            den //= k
            if (a[t[0]][1] - a[t[1]][1]) * (a[t[0]][0] - a[t[1]][0]) < 0:
                num *= -1
            m = (num, den)
        for i in range(2, len(t)):
            num = abs(a[t[i]][1] - a[t[0]][1])
            den = abs(a[t[i]][0] - a[t[0]][0])
            if den == 0 and num == 0:
                key = ('same', 0)
            else:
                k = gcd(num, den)
                num //= k
                den //= k
                if (a[t[0]][1] - a[t[i]][1]) * (a[t[0]][0] - a[t[i]][0]) < 0:
                    num *= -1
                key = (num, den)
            if key != m:
                f = 0
                break

    if f:
        print('YES')
        return

    # 尝试以点1为基准
    d = {}
    a[0], a[1] = a[1], a[0]

    if n == 1:
        print('YES')
        return

    vis = [0] * n
    for i in range(1, n):
        num = abs(a[i][1] - a[0][1])
        den = abs(a[i][0] - a[0][0])
        if den == 0 and num == 0:
            key = ('same', 0)
        else:
            k = gcd(num, den)
            num //= k
            den //= k
            if ((a[i][1] - a[0][1]) * (a[i][0] - a[0][0])) < 0:
                num *= -1
            key = (num, den)
        d.setdefault(key, []).append(i)

    maxx = 0
    ki = None
    for k in d.keys():
        if len(d[k]) > maxx:
            maxx = len(d[k])
            ki = k

    vis[0] = 1
    for i in d[ki]:
        vis[i] = 1
    t = [i for i in range(n) if not vis[i]]

    f = 1
    if len(t) > 1:
        num = abs(a[t[0]][1] - a[t[1]][1])
        den = abs(a[t[0]][0] - a[t[1]][0])
        if den == 0 and num == 0:
            m = ('same', 0)
        else:
            k = gcd(num, den)
            num //= k
            den //= k
            if (a[t[0]][1] - a[t[1]][1]) * (a[t[0]][0] - a[t[1]][0]) < 0:
                num *= -1
            m = (num, den)
        for i in range(2, len(t)):
            num = abs(a[t[i]][1] - a[t[0]][1])
            den = abs(a[t[i]][0] - a[t[0]][0])
            if den == 0 and num == 0:
                key = ('same', 0)
            else:
                k = gcd(num, den)
                num //= k
                den //= k
                if (a[t[0]][1] - a[t[i]][1]) * (a[t[0]][0] - a[t[i]][0]) < 0:
                    num *= -1
                key = (num, den)
            if key != m:
                f = 0
                break

    if f:
        print('YES')
    else:
        print('NO')


def main(n):
    a = generate_test_data(n)
    solve(a)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)