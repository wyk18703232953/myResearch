#!/usr/bin/env python3
import random

def contain(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return bx1 <= ax1 and ax2 <= bx2 and by1 <= ay1 and ay2 <= by2

def rect_intersect(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return not (ax2 <= bx1 or bx2 <= ax1 or ay2 <= by1 or by2 <= ay1)

def rect_inside(q, r):
    # q completely inside r
    qx1, qy1, qx2, qy2 = q
    rx1, ry1, rx2, ry2 = r
    return rx1 <= qx1 and qx2 <= rx2 and ry1 <= qy1 and qy2 <= ry2

def ask(x1, y1, x2, y2, known=(), memo={}, hidden_rects=None):
    if x2 < x1+1 or y2 < y1+1:
        return 0
    ofs = len(list(filter(lambda rect: contain(rect, (x1, y1, x2, y2)), known)))
    key = (x1+1, y1+1, x2, y2)
    if key in memo:
        return memo[key] - ofs
    # simulate judge: count hidden_rects fully inside query
    cnt = 0
    if hidden_rects is not None:
        q = (x1, y1, x2, y2)
        for r in hidden_rects:
            if rect_inside(r, q):
                cnt += 1
    memo[key] = cnt
    return memo[key] - ofs

def binsearch(l, r, p):  # (l,r], return the smallest n which p holds
    assert l < r
    while l + 1 != r:
        m = (l + r) // 2
        if p(m):
            r = m
        else:
            l = m
    return r

def shrink(x1, y1, x2, y2, cnt, known=(), hidden_rects=None):
    assert ask(x1, y1, x2, y2, known=known, hidden_rects=hidden_rects) == cnt
    x1 = binsearch(x1, x2,
                   lambda x: ask(x, y1, x2, y2, known=known, hidden_rects=hidden_rects) != cnt) - 1
    y1 = binsearch(y1, y2,
                   lambda y: ask(x1, y, x2, y2, known=known, hidden_rects=hidden_rects) != cnt) - 1
    x2 = binsearch(x1, x2,
                   lambda x: ask(x1, y1, x, y2, known=known, hidden_rects=hidden_rects) == cnt)
    y2 = binsearch(y1, y2,
                   lambda y: ask(x1, y1, x2, y, known=known, hidden_rects=hidden_rects) == cnt)
    assert ask(x1, y1, x2, y2, known=known, hidden_rects=hidden_rects) == cnt
    assert ask(x1, y1, x2, y2, known=known, hidden_rects=hidden_rects) == cnt
    return x1, y1, x2, y2

def go(x1, y1, x2, y2, hidden_rects):
    assert ask(x1, y1, x2, y2, hidden_rects=hidden_rects) == 2
    x1, y1, x2, y2 = shrink(x1, y1, x2, y2, 2, hidden_rects=hidden_rects)
    a = None
    if not a and x1 < x2:
        if ask(x1 + 1, y1, x2, y2, hidden_rects=hidden_rects) == 1:
            a = shrink(x1 + 1, y1, x2, y2, 1, hidden_rects=hidden_rects)
        elif ask(x1, y1, x2 - 1, y2, hidden_rects=hidden_rects) == 1:
            a = shrink(x1, y1, x2 - 1, y2, 1, hidden_rects=hidden_rects)
    if not a and y1 < y2:
        if ask(x1, y1 + 1, x2, y2, hidden_rects=hidden_rects) == 1:
            a = shrink(x1, y1 + 1, x2, y2, 1, hidden_rects=hidden_rects)
        elif ask(x1, y1, x2, y2 - 1, hidden_rects=hidden_rects) == 1:
            a = shrink(x1, y1, x2, y2 - 1, 1, hidden_rects=hidden_rects)
    if not a:
        a = x1, y1, x2, y2
        return a, a
    else:
        b = shrink(x1, y1, x2, y2, 1, known=[a], hidden_rects=hidden_rects)
        return a, b

def generate_two_rects(n, max_tries=1000):
    # generate two non-empty rectangles within [0,n)×[0,n) that intersect
    for _ in range(max_tries):
        def rand_rect():
            x1 = random.randrange(0, n)
            x2 = random.randrange(x1 + 1, n + 1)
            y1 = random.randrange(0, n)
            y2 = random.randrange(y1 + 1, n + 1)
            return (x1, y1, x2, y2)
        r1 = rand_rect()
        r2 = rand_rect()
        if rect_intersect(r1, r2):
            return r1, r2
    # fallback: force intersection
    x1 = 0
    x2 = max(1, n // 2)
    y1 = 0
    y2 = max(1, n // 2)
    r1 = (x1, y1, x2, y2)
    r2 = (x1, y1, min(n, x2 + 1), min(n, y2 + 1))
    return r1, r2

def main(n):
    random.seed(0)
    r1, r2 = generate_two_rects(n)
    hidden_rects = [r1, r2]
    a, b = go(0, 0, n, n, hidden_rects)
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    print('!', ax1 + 1, ay1 + 1, ax2, ay2, bx1 + 1, by1 + 1, bx2, by2)

if __name__ == "__main__":
    # example run
    main(10)

# Made By Mostafa_Khaled