import random
import sys

def balance(x1, y1, x2, y2):
    return min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)


def make_query(rects, x1, y1, x2, y2):
    x1, y1, x2, y2 = balance(x1, y1, x2, y2)
    cnt = 0
    for rx1, ry1, rx2, ry2 in rects:
        ix1 = max(x1, rx1)
        iy1 = max(y1, ry1)
        ix2 = min(x2, rx2)
        iy2 = min(y2, ry2)
        if ix1 <= ix2 and iy1 <= iy2:
            cnt += 1
    return cnt


def get_lr(n, rects):
    l, r = 0, n
    while r - l > 1:
        m = (r + l) // 2
        x1, y1, x2, y2 = 1, 1, m, n
        x1, y1, x2, y2 = balance(x1, y1, x2, y2)
        res = make_query(rects, x1, y1, x2, y2)
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
        res = make_query(rects, x1, y1, x2, y2)
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
        res = make_query(rects, x1, y1, x2, y2)
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
        res = make_query(rects, x1, y1, x2, y2)
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
        res = make_query(rects, x1, y1, x2, y2)
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
        res = make_query(rects, x1, y1, x2, y2)
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
        res = make_query(rects, x1, y1, x2, y2)
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
        res = make_query(rects, x1, y1, x2, y2)
        if res >= 1:
            l = m
        else:
            r = m
    l1 = l
    return r1, r2, l2, l1


def generate_rect(n):
    x1 = random.randint(1, n)
    y1 = random.randint(1, n)
    x2 = random.randint(x1, n)
    y2 = random.randint(y1, n)
    return x1, y1, x2, y2


def main(n):
    # 生成两个人工测试矩形
    rect1 = generate_rect(n)
    rect2 = generate_rect(n)
    # 确保两个矩形不完全相同（仅作为测试方便）
    while rect2 == rect1:
        rect2 = generate_rect(n)

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
                    res1 = make_query(rects, l1, d1, r1, u1)
                    res2 = make_query(rects, l2, d2, r2, u2)
                    if res1 == res2 == 1:
                        # 输出找到的两个矩形
                        print('!', l1, d1, r1, u1, l2, d2, r2, u2)
                        return

    print("Failed to find rectangles")
    print("Actual rects:", rect1, rect2)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)