# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import itertools
import sys
import random


def main(n):
    """
    n: 规模，用作查询个数 Q
    根据 n 生成 Q 组 [l, r] 测试数据，并输出对应答案
    """
    Q = n

    # 生成测试数据：
    # 这里简单生成 Q 组区间 [l, r]，其中 0 <= l <= r <= 2*n
    # 可根据需要调整数据生成策略
    queries = []
    for _ in range(Q):
        l = random.randint(0, 2 * n)
        r = random.randint(l, 2 * n)
        queries.append((l, r))

    ans = []

    for l, r in queries:
        if l % 2 == 0 and r % 2 == 0:
            ans.append((r - l) // 2 + l)
        elif l % 2 == 1 and r % 2 == 0:
            ans.append((r - l + 1) // 2)
        elif l % 2 == 1 and r % 2 == 1:
            ans.append(0 - (r - l) // 2 - l)
        else:
            ans.append(0 - (r - l + 1) // 2)

    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)