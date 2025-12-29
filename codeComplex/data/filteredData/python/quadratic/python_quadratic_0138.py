import sys
import math
import itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify, nlargest
from copy import deepcopy

mod = 10 ** 9 + 7
INF = float('inf')


def main(n):
    # 生成测试数据：4 个 n×n 的 01 棋盘
    # 这里构造一个可重复测试的模式：第 k 个棋盘为 (i+j+k) % 2
    s = []
    for k in range(4):
        board = []
        for i in range(n):
            row = ''.join(str((i + j + k) % 2) for j in range(n))
            board.append(row)
        s.append(board)

    res = INF
    # 在 4 个棋盘中任选两个做“翻转起点”（原逻辑）
    for pt in itertools.combinations(range(4), 2):
        cnt = 0
        for k in range(4):
            f = 1 if k in pt else 0
            for i in range(n):
                for j in range(n):
                    if (i + j + f) % 2 != int(s[k][i][j]):
                        cnt += 1
        res = min(res, cnt)
    print(res)


if __name__ == "__main__":
    # 示例：规模为 4，可按需修改或在外部调用 main(n)
    main(4)