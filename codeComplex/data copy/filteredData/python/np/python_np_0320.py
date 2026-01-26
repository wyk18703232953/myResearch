import sys

mod = 998244353
INF = float('inf')

def comb(n, m):
    from math import factorial
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0

def perm(n, m):
    from math import factorial
    return factorial(n) // (factorial(n - m)) if n >= m else 0

def mdis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def main(n):
    # 映射规则：给定规模 n，构造 (N, K)
    # 这里取 N = n，K = max(1, n // 2)，保证 k <= n 且可规模化
    N, K = n, max(1, n // 2)

    dp = [[0] * 4 for _ in range(K + 2)]
    dp[1][0] = 1
    dp[1][3] = 1
    if K + 1 >= 2:
        dp[2][1] = 1
        dp[2][2] = 1

    for i in range(2, N + 1):
        new = [[0] * 4 for _ in range(K + 2)]
        for j in range(1, K + 2):
            for l in range(4):
                new[j][l] += dp[j][l]
                if l == 0 or l == 3:
                    if j - 1 >= 0:
                        new[j][l] += dp[j - 1][l ^ 3]
                    new[j][l] += (dp[j][1] + dp[j][2])
                elif l == 1 or l == 2:
                    if j - 1 >= 0:
                        new[j][l] += (dp[j - 1][0] + dp[j - 1][3])
                    if j - 2 >= 0:
                        new[j][l] += dp[j - 2][l ^ 3]
                new[j][l] %= mod
        dp = new

    result = sum(dp[K]) % mod
    print(result)
    return result

if __name__ == "__main__":
    # 示例：使用固定 n 调用 main，用于时间复杂度实验时可自行修改
    main(1000)