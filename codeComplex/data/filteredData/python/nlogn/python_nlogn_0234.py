import math
import random


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
    for x, y in xy:
        if a1 * y + b1 * x + c1 != 0:
            if other_point is None:
                other_point = (x, y)
                cnt_other = 1
            elif cnt_other == 1:
                cnt_other = 2
                a2, b2, c2 = get_line(*other_point, x, y)
            else:
                if a2 * y + b2 * x + c2 != 0:
                    return False
    return True


def main(n):
    # 生成规模为 n 的测试数据：n 个点，坐标在 [-10^6, 10^6] 范围内
    random.seed(0)
    xy = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        y = random.randint(-10**6, 10**6)
        xy.append((x, y))

    if n <= 3:
        print("YES")
        return

    if check(*xy[0], *xy[1], xy[2:]):
        print("YES")
    elif check(*xy[1], *xy[2], [xy[0]] + xy[3:]):
        print("YES")
    elif check(*xy[0], *xy[2], [xy[1]] + xy[3:]):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)