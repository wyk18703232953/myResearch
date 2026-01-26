import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, copy, functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
mod2 = 998244353
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def JA(a, sep):
    return sep.join(map(str, a))


def main(n):
    # 生成测试数据：n, k
    # 原代码逻辑是寻找满足 t - (n - i) == k 的 n - i
    # 这里简单令 k = n // 2（可按需要调整生成规则）
    k = n // 2

    t = 0
    rr = []
    for i in range(1, 10 ** 5):
        t += i
        if t - (n - i) == k:
            rr.append(n - i)
            break

    return JA(rr, "\n")


if __name__ == "__main__":
    # 示例：用 n = 100 运行一次
    # print(main(100))
    pass