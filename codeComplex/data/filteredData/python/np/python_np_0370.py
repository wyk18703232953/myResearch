from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
import random

mod = 998244353
INF = float('inf')


def comb(n, m): 
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0


def perm(n, m): 
    return factorial(n) // (factorial(n - m)) if n >= m else 0


def mdis(x1, y1, x2, y2): 
    return abs(x1 - x2) + abs(y1 - y2)


def solve_single(n, m, arr):
    larr = [list(i) for i in zip(*arr)]
    larr.sort(key=lambda a: max(a), reverse=True)
    larr = larr[:n]

    res = 0

    def dfs(lst, pos=0):
        nonlocal res
        if pos == min(n, len(larr)):
            res = max(res, sum(lst))
            return

        for i in range(n):
            nex = lst.copy()
            for j in range(n):
                nex[(i + j) % n] = max(nex[(i + j) % n], larr[pos][j])
            dfs(nex, pos + 1)

    dfs([0] * n)
    return res


def main(scale_n: int):
    """
    scale_n: 控制测试规模的参数。
    这里设置:
        n = scale_n
        m = min(scale_n, 10) 保持可控
        数组元素为 [1, 100] 的随机整数。
    """
    random.seed(0)
    t = 1  # 测试组数，可根据需要调整为与 scale_n 相关
    results = []

    for _ in range(t):
        n = max(1, scale_n)
        m = max(1, min(scale_n, 10))
        arr = [[random.randint(1, 100) for _ in range(m)] for _ in range(n)]
        res = solve_single(n, m, arr)
        results.append(res)

    # 输出结果
    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：以 5 作为规模参数运行
    main(5)