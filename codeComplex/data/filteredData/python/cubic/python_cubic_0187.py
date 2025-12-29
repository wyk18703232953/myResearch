from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush
import random

mod = 998244353
INF = float('inf')

def comb(n, m): 
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0

def perm(n, m): 
    return factorial(n) // (factorial(n - m)) if n >= m else 0

def mdis(x1, y1, x2, y2): 
    return abs(x1 - x2) + abs(y1 - y2)


def main(n):
    # 生成规模为 n 的测试数据：arr 为长度为 n 的正整数数组
    # 这里生成 1~3 的随机整数，可根据需要修改范围或生成方式
    random.seed(0)
    arr = [random.randint(1, 3) for _ in range(n)]

    dp = [[n] * n for _ in range(n)]
    rec = [[0] * n for _ in range(n)]

    for i in range(n):
        rec[i][i] = arr[i]
        dp[i][i] = 1

    for le in range(2, n + 1):
        for l in range(n):
            r = l + le - 1
            if r > n - 1:
                break
            for m in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][m] + dp[m + 1][r])
                if rec[l][m] == rec[m + 1][r] and dp[l][m] == dp[m + 1][r] == 1:
                    dp[l][r] = 1
                    rec[l][r] = rec[l][m] + 1

    print(dp[0][-1])


if __name__ == "__main__":
    # 示例调用：可修改 n 测试不同规模
    main(5)