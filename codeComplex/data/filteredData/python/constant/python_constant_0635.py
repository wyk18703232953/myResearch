import random

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


def solve_one(n, m, rect1, rect2):
    rect12 = intersect_rects(rect1, rect2)

    w_start = get_w([1, 1, n, m])
    w1 = get_w(rect1)
    w2 = get_w(rect2)
    w12 = get_w(rect12)

    w = w_start - w1 - w2 + w12 + area(rect1) - area(rect12)
    return w, n * m - w


def main(n, q=1, seed=None):
    """
    n: 棋盘高，宽也设为 n（生成 n×n 棋盘）
    q: 生成的测试组数
    seed: 随机种子，便于复现
    """
    if seed is not None:
        random.seed(seed)

    m = n
    for _ in range(q):
        # 生成两个随机矩形 rect1, rect2，保证 1 <= x1 <= x2 <= n, 1 <= y1 <= y2 <= m
        def gen_rect():
            x1 = random.randint(1, n)
            x2 = random.randint(x1, n)
            y1 = random.randint(1, m)
            y2 = random.randint(y1, m)
            return [x1, y1, x2, y2]

        rect1 = gen_rect()
        rect2 = gen_rect()

        w, b = solve_one(n, m, rect1, rect2)
        print(w, b)


if __name__ == "__main__":
    # 示例：n=8，q=3
    main(8, q=3, seed=42)