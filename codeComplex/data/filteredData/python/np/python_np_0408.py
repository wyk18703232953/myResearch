# -*- coding:utf-8 -*-

import random
from typing import List, Tuple


def check(val: int, A: List[List[int]], M: int) -> bool:
    s = set()
    for row in A:
        v = 0
        for u in row:
            v <<= 1
            if u >= val:
                v |= 1
        s.add(v)

    x = 1 << M
    for u in s:
        for v in range(x):
            if v in s and (u | v) == x - 1:
                return True

    return False


def getAnswer(val: int, A: List[List[int]], M: int) -> Tuple[int, int]:
    vi = {}
    for i, row in enumerate(A):
        v = 0
        for u in row:
            v <<= 1
            if u >= val:
                v |= 1
        vi[v] = i

    x = 1 << M
    for u in vi:
        for v in range(x):
            if v in vi and (u | v) == x - 1:
                return vi[u], vi[v]

    return 0, 0


def solve(N: int, M: int, A: List[List[int]]) -> Tuple[int, int]:
    lo, hi = 0, max(max(row) for row in A)

    while lo <= hi:
        m = (lo + hi) // 2
        if check(m, A, M):
            lo = m + 1
        else:
            hi = m - 1

    a, b = getAnswer(hi, A, M)
    # 返回 1-based 下标
    return a + 1, b + 1


def main(n: int) -> Tuple[int, int]:
    """
    n 为规模参数，用于控制测试数据大小。
    这里约定：
      - N = n
      - M = max(1, min(10, n))  列数不超过 10，且至少为 1
      - A 的元素为 [0, 10^9] 之间的随机整数
    """
    N = n
    M = max(1, min(10, n))  # 按需调整规则
    max_val = 10 ** 9

    random.seed(0)
    A = [[random.randint(0, max_val) for _ in range(M)] for _ in range(N)]

    return solve(N, M, A)


if __name__ == "__main__":
    # 示例：以 n=5 运行
    ans = main(5)
    print(ans[0], ans[1])