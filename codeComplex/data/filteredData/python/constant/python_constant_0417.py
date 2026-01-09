def main(n):
    class vec():
        def __init__(self, x, y=None):
            if y is None:
                x, y = x
            self.x = x
            self.y = y
        def __mod__(self, other):
            return self.x * other.y - self.y * other.x
        def __sub__(self, other):
            return vec(self.x - other.x, self.y - other.y)
        def __repr__(self):
            return 'vec({}, {})'.format(self.x, self.y)

    def lines_cross(a, b, c, d):
        ab, ac, ad = b - a, c - a, d - a
        cd, ca, cb = d - c, a - c, b - c
        return (ab % ac) * (ab % ad) <= 0 and (cd % ca) * (cd % cb) <= 0

    def rot(a):
        return vec(a.x - a.y, a.x + a.y)

    # 确定性数据生成：n 控制坐标的规模和分布
    # 生成 8 个点的坐标：ax, ay, ..., nx, ny
    # 使用简单算术表达式，确保相同 n 下结果稳定
    ax = n
    ay = 2 * n + 1
    bx = n + 3
    by = 3 * n + 1
    cx = 2 * n + 1
    cy = n + 2
    dx = 3 * n + 2
    dy = 2 * n

    kx = n // 2 + 1
    ky = n // 3 + 2
    lx = n // 2 + 4
    ly = n // 3 + 5
    mx = n // 2 + 2
    my = n // 3 + 7
    nx_ = n // 2 + 6
    ny_ = n // 3 + 1

    c, b, d, a = map(vec, sorted([(ax, ay), (bx, by), (cx, cy), (dx, dy)]))
    m, n_vec, l, k = map(vec, sorted([(kx, ky), (lx, ly), (mx, my), (nx_, ny_)]))
    res = False
    s1 = [a, b, c, d]
    s2 = [k, l, m, n_vec]
    for i in range(4):
        for j in range(4):
            if lines_cross(s1[i], s1[(i + 1) % 4], s2[j], s2[(j + 1) % 4]):
                res = True
                break
        if res:
            break
    if all([b.x <= p.x <= a.x and c.y <= p.y <= b.y for p in [k, l, m, n_vec]]):
        res = True
    if all([rot(l).x <= rot(p).x <= rot(k).x and rot(m).y <= rot(p).y <= rot(l).y for p in [a, b, c, d]]):
        res = True
    # print('YES' if res else 'NO')
    pass
if __name__ == "__main__":
    main(10)