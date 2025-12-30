import bisect
import collections
import copy
import functools
import heapq
import itertools
import math
import sys
import string
import random
from typing import List

sys.setrecursionlimit(99999)


def main(n: int):
    # 生成参数
    # k 在 [0, 10] 范围内任选一个
    k = random.randint(0, 10)
    # 生成长度为 n 的数组，元素在 [0, 20] 范围内
    arr = [random.randint(0, 20) for _ in range(n)]

    cs = collections.Counter(arr)
    ks = list(cs.keys())
    ks.sort()
    ans = 0
    for i in range(1, len(ks)):
        if ks[i] <= ks[i - 1] + k:
            continue
        else:
            ans += cs[ks[i - 1]]
    ans += cs[ks[-1]]
    print(ans)


if __name__ == "__main__":
    # 示例：可以在这里指定规模 n
    main(10)