#!/usr/bin/env python3
import random

def contain(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return bx1 <= ax1 and ax2 <= bx2 and by1 <= ay1 and ay2 <= by2

def ask_factory(rects):
    """
    rects: list of rectangles (x1, y1, x2, y2), 0-based, [x1,x2) × [y1,y2)
    Returns an ask function that emulates the interactive judge:
    ask(x1,y1,x2,y2,known=(),memo={}) -> number of rectangles strictly inside.
    """
    def ask(x1, y1, x2, y2, known=(), memo={}):
        if x2 < x1 + 1 or y2 < y1 + 1:
            return 0
        ofs = len(list(filter(lambda rect: contain(rect, (x1, y1, x2, y2)), known)))
        key = (x1 + 1, y1 + 1, x2, y2)
        if key in memo:
            return memo[key] - ofs
        # simulate judge: count rects fully contained in (x1+1,y1+1,x2,y2)
        qx1, qy1, qx2, qy2 = key
        cnt = 0
        for rx1, ry1, rx2, ry2 in rects:
            if qx1 <= rx1 and rx2 <= qx2 and qy1 <= ry1 and ry2 <= qy2:
                cnt += 1
        memo[key] = cnt
        return memo[key] - ofs
    return ask

def binsearch(l, r, p):  # (l,r], return the smallest n which p holds
    assert l < r
    while l + 1 != r:
        m = (l + r) // 2
        if p(m):
            r = m
        else:
            l = m
    return r

def shrink(x1, y1, x2, y2, cnt, ask, known=()):
    assert ask(x1, y1, x2, y2, known=known) == cnt
    x1 = binsearch(x1, x2, lambda x: ask(x, y1, x2, y2, known=known) != cnt) - 1
    y1 = binsearch(y1, y2, lambda y: ask(x1, y, x2, y2, known=known) != cnt) - 1
    x2 = binsearch(x1, x2, lambda x: ask(x1, y1, x, y2, known=known) == cnt)
    y2 = binsearch(y1, y2, lambda y: ask(x1, y1, x2, y, known=known) == cnt)
    assert ask(x1, y1, x2, y2, known=known) == cnt
    assert ask(x1, y1, x2, y2, known=known) == cnt
    return x1, y1, x2, y2

def go(x1, y1, x2, y2, ask):
    assert ask(x1, y1, x2, y2) == 2
    x1, y1, x2, y2 = shrink(x1, y1, x2, y2, 2, ask)
    a = None
    if not a and x1 < x2:
        if ask(x1 + 1, y1, x2, y2) == 1:
            a = shrink(x1 + 1, y1, x2, y2, 1, ask)
        elif ask(x1, y1, x2 - 1, y2) == 1:
            a = shrink(x1, y1, x2 - 1, y2, 1, ask)
    if not a and y1 < y2:
        if ask(x1, y1 + 1, x2, y2) == 1:
            a = shrink(x1, y1 + 1, x2, y2, 1, ask)
        elif ask(x1, y1, x2, y2 - 1) == 1:
            a = shrink(x1, y1, x2, y2 - 1, 1, ask)
    if not a:
        a = (x1, y1, x2, y2)
        return a, a
    else:
        b = shrink(x1, y1, x2, y2, 1, ask, known=[a])
        return a, b

def generate_two_rectangles(n):
    """
    Generate two non-empty axis-aligned rectangles fully inside [0,n)×[0,n),
    each as (x1,y1,x2,y2) with x1<x2, y1<y2. They may overlap arbitrarily.
    """
    def gen_rect():
        x1 = random.randint(0, n - 1)
        x2 = random.randint(x1 + 1, n)
        y1 = random.randint(0, n - 1)
        y2 = random.randint(y1 + 1, n)
        return (x1, y1, x2, y2)

    a = gen_rect()
    b = gen_rect()
    return a, b

def main(n, seed=None):
    if seed is not None:
        random.seed(seed)
    # generate test data: two rectangles within [0,n)×[0,n)
    true_a, true_b = generate_two_rectangles(n)
    rects = [true_a, true_b]

    ask = ask_factory(rects)
    a, b = go(0, 0, n, n, ask)

    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    # original code outputs 1-based for (x1,y1) and keeps x2,y2 as-is
    print('True rectangles (0-based):', true_a, true_b)
    print('Recovered rectangles (0-based):', a, b)
    print('Output format (as original):',
          ax1 + 1, ay1 + 1, ax2, ay2,
          bx1 + 1, by1 + 1, bx2, by2)

if __name__ == "__main__":
    # example run with n = 10
    main(10, seed=0)