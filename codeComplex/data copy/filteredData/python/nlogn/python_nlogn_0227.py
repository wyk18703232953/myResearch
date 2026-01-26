def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def kstr(xy1, xy2):
    cx, cy = xy1[0], xy1[1]
    x, y = xy2[0], xy2[1]
    dx = x - cx
    dy = y - cy
    if dx == 0:
        return str(x) + '/y'
    elif dy == 0:
        return 'x/' + str(y)

    else:
        g = gcd(dx, dy)
        dx //= g
        dy //= g
        return str(dx) + '/' + str(dy)


def judge(p, k, xy_a):
    rl = []
    for xy in xy_a:
        if p[0] == xy[0] and p[1] == xy[1]:
            continue
        if kstr(p, xy) != k:
            rl.append(xy)

    if len(rl) > 2:
        ck = kstr(rl[0], rl[1])
        for i in range(2, len(rl)):
            if ck != kstr(rl[0], rl[i]):
                return False

    return True


def pair_of_lines(n, xy_a):
    if len(xy_a) <= 3:
        return 'YES'

    p1, p2, p3 = xy_a[0], xy_a[1], xy_a[2]
    if judge(p1, kstr(p1, p2), xy_a):
        return 'YES'
    if judge(p1, kstr(p1, p3), xy_a):
        return 'YES'
    if judge(p2, kstr(p2, p3), xy_a):
        return 'YES'
    return 'NO'


def generate_points(n):
    # 生成 n 个确定性的整数点 (x, y)
    # 这里选择一种简单的构造：x = i, y = i % 5
    # 可保证随 n 线性扩展
    points = []
    for i in range(n):
        x = i
        y = (i * 2 + 3) % 7
        points.append([x, y])
    return points


def main(n):
    # n 表示点的数量
    if n <= 0:
        # print('YES')
        pass
        return
    xy_a = generate_points(n)
    res = pair_of_lines(n, xy_a)
    # print(res)
    pass
if __name__ == "__main__":
    main(10)