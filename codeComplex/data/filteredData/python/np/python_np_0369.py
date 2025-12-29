from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
import random

def comb(n, m): 
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0

def perm(n, m): 
    return factorial(n) // (factorial(n - m)) if n >= m else 0

def mdis(x1, y1, x2, y2): 
    return abs(x1 - x2) + abs(y1 - y2)

mod = 998244353
INF = float('inf')

def solve_single_case(arr, n, m):
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
            now = larr[pos][i:n] + larr[pos][0:i]
            nex = [max(now[j], lst[j]) for j in range(n)]
            dfs(nex, pos + 1)

    dfs([0] * n)
    return res

def main(n):
    """
    n: 规模参数，用于生成测试数据。
       本函数将生成若干测试用例并输出结果。
    测试数据生成规则：
      - 设测试组数 T = 3（可根据需要修改）
      - 对于每组：
          n_rows = n
          m_cols = n
          arr 为 n_rows x m_cols 的矩阵，元素为 [0, 10^9) 内的随机整数
    """
    random.seed(0)

    T = 3
    results = []
    for _ in range(T):
        n_rows = n
        m_cols = n
        arr = [[random.randint(0, 10**9) for _ in range(m_cols)] for _ in range(n_rows)]
        res = solve_single_case(arr, n_rows, m_cols)
        results.append(res)

    for r in results:
        print(r)

if __name__ == "__main__":
    # 示例：以 n = 5 作为规模运行
    main(5)