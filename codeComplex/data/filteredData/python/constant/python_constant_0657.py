def path(x1, y1, x2, y2, hor):
    out = []
    if hor:
        for i in range(x2 - x1):
            out.append((x1 + i, y1))
        if y2 > y1:
            for i in range(y2 - y1):
                out.append((x2, y1 + i))
        else:
            for i in range(y1 - y2):
                out.append((x2, y1 - i))
    else:
        for i in range(x2 - x1):
            out.append((x2 - i, y2))
        if y2 > y1:
            for i in range(y2 - y1):
                out.append((x1, y2 - i))
        else:
            for i in range(y1 - y2):
                out.append((x1, y2 + i))
    return out[1:]


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里简单地让三个点在 [0, n] 的网格内，保持整数坐标。
    # 可以按需要修改生成策略。
    a, b = 0, 0
    c, d = n // 2, n // 3
    e, f = n, n // 2

    if a > c:
        a, b, c, d = c, d, a, b
    if c > e:
        c, d, e, f = e, f, c, d
    if a > c:
        a, b, c, d = c, d, a, b
    if c == e and abs(f - b) < abs(d - b):
        c, d, e, f = e, f, c, d

    g1 = path(a, b, c, d, True)
    if d > b:
        if f < b:
            g2 = path(c, b, e, f, True)
        elif f < d:
            g2 = path(c, f, e, f, True)
        else:
            g2 = path(c, d, e, f, True)
    else:
        if f < d:
            g2 = path(c, d, e, f, True)
        elif f < b:
            g2 = path(c, f, e, f, True)
        else:
            g2 = path(c, b, e, f, True)

    print(len(g1) + len(g2) + 3)
    print(a, b)
    print(c, d)
    print(e, f)
    for x, y in g1:
        print(x, y)
    for x, y in g2:
        print(x, y)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)