import math
import itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify, nlargest
from copy import deepcopy

mod = 10**9 + 7
INF = float('inf')


def main(n):
    # 映射规模：n -> n 行, n 列的 01 矩阵
    # 生成一个确定性的 n x n 字符矩阵 s，每个元素为 '0' 或 '1'
    # 这里使用简单的算术构造 (i * n + j) % 2 来生成
    m = n
    s = []
    for i in range(n):
        row = [('1' if ((i * n + j) % 2 == 0) else '0') for j in range(m)]
        s.append(row)

    lampcnt = [0] * m
    for i in range(n):
        for j in range(m):
            if s[i][j] == '1':
                lampcnt[j] += 1

    res = False
    for i in range(n):
        only = False
        for j in range(m):
            if s[i][j] == '1' and lampcnt[j] == 1:
                only = True
        if not only:
            res = True

    # print('YES' if res else 'NO')
    pass
if __name__ == "__main__":
    # 示例调用，使用一个固定规模 n
    main(10)