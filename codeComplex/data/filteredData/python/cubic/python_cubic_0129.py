import math
import collections
import bisect
import heapq
import time
import itertools
import sys
from typing import List


def check(s, a, b, after):
    ns, na, nb = len(s), len(a), len(b)
    if ns < na + nb:
        return False

    dp = [[0 for _ in range(nb+1)] for _ in range(na+1)]
    for i in range(na+1):
        for j in range(nb+1):
            if i == 0 and j == 0:
                continue
            dp[i][j] = min(after[dp[i-1][j]][a[i-1]] if i > 0 else ns,
                           after[dp[i][j-1]][b[j-1]] if j > 0 else ns) + 1

    return dp[na][nb] <= ns


def solve(s, t):
    ns = len(s)
    after = [[ns for _ in range(26)] for _ in range(ns+2)]
    for i in range(ns-1, -1, -1):
        for j in range(26):
            after[i][j] = after[i+1][j]
        after[i][s[i]] = i

    for i in range(len(t)):
        a, b = t[:i], t[i:]
        if check(s, a, b, after):
            return 'YES'

    return 'NO'


def main(n):
    # n 作为规模参数：构造 T 个测试用例，每个用例中
    # |s| = n，|t| = n
    T = n
    answers = []

    for case_id in range(T):
        # 构造确定性的 s 和 t
        # s: 长度 n，字符依次为 (i + case_id) % 26
        s = [(i + case_id) % 26 for i in range(n)]
        # t: 长度 n，字符依次为 (i * 2 + case_id) % 26
        t = [(i * 2 + case_id) % 26 for i in range(n)]
        res = solve(s, t)
        answers.append(res)

    # 为了保持与原程序类似的行为，这里打印全部结果
    # print("\n".join(answers))
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 规模
    main(10)