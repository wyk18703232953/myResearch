import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def main(n):
    # 生成测试数据：n 对区间 [a, b]
    # 这里示例生成方式：a, b 为正整数，且 a <= b
    # 你可以根据需要修改下面的生成策略
    random.seed(0)
    aa = []
    for _ in range(n):
        a = random.randint(1, 10**6)
        b = random.randint(a, a + random.randint(0, 10**6))
        aa.append((a, b))

    r = []
    for a, b in aa:
        al = a + (1 - a % 2)
        ar = b - (1 - b % 2)
        if ar >= al:
            sa = (ar - al) // 2 + 1
            tr = -(al + ar) * sa // 2
        else:
            tr = 0

        bl = a + (a % 2)
        br = b - (b % 2)
        if br >= bl:
            sb = (br - bl) // 2 + 1
            tr += (bl + br) * sb // 2

        r.append(tr)

    # 输出
    print("\n".join(map(str, r)))


if __name__ == "__main__":
    # 示例调用：规模 n 自行指定
    main(5)