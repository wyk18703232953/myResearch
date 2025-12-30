import random

class vec:
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


def main(n):
    # 使用 n 控制坐标随机范围：[-n, n]
    coord_min, coord_max = -n, n

    def gen_point():
        return random.randint(coord_min, coord_max), random.randint(coord_min, coord_max)

    # 生成两组四个点
    ax, ay = gen_point()
    bx, by = gen_point()
    cx, cy = gen_point()
    dx, dy = gen_point()

    kx, ky = gen_point()
    lx, ly = gen_point()
    mx, my = gen_point()
    nx, ny = gen_point()

    # 原始逻辑
    c, b, d, a = map(vec, sorted([(ax, ay), (bx, by), (cx, cy), (dx, dy)]))
    m, n_vec, l, k = map(vec, sorted([(kx, ky), (lx, ly), (mx, my), (nx, ny)]))

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

    print('YES' if res else 'NO')


if __name__ == "__main__":
    # 示例：n = 10
    main(10)