MOD = 10 ** 9 + 7


def make_nCr_mod(max_n=2 * 10 ** 5, mod=MOD):
    max_n = min(max_n, mod - 1)

    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod

    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod

    def nCr_mod(n, r):
        res = 1
        while n or r:
            a, b = n % mod, r % mod
            if a < b:
                return 0
            res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
            n //= mod
            r //= mod
        return res

    return nCr_mod


def build_dp(limit=1100):
    dp = [0] * (limit + 1)
    dp[1] = 1
    for i in range(2, len(dp)):
        o = bin(i).count("1")
        if o == 1:
            dp[i] = 2
        else:
            dp[i] = dp[o] + 1
    return dp


DP = build_dp()
COMB = make_nCr_mod()


def bit(s, k):
    dp = DP
    comb = COMB
    ans = 0
    ll = len(s)
    ones = 0

    if k == 0:
        return 1

    for i in range(ll):
        if s[i] == "0":
            continue
        for j in range(max(ones, 1), 1000):
            if dp[j] == k:
                ans = (ans + comb(ll - i - 1, j - ones)) % MOD
                if i == 0 and k == 1:
                    ans = (ans - 1) % MOD
        ones += 1

    if dp[ones] == k:
        ans = (ans + 1) % MOD

    return ans % MOD


def main(n):
    """
    生成测试数据：
    - s: 长度为 n 的二进制串，周期性 "10" 填充，多余位补 '1'
    - k: 取 n 的二进制中 1 的个数
    返回 bit(s, k) 的结果。
    """
    if n <= 0:
        return 0

    s = "".join("10"[(i % 2)] for i in range(n - 1)) + "1"
    k = s.count("1")
    return bit(s, k)


if __name__ == "__main__":
    # 示例：规模 n = 10
    print(main(10))