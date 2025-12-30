from collections import defaultdict, Counter, deque
from math import sqrt, log10, log, floor, factorial, gcd
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
import random

inf = float('inf')
mod = 10 ** 9 + 7
ceil = lambda a, b: (a + b - 1) // b

def main(n):
    # 生成测试数据：n 个整数，范围在 [0, 2^lim - 1]
    lim = 22
    po = [1 << j for j in range(lim + 1)]
    maxbits = lim
    masks = po[lim]

    # 限制 n 不超过 masks（原算法需要用到下标为 l[i] 的 dp[l[i]]）
    n = min(n, masks)

    # 生成 l：0 ~ masks-1 中的 n 个整数（可重复）
    l = [random.randrange(0, masks) for _ in range(n)]

    dp = [-1] * masks

    # 原逻辑开始
    for x in l:
        dp[x] = x
    for i in range(masks):
        for j in range(maxbits):
            if dp[i] == -1 and (i & (1 << j)):
                dp[i] = dp[i - (1 << j)]
    ans = [dp[x ^ (masks - 1)] for x in l]

    # 输出：先输出生成的数据，再输出结果
    print("n =", n)
    print("l:", *l)
    print("ans:", *ans)


# 示例调用（提交到评测时可删除或注释）
if __name__ == "__main__":
    main(10)