from __pypy__.intop import int_mulmod

def main(n):
    n_ = n
    MOD = 10**9 + 7

    def mul(a, b):
        return int_mulmod(a, b, MOD)

    N = max(2, n_ + 5)
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    fact = [1]
    for x in range(1, N):
        fact.append(fact[-1] * x % MOD)

    inv_fact = [0] * N
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for x in range(N - 1, 0, -1):
        inv_fact[x - 1] = inv_fact[x] * x % MOD

    def nCr(nn, rr):
        if rr < 0 or rr > nn:
            return 0
        return mul(fact[nn], mul(inv_fact[nn - rr], inv_fact[rr]))

    for nn in range(1, N + 1):
        dp[nn][nn] = pow(2, nn - 1, MOD)
        for i in range(1, nn - 1):
            j = nn - i - 1
            for k in range(1, i + 1):
                dp[nn][k + j] = (dp[nn][k + j]
                                 + mul(nCr(k + j, k), mul(dp[i][k], dp[j][j]))) % MOD

    return sum(dp[n_]) % MOD


if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    print(main(10))