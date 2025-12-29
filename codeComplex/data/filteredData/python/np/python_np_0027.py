from collections import defaultdict, Counter, deque
from math import sqrt, log10, log, floor, factorial, gcd
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
import sys, io, os

inf = float('inf')
mod = 10 ** 9 + 7
ceil = lambda a, b: (a + b - 1) // b


class masks:
    def all_masks_sos(self, arr, lim=22):
        lim = 22
        maxbits = lim
        self.masks = masks_val = 1 << lim
        self.dp = [-1] * masks_val
        for i in arr:
            self.dp[i] = i
        for i in range(masks_val):
            for j in range(maxbits):
                if self.dp[i] == -1 and (i & (1 << j)):
                    self.dp[i] = self.dp[i - (1 << j)]


def main(n):
    """
    n: number of elements to generate as test data.
       Each element is an integer mask in [0, 2^22 - 1].
    """
    import random

    lim = 22
    max_mask = (1 << lim) - 1

    # 生成测试数据：n 个在 [0, 2^22 - 1] 范围内的整数
    l = [random.randint(0, max_mask) for _ in range(n)]

    m = masks()
    m.all_masks_sos(l, lim)

    ans = [m.dp[x ^ (m.masks - 1)] for x in l]
    print(*ans)


if __name__ == "__main__":
    # 示例：当作脚本执行时，用 n = 5 演示
    main(5)