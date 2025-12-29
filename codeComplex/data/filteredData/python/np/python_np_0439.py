from math import factorial
from collections import Counter, defaultdict
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

def main(n: int):
    # 根据规模 n 生成测试数据
    # 将原来的 n, m 合并为：n 行，m = n 列，元素为 [0, 1e9] 区间的随机整数
    m = n
    max_val = 10**9
    random.seed(0)
    arr = [[random.randint(0, max_val) for _ in range(m)] for _ in range(n)]

    res = []

    def c(num):
        nonlocal res
        dic = {}
        for i in range(n):
            now = 0
            for j in range(m):
                if arr[i][j] >= num:
                    now |= 1 << j
            dic[now] = i + 1

        full = (1 << m) - 1
        for k, v in dic.items():
            for kk, vv in dic.items():
                if k | kk == full:
                    res = [v, vv]
                    return True
        return False

    l, r = 0, max_val
    while l <= r:
        mp = (l + r + 1) // 2
        if c(mp):
            l = mp + 1
        else:
            r = mp - 1

    print(*res)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)