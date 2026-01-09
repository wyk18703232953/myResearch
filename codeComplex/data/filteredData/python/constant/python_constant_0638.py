def get_colors(x1, y1, x2, y2):
    w = x2 - x1 + 1
    h = y2 - y1 + 1
    if w % 2 == 0 or h % 2 == 0:
        black = w * h // 2
        white = w * h // 2

    else:
        oddx = w // 2
        if x1 % 2 == 1 and x2 % 2 == 1:
            oddx += 1
        oddy = h // 2
        if y1 % 2 == 1 and y2 % 2 == 1:
            oddy += 1
        evenx = w // 2
        if x1 % 2 == 0 and x2 % 2 == 0:
            evenx += 1
        eveny = h // 2
        if y1 % 2 == 0 and y2 % 2 == 0:
            eveny += 1
        white = oddx * oddy + evenx * eveny
        black = w * h - white
    return white, black

def get_intersection(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if ax1 > bx2:
        return None, None, None, None
    if bx1 > ax2:
        return None, None, None, None
    if ay1 > by2:
        return None, None, None, None
    if by1 > ay2:
        return None, None, None, None
    return max(ax1, bx1), max(ay1, by1), min(ax2, bx2), min(ay2, by2)

def main(n):
    # n 控制测试用例数量和棋盘规模、矩形规模
    t = n
    results = []
    for i in range(t):
        # 棋盘大小随 n 和用例编号变化，保证确定性和可规模化
        rows = n + i + 1
        cols = n + 2 * i + 2

        white, black = get_colors(1, 1, cols, rows)

        # 构造第一个矩形 (白色涂色矩形)
        wx1 = 1 + (i % max(1, cols // 3))
        wy1 = 1 + (i % max(1, rows // 3))
        wx2 = min(cols, wx1 + max(1, cols // 2))
        wy2 = min(rows, wy1 + max(1, rows // 2))

        w, b = get_colors(wx1, wy1, wx2, wy2)
        white += b
        black -= b

        # 构造第二个矩形 (黑色涂色矩形)
        bx1 = 1 + ((i * 2) % max(1, cols // 3))
        by1 = 1 + ((i * 2) % max(1, rows // 3))
        bx2 = min(cols, bx1 + max(1, cols // 2))
        by2 = min(rows, by1 + max(1, rows // 2))

        ix1, iy1, ix2, iy2 = get_intersection(wx1, wy1, wx2, wy2, bx1, by1, bx2, by2)
        if ix1 is not None:
            w_int, b_int = get_colors(ix1, iy1, ix2, iy2)
            white -= b_int
            black += b_int

        w_b, b_b = get_colors(bx1, by1, bx2, by2)
        white -= w_b
        black += w_b

        results.append((white, black))

    for w, b in results:
        # print(w, b)
        pass
if __name__ == "__main__":
    main(10)