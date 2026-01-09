def main(n: int):
    # 生成测试数据：固定一个较大的质数模数
    MOD = 10**9 + 7

    max_size = 500
    fac = [1] * max_size
    finv = [1] * max_size
    p2 = [1] * max_size

    # 预处理阶乘、阶乘逆元和 2 的幂
    for i in range(max_size - 1):
        fac[i + 1] = fac[i] * (i + 1) % MOD
        finv[i + 1] = pow(fac[i + 1], MOD - 2, MOD)
        p2[i + 1] = p2[i] * 2 % MOD

    dp = [[0] * (n // 2 + 2) for _ in range(n + 2)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(i + 2, n + 2):
            gap = j - i - 1
            if gap - 1 < 0:
                continue
            coef = finv[gap] * p2[gap - 1] % MOD
            for k in range(n // 2 + 1):
                dp[j][k + 1] = (dp[j][k + 1] + dp[i][k] * coef) % MOD

    ans = 0
    for i in range(1, n // 2 + 2):
        ans = (ans + dp[n + 1][i] * fac[n - i + 1]) % MOD

    # print(ans % MOD)
    pass
if __name__ == "__main__":
    # 示例：规模 n 的测试
    main(10)