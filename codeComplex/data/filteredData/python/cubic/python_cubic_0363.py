#   Author: yumtam (modified)
#   Converted to main(n) style without input(), with generated test data.

try:
    from __pypy__.intop import int_mulmod
    def mul(a, b, MOD):
        return int_mulmod(a, b, MOD)
except ImportError:
    # Fallback for CPython or environments without __pypy__.intop
    def mul(a, b, MOD):
        return (a * b) % MOD


def main(n_):
    # 1. 设置规模和模数（可根据需要改成参数）
    MOD = 10**9 + 7
    N = max(410, n_)  # 原代码中 N 固定为 410，这里确保 N 至少覆盖到 n_

    # 2. 预处理阶乘与逆元
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    fact = [1]
    for x in range(1, N):
        fact.append(fact[-1] * x % MOD)

    inv_fact = [0] * N
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for x in reversed(range(1, N)):
        inv_fact[x - 1] = inv_fact[x] * x % MOD

    def nCr(n, r):
        if r < 0 or r > n:
            return 0
        return mul(fact[n], mul(inv_fact[n - r], inv_fact[r], MOD), MOD)

    # 3. DP 转移
    for n in range(1, N + 1):
        dp[n][n] = pow(2, n - 1, MOD)
        for i in range(1, n - 1):
            j = n - i - 1
            for k in range(1, i + 1):
                dp[n][k + j] = (dp[n][k + j]
                                + mul(nCr(k + j, k),
                                      mul(dp[i][k], dp[j][j], MOD),
                                      MOD)) % MOD

    # 4. 返回结果（对应原程序的输出）
    return sum(dp[n_]) % MOD


# 示例：生成一个测试规模并调用 main
if __name__ == "__main__":
    # 根据规模 n 生成测试：这里简单示例使用 n = 10
    n_test = 10
    ans = main(n_test)
    print(ans)