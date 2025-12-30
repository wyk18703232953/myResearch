import random

import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, time, copy, functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


def main(n):
    """
    n: 规模参数，用于控制测试数据大小。
       这里将生成 q = n 组询问，每个棋盘大小和矩形随机生成，
       棋盘大小不超过 n。
    """

    def f(a, b, c, d):
        if a > c or b > d:
            return (0, 0)
        sa = c - a + 1
        sb = d - b + 1
        g = h = (sa * sb) // 2
        if (sa * sb) % 2 == 1:
            g += 1
        if (a + b) % 2 == 0:
            return (g, h)
        return (h, g)

    def fa(a):
        return f(a[0], a[1], a[2], a[3])

    # 生成测试数据：q 组询问
    q = n
    rr = []

    for _ in range(q):
        # 棋盘大小 [1, n] x [1, m]，这里令 m 也在 [1, n]
        N = random.randint(1, n)
        M = random.randint(1, n)

        # 生成两个矩形 [x1,y1,x2,y2]，保证在棋盘内，且 x1<=x2, y1<=y2
        def gen_rect():
            x1 = random.randint(1, N)
            x2 = random.randint(x1, N)
            y1 = random.randint(1, M)
            y2 = random.randint(y1, M)
            return [x1, y1, x2, y2]

        wa = gen_rect()
        ba = gen_rect()

        wc, bc = f(1, 1, N, M)
        w1, b1 = fa(wa)
        w2, b2 = fa(ba)
        w3, b3 = f(
            max(wa[0], ba[0]),
            max(wa[1], ba[1]),
            min(wa[2], ba[2]),
            min(wa[3], ba[3]),
        )

        wc += b1
        bc -= b1
        wc -= w2
        bc += w2
        wc -= b3
        bc += b3
        rr.append(f"{wc} {bc}")

    return "\n".join(rr)


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    print(main(10))