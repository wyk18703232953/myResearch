def main(n):
    # 根据规模 n 生成 N 和 MOD，这里简单设定：
    # N = n, MOD 取一个常用大质数
    N = n
    MOD = 10**9 + 7

    dp = [[0] * (N + 2) for _ in range(N + 2)]
    dp[0][0] = 1
    limit = 1000

    # 阶乘与逆阶乘预处理（取前 limit 项）
    frac = [1] * limit
    for i in range(2, limit):
        frac[i] = i * frac[i - 1] % MOD

    fraci = [None] * limit
    fraci[-1] = pow(frac[-1], MOD - 2, MOD)
    for i in range(-2, -limit - 1, -1):
        fraci[i] = fraci[i + 1] * (limit + i + 1) % MOD

    # 预处理 2^k
    bb = [1, 2]
    for _ in range(1000):
        bb.append(bb[-1] * 2 % MOD)

    # DP 主循环
    for ln in range(N + 1):
        for cnt in range(ln // 2, ln + 1):
            for k in range(1, N - ln + 1):
                cmb = frac[cnt + k] * (fraci[cnt] * fraci[k] % MOD) % MOD
                dp[ln + k + 1][cnt + k] += dp[ln][cnt] * (bb[k - 1] * cmb % MOD) % MOD
                dp[ln + k + 1][cnt + k] %= MOD

    R = 0
    for x in dp[N + 1][:N + 1]:
        R = (R + x) % MOD
    print(R)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)