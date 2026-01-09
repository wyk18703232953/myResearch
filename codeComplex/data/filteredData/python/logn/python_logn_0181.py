def req(a, b, c, d, rectangles):
    ans = 0
    for x1, y1, x2, y2 in rectangles:
        if a <= x1 and b <= y1 and c >= x2 and d >= y2:
            ans += 1
    return ans


def bin_search(l, r, down, left, up, right, tp, tar, rectangles):
    while r - l > 1:
        m = (r + l) // 2

        if tp == 0:
            down = m
        if tp == 1:
            left = m
        if tp == 2:
            up = m
        if tp == 3:
            right = m

        if req(down, left, up, right, rectangles) == tar:
            l = m

        else:
            r = m
    return [l, r]


def find_rec(x1, y1, x2, y2, rectangles) -> list:
    up_ = bin_search(x1 - 1, x2 + 1, x1, y1, -2, y2, 2, 0, rectangles)[1]
    down_ = bin_search(x1 - 1, x2 + 1, -2, y1, x2, y2, 0, 1, rectangles)[0]
    left_ = bin_search(y1 - 1, y2 + 1, x1, -2, x2, y2, 1, 1, rectangles)[0]
    right_ = bin_search(left_ - 1, y2 + 1, x1, y1, x2, -2, 3, 0, rectangles)[1]
    return [down_, left_, up_, right_]


def generate_rectangles(n):
    # Deterministically generate two non-overlapping rectangles inside [1, n] x [1, n]
    # First rectangle roughly in top-left
    x1_1 = 1
    y1_1 = 1
    x2_1 = max(1, n // 3)
    y2_1 = max(1, n // 2)

    # Second rectangle roughly in bottom-right
    x2_2 = n
    y2_2 = n
    x1_2 = min(n, 2 * n // 3 + 1)
    y1_2 = min(n, n // 2 + 1)

    # Ensure coordinates are valid rectangles
    if x2_1 < x1_1:
        x2_1 = x1_1
    if y2_1 < y1_1:
        y2_1 = y1_1
    if x2_2 < x1_2:
        x1_2 = x2_2
    if y2_2 < y1_2:
        y1_2 = y2_2

    return [(x1_1, y1_1, x2_1, y2_1), (x1_2, y1_2, x2_2, y2_2)]


def main(n):
    rectangles = generate_rectangles(n)

    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r) // 2
        if req(1, 1, m, n, rectangles) == 0:
            l = m

        else:
            r = m

    rec = []

    if r != n and req(r + 1, 1, n, n, rectangles) == 1:
        rec.append(find_rec(1, 1, r, n, rectangles))
        rec.append(find_rec(r + 1, 1, n, n, rectangles))

    else:
        l = 0
        r = n + 1
        while r - l > 1:
            m = (l + r) // 2
            if req(1, 1, n, m, rectangles) == 0:
                l = m

            else:
                r = m
        rec.append(find_rec(1, 1, n, r, rectangles))
        rec.append(find_rec(1, r + 1, n, n, rectangles))

    # print('!', *rec[0], *rec[1])
    pass
if __name__ == "__main__":
    main(10)