from math import factorial
from collections import Counter, defaultdict
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
    """
    n 为原程序中的 n。
    这里根据规模 n 自动生成 k（例如 k 在 [1, n] 中随机取值）。
    也可以按需改成固定关系，如 k = n // 2 等。
    """
    if n < 1:
        print(0)
        return

    # 根据规模 n 生成测试数据 (n, k)
    # 示例：k 在 [1, n] 范围内随机生成
    k = random.randint(1, n)

    dp = [[0] * 4 for _ in range(k + 2)]
    dp[1][0] = 1
    dp[1][3] = 1
    if k + 1 >= 2:
        dp[2][1] = 1
        dp[2][2] = 1

    for i in range(2, n + 1):
        new = [[0] * 4 for _ in range(k + 2)]
        for j in range(1, k + 2):
            for l in range(4):
                new[j][l] += dp[j][l]
                if l == 0 or l == 3:
                    new[j][l] += dp[j - 1][l ^ 3]
                    new[j][l] += (dp[j][1] + dp[j][2])
                elif l == 1 or l == 2:
                    new[j][l] += (dp[j - 1][0] + dp[j - 1][3])
                    if j - 2 >= 0:
                        new[j][l] += dp[j - 2][l ^ 3]
                new[j][l] %= mod
        dp = new

    print(sum(dp[k]) % mod)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)