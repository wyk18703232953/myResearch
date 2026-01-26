def contain(a, b):
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    return bx1 <= ax1 and ax2 <= bx2 and by1 <= ay1 and ay2 <= by2

def ask(x1, y1, x2, y2, known=(), memo=None):
    if memo is None:
        memo = {}
    if x2 < x1+1 or y2 < y1+1:
        return 0
    ofs = len([rect for rect in known if contain(rect, (x1, y1, x2, y2))])
    key = (x1+1, y1+1, x2, y2)
    if key in memo:
        return memo[key] - ofs
    # Deterministic oracle: two fixed rectangles inside [0,n]x[0,n]
    global RECT1, RECT2
    x1q, y1q, x2q, y2q = key
    def intersect_area(r, q):
        rx1, ry1, rx2, ry2 = r
        qx1, qy1, qx2, qy2 = q
        ix1 = max(rx1, qx1-1)
        iy1 = max(ry1, qy1-1)
        ix2 = min(rx2, qx2)
        iy2 = min(ry2, qy2)
        if ix1 >= ix2 or iy1 >= iy2:
            return 0
        return 1
    cnt = intersect_area(RECT1, (x1, y1, x2, y2)) + intersect_area(RECT2, (x1, y1, x2, y2))
    memo[key] = cnt
    return memo[key] - ofs

def binsearch(l, r, p):  # (l,r], return the smallest n which p holds
    assert l < r
    while l+1 != r:
        m = (l + r) // 2
        if p(m):
            r = m

        else:
            l = m
    return r

def shrink(x1, y1, x2, y2, cnt, known=(), memo=None):
    if memo is None:
        memo = {}
    assert ask(x1, y1, x2, y2, known=known, memo=memo) == cnt
    x1 = binsearch(x1, x2, lambda x: ask(x, y1, x2, y2, known=known, memo=memo) != cnt) - 1
    y1 = binsearch(y1, y2, lambda y: ask(x1, y, x2, y2, known=known, memo=memo) != cnt) - 1
    x2 = binsearch(x1, x2, lambda x: ask(x1, y1, x, y2, known=known, memo=memo) == cnt)
    y2 = binsearch(y1, y2, lambda y: ask(x1, y1, x2, y, known=known, memo=memo) == cnt)
    assert ask(x1, y1, x2, y2, known=known, memo=memo) == cnt
    assert ask(x1, y1, x2, y2, known=known, memo=memo) == cnt
    return x1, y1, x2, y2

def go(x1, y1, x2, y2):
    memo = {}
    assert ask(x1, y1, x2, y2, memo=memo) == 2
    x1, y1, x2, y2 = shrink(x1, y1, x2, y2, 2, memo=memo)
    a = None
    if not a and x1 < x2:
        if ask(x1+1, y1, x2, y2, memo=memo) == 1:
            a = shrink(x1+1, y1, x2, y2, 1, memo=memo)
        elif ask(x1, y1, x2-1, y2, memo=memo) == 1:
            a = shrink(x1, y1, x2-1, y2, 1, memo=memo)
    if not a and y1 < y2:
        if ask(x1, y1+1, x2, y2, memo=memo) == 1:
            a = shrink(x1, y1+1, x2, y2, 1, memo=memo)
        elif ask(x1, y1, x2, y2-1, memo=memo) == 1:
            a = shrink(x1, y1, x2, y2-1, 1, memo=memo)
    if not a:
        a = (x1, y1, x2, y2)
        return a, a

    else:
        b = shrink(x1, y1, x2, y2, 1, known=[a], memo=memo)
        return a, b

def build_rectangles(n):
    # Build two deterministic non-overlapping rectangles inside [0,n]x[0,n]
    # Rectangles are [x1,x2)×[y1,y2)
    x_mid = n // 2
    rect1 = (1, 1, max(2, x_mid), max(2, n//3 + 1))
    rect2 = (max(x_mid, 2), max(n//2, 2), max(x_mid+2, min(n, x_mid+4)), min(n, max(n//2+2, 4)))
    return rect1, rect2

def main(n):
    global RECT1, RECT2
    RECT1, RECT2 = build_rectangles(n)
    a, b = go(0, 0, n, n)
    ax1, ay1, ax2, ay2 = a
    bx1, by1, bx2, by2 = b
    # print(ax1+1, ay1+1, ax2, ay2, bx1+1, by1+1, bx2, by2)
    pass
if __name__ == "__main__":
    main(1000)