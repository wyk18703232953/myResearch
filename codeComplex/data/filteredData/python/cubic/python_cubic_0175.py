from collections import Counter, defaultdict
import math
import random
import heapq as hq
from math import sqrt
from functools import reduce

mod = int(1e9) + 7


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


def main(n):
    # 生成测试数据：长度为 n 的数组 a，元素为 1~5 之间的随机整数
    random.seed(0)
    a = [random.randint(1, 5) for _ in range(n)]

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]

    for l in range(n - 2, -1, -1):
        for r in range(l + 1, n):
            for k in range(l, r):
                if dp[l][k] == dp[k + 1][r] and dp[l][k] != 0:
                    dp[l][r] = dp[l][k] + 1

    squeeze = [float('inf')] * (n + 1)
    squeeze[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j][i - 1] != 0:
                squeeze[i] = min(squeeze[i], squeeze[j] + 1)

    print(squeeze[n])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)