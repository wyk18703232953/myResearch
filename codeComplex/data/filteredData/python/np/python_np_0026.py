from collections import defaultdict, Counter, deque
from math import sqrt, log10, log, floor, factorial, gcd
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations
import random

inf = float('inf')
mod = 10 ** 9 + 7
ceil = lambda a, b: (a + b - 1) // b

# 原代码中使用的全局配置
lim = 22
po = [1 << j for j in range(lim + 1)]
maxbits = lim
masks = po[lim]          # 2^22
# dp 数组维度为 2^22，约 419 万，注意内存占用
dp = [-1] * masks


def main(n):
    """
    n: 规模，用作生成长度为 n 的测试数组 l
    自动生成测试数据并执行原逻辑：
    - 生成长度为 n 的数组 l，元素在 [0, 2^22 - 1] 范围内
    - 对 l 中每个元素 v，输出 dp[(2^22 - 1) ^ v]
    """

    # 生成测试数据：长度 n，每个数在 [0, masks-1]
    random.seed(0)
    l = [random.randrange(0, masks) for _ in range(n)]

    # 初始化 dp
    for i in l:
        dp[i] = i

    # 按位补全 dp
    for i in range(masks):
        for j in range(maxbits):
            if dp[i] == -1 and (i & po[j]):
                dp[i] = dp[i - po[j]]

    ans = [dp[i ^ (masks - 1)] for i in l]
    print(*ans)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)