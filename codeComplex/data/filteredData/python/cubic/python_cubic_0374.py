#!/usr/bin/python3

def main(n):
    # 生成测试数据：给定规模 n，构造模数 m
    # 原程序对 MOD 的要求：作为 pow(..., MOD-2, MOD) 的模，需为质数
    # 简单起见，取一个固定大质数
    m = 10**9 + 7

    MOD = m
    MAX_N = 10**3

    # 构造阶乘表
    fac = [1] + [0] * MAX_N
    for i in range(1, MAX_N + 1):
        fac[i] = fac[i - 1] * i % MOD

    fac_inv = [1] + [0] * MAX_N
    # f[n!] 的逆元
    fac_inv[MAX_N] = pow(fac[MAX_N], MOD - 2, MOD)
    for i in range(MAX_N, 1, -1):
        fac_inv[i - 1] = fac_inv[i] * i % MOD

    def mod_nCr(nn, r):
        if nn < r or nn < 0 or r < 0:
            return 0
        tmp = fac_inv[nn - r] * fac_inv[r] % MOD
        return tmp * fac[nn] % MOD

    # 预计算 2 的幂
    pow2 = [0] * (n + 1)
    pow2[0] = 1
    for i in range(1, n + 1):
        pow2[i] = pow2[i - 1] * 2 % MOD

    # 预计算组合数
    TABLE_N = 500
    table = [[0] * TABLE_N for _ in range(TABLE_N)]
    for i in range(TABLE_N):
        for j in range(i + 1):
            table[i][j] = mod_nCr(i, j)

    # dp[i-th][j used]
    dp = [[0] * (n + 1) for _ in range(n)]
    for i in range(n):
        dp[i][i + 1] = pow2[i]

    for i in range(n - 1):
        for j in range(i // 2 + 1, n - 1):
            if dp[i][j] == 0:
                continue
            dp[i][j] %= MOD
            for k in range(1, n - j):
                if i + k + 1 >= n:
                    break
                # create new
                dp[i + k + 1][j + k] += dp[i][j] * pow2[k - 1] * table[k + j][k]

    ans = sum(dp[-1]) % MOD
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(n)，这里可以修改 n 以进行不同规模测试
    main(10)