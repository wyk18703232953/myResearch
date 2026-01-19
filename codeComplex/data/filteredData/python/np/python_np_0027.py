from collections import defaultdict, Counter, deque
from math import sqrt, log10, log, floor, factorial, gcd
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations

inf = float('inf')
mod = 10 ** 9 + 7
ceil = lambda a, b: (a + b - 1) // b


class masks:
    def all_masks_sos(self, arr, lim=22):
        lim = 22
        maxbits = lim
        self.masks = masks_val = 1 << lim
        self.dp = [-1] * masks_val
        for v in arr:
            if 0 <= v < masks_val:
                self.dp[v] = v
        for i in range(masks_val):
            for j in range(maxbits):
                if self.dp[i] == -1 and i & (1 << j):
                    self.dp[i] = self.dp[i - (1 << j)]


def main(n):
    if n <= 0:
        return
    lim = 22
    max_val = (1 << lim) - 1
    # deterministically generate n integers in [0, max_val]
    l = [((i * 1234567) + 890123) & max_val for i in range(n)]
    m = masks()
    m.all_masks_sos(l, lim)
    ans = [m.dp[x ^ (m.masks - 1)] for x in l]
    print(*ans)


if __name__ == "__main__":
    main(5)