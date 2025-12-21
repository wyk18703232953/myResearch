def balance(x1, y1, x2, y2):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


def query(grid, x1, y1, x2, y2):
    cnt = 0
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            if grid[i][j] == 1:
                cnt += 1
    return cnt


def get_lr(n, grid):
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(grid, x1, y1, x2, y2)
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
        res = query(grid, x1, y1, x2, y2)
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
        res = query(grid, x1, y1, x2, y2)
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
        res = query(grid, x1, y1, x2, y2)
        if res >= 1:
            l = m
        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def get_ud(n, grid):
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, n, m
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(grid, x1, y1, x2, y2)
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
        res = query(grid, x1, y1, x2, y2)
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
        res = query(grid, x1, y1, x2, y2)
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
        res = query(grid, x1, y1, x2, y2)
        if res >= 1:
            l = m
        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def main(n):
    grid = [[0] * n for _ in range(n)]
    if n >= 4:
        grid[0][0] = 1
        grid[n - 1][n - 1] = 1
    else:
        grid[0][0] = 1
        grid[0][min(1, n - 1)] = 1
    lr = get_lr(n, grid)
    ud = get_ud(n, grid)
    rr = [lr[0], lr[1]]
    ll = [lr[2], lr[3]]
    uu = [ud[0], ud[1]]
    dd = [ud[2], ud[3]]
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
                    res1 = query(grid, l1, d1, r1, u1)
                    res2 = query(grid, l2, d2, r2, u2)
                    if res1 == res2 == 1:
                        result = (l1, d1, r1, u1, l2, d2, r2, u2)
                        print(result)
                        return result
    print(None)
    return None


if __name__ == "__main__":
    main(8)