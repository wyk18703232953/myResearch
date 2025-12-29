import random

def balance(x1, y1, x2, y2):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


def query(rects, x1, y1, x2, y2):
    """返回有多少个目标矩形与 [x1,y1,x2,y2] 有非空交集。"""
    x1, y1, x2, y2 = balance(x1, y1, x2, y2)
    cnt = 0
    for (lx, ly, rx, ry) in rects:
        if not (rx < x1 or x2 < lx or ry < y1 or y2 < ly):
            cnt += 1
    return cnt


def get_lr(n, rects):
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(rects, x1, y1, x2, y2)
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
        res = query(rects, x1, y1, x2, y2)
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
        res = query(rects, x1, y1, x2, y2)
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
        res = query(rects, x1, y1, x2, y2)
        if res >= 1:
            l = m
        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def get_ud(n, rects):
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, n, m
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = query(rects, x1, y1, x2, y2)
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
        res = query(rects, x1, y1, x2, y2)
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
        res = query(rects, x1, y1, x2, y2)
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
        res = query(rects, x1, y1, x2, y2)
        if res >= 1:
            l = m
        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def gen_rect(n):
    x1 = random.randint(1, n)
    x2 = random.randint(1, n)
    y1 = random.randint(1, n)
    y2 = random.randint(1, n)
    return balance(x1, y1, x2, y2)


def main(n, seed=0):
    random.seed(seed)
    # 生成两个人工目标矩形
    rect1 = gen_rect(n)
    rect2 = gen_rect(n)
    rects = [rect1, rect2]

    lr = get_lr(n, rects)
    ud = get_ud(n, rects)
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
                    res1 = query(rects, l1, d1, r1, u1)
                    res2 = query(rects, l2, d2, r2, u2)
                    if res1 == res2 == 1:
                        # 返回推断出的两个矩形以及真实数据，方便测试
                        return {
                            "found": (l1, d1, r1, u1, l2, d2, r2, u2),
                            "real": (rect1, rect2),
                            "n": n,
                        }
    return {
        "found": None,
        "real": (rect1, rect2),
        "n": n,
    }


if __name__ == "__main__":
    # 示例运行
    result = main(10, seed=1)
    print(result)