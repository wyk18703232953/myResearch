import sys, math, itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify, nlargest
from copy import deepcopy

mod = 10**9 + 7
INF = float('inf')


def main(n):
    # 映射规模：构造一个近似平方的矩阵 n = rows * cols
    if n <= 0:
        # print('NO')
        pass
        return

    rows = int(n ** 0.5)
    if rows == 0:
        rows = 1
    cols = (n + rows - 1) // rows  # 向上取整，保证 rows * cols >= n

    # 构造确定性的 0/1 矩阵 s，大小为 rows x cols
    # 规则：位置 (i, j) 是 '1' 当且仅当 (i * cols + j) % 3 == 0
    # 最后一行多出的元素也按同一规则填充
    s = []
    for i in range(rows):
        row = []
        for j in range(cols):
            idx = i * cols + j
            if idx < n and idx % 3 == 0:
                row.append('1')

            else:
                row.append('0')
        s.append(row)

    n_rows = rows
    m_cols = cols

    lampcnt = [0] * m_cols
    for i in range(n_rows):
        for j in range(m_cols):
            if s[i][j] == '1':
                lampcnt[j] += 1

    res = False
    for i in range(n_rows):
        only = False
        for j in range(m_cols):
            if s[i][j] == '1' and lampcnt[j] == 1:
                only = True
        if not only:
            res = True

    # print('YES' if res else 'NO')
    pass
if __name__ == "__main__":
    # 示例调用：可以修改 n 以改变输入规模
    main(1000)