import math, string, itertools, fractions, heapq, collections, re, array, bisect, sys, random, time, copy, functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9 + 7
dd = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ddn = [
    (0, -1), (1, -1), (1, 0), (1, 1),
    (0, 1), (-1, -1), (-1, 0), (-1, 1)
]


def main(n):
    """
    n: 规模参数，用于生成测试数据 (x, k)。
       这里约定：
       - x 在 [0, 10^9]
       - k 在 [0, n]
    """

    random.seed(n)  # 保证同一 n 下测试数据可复现

    # 生成测试数据
    x = random.randint(0, 10**9)
    k = random.randint(0, n)

    if x == 0:
        return 0

    t = pow(2, k + 1, mod) * x % mod
    d = pow(2, k, mod) - 1

    return (t + mod - d) % mod


if __name__ == "__main__":
    # 示例：使用某个 n 调用 main，并打印结果
    n = 10
    print(main(n))