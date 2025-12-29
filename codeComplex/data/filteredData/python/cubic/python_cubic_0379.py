import sys
from math import ceil, log, gcd, pi

MOD_DEFAULT = 10**9 + 7
N = 406  # maximum size used in original precomputation


def main(n):
    """
    n: problem size (integer), should satisfy n + 2 <= N (i.e., n <= 404) for safety.
    Returns the computed answer instead of printing.
    """
    mod = MOD_DEFAULT

    # Precompute factorials, inverses, powers of 2, and nCr up to N
    fact = [1] * N
    inver = [1] * N
    power2 = [1] * N
    ncr = [[1] * N for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    # Precomputation
    fact[0] = 1
    inver[0] = 1
    for i in range(1, N):
        fact[i] = (fact[i - 1] * i) % mod
        inver[i] = pow(fact[i], mod - 2, mod)

    for i in range(N):
        for j in range(i + 1):
            ncr[i][j] = (((fact[i] * inver[j]) % mod) * inver[i - j]) % mod

    for i in range(1, N):
        power2[i] = (power2[i - 1] * 2) % mod

    # DP logic from original code
    dp[0][0] = 1

    for i in range(n):
        for j in range(i + 1):
            k = 1
            while i + k <= n:
                dp[i + k + 1][j + k] = (
                    dp[i + k + 1][j + k]
                    + (dp[i][j] * power2[k - 1]) % mod * ncr[j + k][k]
                ) % mod
                k += 1

    ans = 0
    for i in range(n + 1):
        ans = (ans + dp[n + 1][i]) % mod

    return ans


# 示例：如需直接运行测试，可取消下面注释
# if __name__ == "__main__":
#     n_test = 5  # 自定义规模
#     print(main(n_test))