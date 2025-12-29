# -*- coding: utf-8 -*-

import random


def interact(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    ans = (-1, -1, -1, -1)
    if x2 < x3 or x4 < x1:
        return 0, ans
    if y2 < y3 or y4 < y1:
        return 0, ans

    ans = (max(x1, x3), max(y1, y3), min(x2, x4), min(y2, y4))

    return area(ans), ans


def area(rect):
    return (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)


def winrect(rect):
    a = area(rect)
    if a % 2 == 0:
        return a // 2

    x1, y1, x2, y2 = rect
    e1, e2 = x1 % 2 == 0, y1 % 2 == 0
    ow = (e1 and e2) or (not e1 and not e2)
    return a // 2 + 1 if ow else a // 2


def main(n):
    """
    n: 规模，用作测试数据的数量 T。
       对于每个测试：
         - N, M 在 [1, n]
         - 在 N x M 网格内随机生成两个矩形 a, b
    """
    T = n
    ans = []

    for _ in range(T):
        # 随机生成棋盘大小
        N = random.randint(1, n)
        M = random.randint(1, n)

        # 随机生成矩形 a
        x1 = random.randint(1, N)
        x2 = random.randint(x1, N)
        y1 = random.randint(1, M)
        y2 = random.randint(y1, M)
        a = (x1, y1, x2, y2)

        # 随机生成矩形 b
        x3 = random.randint(1, N)
        x4 = random.randint(x3, N)
        y3 = random.randint(1, M)
        y4 = random.randint(y3, M)
        b = (x3, y3, x4, y4)

        w = winrect((1, 1, N, M))
        s, c = interact(a, b)

        if s == 0:
            w -= winrect(a) + winrect(b)
            w += area(a)
        elif s == area(a):
            w -= winrect(b)
        elif s == area(b):
            w -= winrect(b)
            w += area(a) - area(b) - (winrect(a) - winrect(b))
        else:
            w += area(a) - winrect(a)
            w -= winrect(b)
            w -= area(c) - winrect(c)

        ans.append((w, N * M - w))

    print('\n'.join(['{} {}'.format(a, b) for a, b in ans]))


if __name__ == "__main__":
    # 示例：生成规模为 5 的测试数据
    main(5)