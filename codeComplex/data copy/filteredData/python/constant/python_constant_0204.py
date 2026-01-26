import math
import itertools
from collections import Counter, deque, defaultdict
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush, heapify
from copy import deepcopy

mod = 10**9 + 7
INF = float('inf')


def main(n):
    if n <= 0:
        k = []

    else:
        # 生成一个长度为 n 的整数列表，元素为 i % 5 + 1，确保可重复且有一定多样性
        k = [(i % 5) + 1 for i in range(n)]

    k.sort()
    if k.count(1) >= 1 or k.count(2) >= 2 or k.count(3) >= 3 or k == [2, 4, 4]:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例：使用 n = 10 作为输入规模
    main(10)