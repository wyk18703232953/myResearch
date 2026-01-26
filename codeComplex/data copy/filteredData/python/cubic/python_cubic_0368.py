def main(n: int):
    # 生成测试数据：规模 N = n，模数取一个大质数
    N = n
    mod = 10**9 + 7

    two = [1] * (N + 1)
    fact = [1] * (N + 1)
    inv = [1] * (N + 1)

    for i in range(1, N + 1):
        two[i] = two[i - 1] * 2 % mod
    for i in range(2, N + 1):
        fact[i] = fact[i - 1] * i % mod

    inv[N] = pow(fact[N], mod - 2, mod)
    for i in range(N, 0, -1):
        inv[i - 1] = inv[i] * i % mod

    dp = [[0] * (N + 2) for _ in range(N + 2)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(i + 1):
            if dp[i][j] == 0:
                continue
            for k in range(1, N + 1):
                if i + k > N:
                    break
                dp[i + k + 1][j + 1] += dp[i][j] * two[k - 1] * inv[k] % mod
                dp[i + k + 1][j + 1] %= mod

    ans = 0
    for j in range(1, N + 1):
        ans += dp[N + 1][j] * fact[N - j + 1] % mod
        ans %= mod

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)