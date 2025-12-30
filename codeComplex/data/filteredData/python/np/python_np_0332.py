import math, sys, bisect, heapq
from collections import defaultdict, Counter, deque
from itertools import groupby, accumulate

MOD = 998244353

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def solve(N, K):
    if K == 1 or K == 2 * N:
        return 2

    dp = list3d(N + 1, 4, K + 1, 0)
    dp[1][0][1] = 1
    dp[1][3][1] = 1
    dp[1][1][2] = 1
    dp[1][2][2] = 1

    for n in range(2, N + 1):
        for k in range(1, K + 1):
            dp[n][0][k] = (
                (dp[n - 1][0][k] + dp[n - 1][1][k]) % MOD +
                (dp[n - 1][2][k] + dp[n - 1][3][k - 1]) % MOD
            ) % MOD

            dp[n][3][k] = (
                (dp[n - 1][0][k - 1] + dp[n - 1][1][k]) % MOD +
                (dp[n - 1][2][k] + dp[n - 1][3][k]) % MOD
            ) % MOD

            if k > 1:
                dp[n][1][k] = (
                    (dp[n - 1][0][k - 1] + dp[n - 1][1][k]) % MOD +
                    (dp[n - 1][2][k - 2] + dp[n - 1][3][k - 1]) % MOD
                ) % MOD
                dp[n][2][k] = (
                    (dp[n - 1][0][k - 1] + dp[n - 1][1][k - 2]) % MOD +
                    (dp[n - 1][2][k] + dp[n - 1][3][k - 1]) % MOD
                ) % MOD
            else:
                dp[n][1][k] = (
                    (dp[n - 1][0][k - 1] + dp[n - 1][1][k]) % MOD +
                    dp[n - 1][3][k - 1] % MOD
                ) % MOD
                dp[n][2][k] = (
                    dp[n - 1][0][k - 1] % MOD +
                    (dp[n - 1][2][k] + dp[n - 1][3][k - 1]) % MOD
                ) % MOD

    ans = (
        (dp[N][0][K] + dp[N][1][K]) % MOD +
        (dp[N][2][K] + dp[N][3][K]) % MOD
    ) % MOD
    return ans

def main(n):
    # 这里根据规模 n 生成一组 (N, K) 测试数据
    # 示例策略：N = n，K = n（需要满足 1 <= K <= 2N）
    N = max(1, n)
    K = max(1, min(2 * N, n))

    result = solve(N, K)
    print(result)

if __name__ == "__main__":
    # 示例：按需要手动指定规模
    main(10)