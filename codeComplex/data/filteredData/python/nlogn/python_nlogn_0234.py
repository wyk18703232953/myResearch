import math


def get_line(x1, y1, x2, y2):
    a = x2 - x1
    b = y1 - y2
    c = x1 * (y2 - y1) - y1 * (x2 - x1)
    g = math.gcd(math.gcd(a, b), c)
    if g != 0:
        a //= g
        b //= g
        c //= g
    return a, b, c


def check(x1, y1, x2, y2, xy):
    a1, b1, c1 = get_line(x1, y1, x2, y2)
    other_point = None
    cnt_other = 0
    a2, b2, c2 = 0, 0, 0
    for i in range(len(xy)):
        x, y = xy[i]
        if a1 * y + b1 * x + c1 != 0:
            if other_point is None:
                other_point = (x, y)
                cnt_other = 1
            elif cnt_other == 1:
                cnt_other = 2
                a2, b2, c2 = get_line(other_point[0], other_point[1], x, y)
            else:
                if a2 * y + b2 * x + c2 != 0:
                    return False
    return True


def main(n):
    if n <= 0:
        print("YES")
        return

    # 生成确定性的点集 xy，规模为 n
    xy = []
    for i in range(n):
        x = i
        y = (i * i + 3 * i) % (n + 7)
        xy.append((x, y))

    if n <= 3:
        print("YES")
        return

    if check(xy[0][0], xy[0][1], xy[1][0], xy[1][1], xy[2:]):
        print("YES")
    elif check(xy[1][0], xy[1][1], xy[2][0], xy[2][1], [xy[0]] + xy[3:]):
        print("YES")
    elif check(xy[0][0], xy[0][1], xy[2][0], xy[2][1], [xy[1]] + xy[3:]):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)