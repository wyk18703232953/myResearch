import math


def get_line(x1, y1, x2, y2):
    a = x2 - x1
    b = y1 - y2
    c = x1 * (y2 - y1) - y1 * (x2 - x1)

    g = math.gcd(math.gcd(a, b), c)
    a //= g
    b //= g
    c //= g
    return a, b, c


n = int(input())
xy = []

for i in range(n):
    x, y = [int(x) for x in input().split()]
    xy.append((x, y))

if n <= 3:
    print("YES")
    exit()


def check(x1, y1, x2, y2, xy):
    a1, b1, c1 = get_line(x1, y1, x2, y2)
    other_point = None
    cnt_other = 0
    a2, b2, c2 = 0, 0, 0
    for i in range(len(xy)):
        x, y = xy[i]

        if a1 * y + b1 * x + c1 != 0:
            if other_point is None:
                other_point = x, y
                cnt_other = 1
            elif cnt_other == 1:
                cnt_other = 2
                a2, b2, c2 = get_line(*other_point, x, y)
            else:
                if a2 * y + b2 * x + c2 != 0:
                    return False
    return True


if check(*xy[0], *xy[1], xy[2:]):
    print("YES")
elif check(*xy[1], *xy[2], [xy[0]] + xy[3:]):
    print("YES")
elif check(*xy[0], *xy[2], [xy[1]] + xy[3:]):
    print("YES")
else:
    print("NO")

