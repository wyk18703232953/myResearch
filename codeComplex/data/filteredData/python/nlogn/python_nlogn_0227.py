from random import randint


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


def generate_test_data(n):
    # 生成 n 个点，坐标范围可根据需要调整
    # 这里简单使用 [-10^6, 10^6] 区间内的随机整数点
    xy_a = []
    for _ in range(n):
        x = randint(-10**6, 10**6)
        y = randint(-10**6, 10**6)
        xy_a.append([x, y])
    return xy_a


def main(n):
    xy_a = generate_test_data(n)
    res = pair_of_lines(n, xy_a)
    print(res)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)