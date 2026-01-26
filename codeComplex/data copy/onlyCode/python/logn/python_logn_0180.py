def balance(x1, y1, x2, y2):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


def get_lr():
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        print('?', x1, y1, x2, y2)
        res = int(input())
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
        print('?', x1, y1, x2, y2)
        res = int(input())
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
        print('?', x1, y1, x2, y2)
        res = int(input())
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
        print('?', x1, y1, x2, y2)
        res = int(input())
        if res >= 1:
            l = m
        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def get_ud():
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, n, m
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        print('?', x1, y1, x2, y2)
        res = int(input())
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
        print('?', x1, y1, x2, y2)
        res = int(input())
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
        print('?', x1, y1, x2, y2)
        res = int(input())
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
        print('?', x1, y1, x2, y2)
        res = int(input())
        if res >= 1:
            l = m
        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


n = int(input())
lr = get_lr()
ud = get_ud()
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
                print('?', l1, d1, r1, u1)
                res1 = int(input())
                print('?', l2, d2, r2, u2)
                res2 = int(input())
                if res1 == res2 == 1:
                    print('!', l1, d1, r1, u1, l2, d2, r2, u2)
                    __import__('sys').exit(0)
