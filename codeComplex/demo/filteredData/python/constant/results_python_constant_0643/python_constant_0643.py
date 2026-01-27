import math
import collections
import bisect
import heapq
import time
import itertools
import sys


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
    # n controls the number of test cases and the scale of N, M
    if n <= 0:
        return

    T = n
    ans = []
    for ti in range(T):
        # Deterministic generation of N, M (grid size)
        N = 5 + (ti % max(1, n))  # at least 5
        M = 7 + ((ti * 2) % max(1, n))

        # Deterministic rectangles inside [1..N] x [1..M]
        # First rectangle a
        x1 = 1 + (ti * 3) % max(1, N // 2 + 1)
        y1 = 1 + (ti * 5) % max(1, M // 2 + 1)
        x2 = x1 + (1 + (ti % max(1, N - x1 + 1))) // 2
        y2 = y1 + (1 + ((ti * 7) % max(1, M - y1 + 1))) // 2
        if x2 > N:
            x2 = N
        if y2 > M:
            y2 = M

        # Second rectangle b
        x3 = 1 + (ti * 4) % max(1, N)
        y3 = 1 + (ti * 6) % max(1, M)
        x4 = x3 + (1 + ((ti * 3) % max(1, N - x3 + 1))) // 2
        y4 = y3 + (1 + ((ti * 2) % max(1, M - y3 + 1))) // 2
        if x4 > N:
            x4 = N
        if y4 > M:
            y4 = M

        w = winrect((1, 1, N, M))
        a = (x1, y1, x2, y2)
        b = (x3, y3, x4, y4)
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

    # print('\n'.join(['{} {}'.format(a, b) for a, b in ans]))
    pass
if __name__ == "__main__":
    main(10)