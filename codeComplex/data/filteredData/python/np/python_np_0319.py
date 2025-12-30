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
    # 根据规模 n 生成测试数据 (n, k)
    # 这里令 k 在 [1, n] 范围内随机，也可根据需要改成固定规则
    if n < 2:
        n = 2
    k = random.randint(1, n)

    dp = [[0] * 4 for _ in range(k + 2)]
    dp[1][0] = 1
    dp[1][3] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    tag = 0

    for i in range(2, n + 1):
        new = [[0] * 4 for _ in range(k + 2)]
        for j in range(1, k + 2):
            for l in range(4):
                tag += 1
                new[j][l] = (dp[j][l] % mod + new[j][l] % mod) % mod
                if l == 0 or l == 3:
                    new[j][l] = (dp[j - 1][l ^ 3] % mod + new[j][l] % mod) % mod
                    new[j][l] = ((dp[j][1] % mod + dp[j][2] % mod) + new[j][l] % mod) % mod
                elif l == 1 or l == 2:
                    new[j][l] = ((dp[j - 1][0] % mod + dp[j - 1][3] % mod) + new[j][l] % mod) % mod
                    if j - 2 >= 0:
                        new[j][l] = (dp[j - 2][l ^ 3] % mod + new[j][l] % mod) % mod
        dp = new

    ans = sum(dp[k]) % mod
    print(f"n={n}, k={k}, answer={ans}")
    return ans

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)