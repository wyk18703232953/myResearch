def area(rect):
    if rect is None:
        return 0
    x1, y1, x2, y2 = rect
    return (x2 - x1 + 1) * (y2 - y1 + 1)


def get_w(rect):
    if rect is None:
        return 0
    x1, y1, x2, y2 = rect
    ra = area(rect)
    more, less = (ra + 1) // 2, ra // 2
    if (x1 + y1) % 2 == 0:
        return more

    else:
        return less


def intersect_rects(r1, r2):
    out = []
    for i, a, b in zip(range(4), r1, r2):
        out.append(max(a, b) if i < 2 else min(a, b))
    if out[0] > out[2] or out[1] > out[3]:
        return None
    return out


def main(n):
    q = n
    results = []
    for i in range(q):
        # 确定性生成 n_i, m_i
        ni = i + 2
        mi = n + i + 2

        # 确定性生成两个矩形 rect1, rect2，保证在 [1..ni] x [1..mi] 范围内
        x1_1 = 1
        y1_1 = 1
        x2_1 = max(1, ni // 2)
        y2_1 = max(1, mi // 2)
        rect1 = [x1_1, y1_1, x2_1, y2_1]

        x1_2 = (i % max(1, ni)) + 1
        y1_2 = ((2 * i) % max(1, mi)) + 1
        x2_2 = ni
        y2_2 = mi
        if x1_2 > x2_2:
            x1_2, x2_2 = x2_2, x1_2
        if y1_2 > y2_2:
            y1_2, y2_2 = y2_2, y1_2
        rect2 = [x1_2, y1_2, x2_2, y2_2]

        rect12 = intersect_rects(rect1, rect2)

        w_start = get_w([1, 1, ni, mi])
        w1 = get_w(rect1)
        w2 = get_w(rect2)
        w12 = get_w(rect12)

        w = w_start - w1 - w2 + w12 + area(rect1) - area(rect12)
        results.append((w, ni * mi - w))

    # 为了保持与原程序一致的输出形式，这里输出最后一组结果
    if results:
        last = results[-1]
        # print(last[0], last[1])
        pass
if __name__ == "__main__":
    main(10)