def balance(x1, y1, x2, y2):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


def query(prefix, x1, y1, x2, y2):
    # count number of points inside rectangle [x1,x2] x [y1,y2]
    return (
        prefix[x2][y2]
        - prefix[x1 - 1][y2]
        - prefix[x2][y1 - 1]
        + prefix[x1 - 1][y1 - 1]
    )


def get_lr(n, prefix):
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res < 2:
            l = m

        else:
            r = m
    r2 = r
    l, r = 1, n + 1
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = n, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res == 2:
            l = m

        else:
            r = m
    l2 = l

    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res < 1:
            l = m

        else:
            r = m
    r1 = r
    l, r = 1, n + 1
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = n, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res >= 1:
            l = m

        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def get_ud(n, prefix):
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, n, m
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res < 2:
            l = m

        else:
            r = m
    r2 = r
    l, r = 1, n + 1
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, n, n, m
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res == 2:
            l = m

        else:
            r = m
    l2 = l

    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, n, m
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res < 1:
            l = m

        else:
            r = m
    r1 = r
    l, r = 1, n + 1
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, n, n, m
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(prefix, x1, y1, x2, y2)
        if res >= 1:
            l = m

        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def build_points(n):
    # deterministically build two non-overlapping rectangles inside n x n
    # first rectangle
    x1 = 1
    y1 = 1
    x2 = max(1, n // 3)
    y2 = max(1, n // 3)
    # second rectangle
    x3 = min(n, (2 * n) // 3 + 1)
    y3 = min(n, (2 * n) // 3 + 1)
    x4 = n
    y4 = n
    # generate all points in both rectangles
    pts = []
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            pts.append((i, j))
    for i in range(x3, x4 + 1):
        for j in range(y3, y4 + 1):
            pts.append((i, j))
    return pts, (x1, y1, x2, y2, x3, y3, x4, y4)


def build_prefix(n, pts):
    prefix = [[0] * (n + 1) for _ in range(n + 1)]
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in pts:
        grid[x][y] = 1
    for i in range(1, n + 1):
        row_sum = 0
        for j in range(1, n + 1):
            row_sum += grid[i][j]
            prefix[i][j] = prefix[i - 1][j] + row_sum
    return prefix


def main(n):
    if n < 2:
        return None
    pts, true_rects = build_points(n)
    prefix = build_prefix(n, pts)
    lr = get_lr(n, prefix)
    ud = get_ud(n, prefix)
    rr = [lr[0], lr[1]]
    ll = [lr[2], lr[3]]
    uu = [ud[0], ud[1]]
    dd = [ud[2], ud[3]]
    found = None
    for r1 in rr:
        r2 = rr[0] if rr[0] != r1 else rr[1]
        for l1 in ll:
            l2 = ll[0] if ll[0] != l1 else ll[1]
            for u1 in uu:
                u2 = uu[0] if uu[0] != u1 else uu[1]
                for d1 in dd:
                    d2 = dd[0] if dd[0] != d1 else dd[1]
                    if r1 < l1 or r2 < l2 or u1 < d1 or u2 < d2:
                        continue
                    res1 = query(prefix, l1, d1, r1, u1)
                    res2 = query(prefix, l2, d2, r2, u2)
                    if res1 == res2 == 1:
                        found = (l1, d1, r1, u1, l2, d2, r2, u2)
                        return found
    return found


if __name__ == "__main__":
    # example call for time complexity experiments
    result = main(300)
    # print(result)
    pass