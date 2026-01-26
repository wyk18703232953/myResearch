def make_nCr_mod(max_n=2 * 10**5, mod=10**9 + 7):
    global fact, inv_fact
    max_n = min(max_n, mod - 1)
    fact, inv_fact = [0] * (max_n + 1), [0] * (max_n + 1)
    fact[0] = 1
    for i in range(max_n):
        fact[i + 1] = fact[i] * (i + 1) % mod
    inv_fact[-1] = pow(fact[-1], mod - 2, mod)
    for i in reversed(range(max_n)):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod


def comb(n, r):
    mod = 10**9 + 7
    global fact, inv_fact
    res = 1
    while n or r:
        a, b = n % mod, r % mod
        if a < b:
            return 0
        res = res * fact[a] % mod * inv_fact[b] % mod * inv_fact[a - b] % mod
        n //= mod
        r //= mod
    return res


def f():
    dp = [0] * (1000 + 100)
    dp[1] = 1
    for i in range(2, len(dp)):
        o = bin(i).count("1")
        if o == 1:
            dp[i] = 2

        else:
            dp[i] += dp[o] + 1
    return dp


def bit(s, k):
    dp = f()
    ans = 0
    ll = len(s)
    ans = 0
    ones = 0
    if k == 0:
        return 1
    for i in range(ll):
        if s[i] == "0":
            continue

        else:
            for j in range(max(ones, 1), 1000):
                if dp[j] == k:
                    ans = (ans + comb(ll - i - 1, j - ones)) % (10**9 + 7)
                    if i == 0 and k == 1:
                        ans -= 1
        ones += 1
    if dp[ones] == k:
        ans += 1
    return ans % (10**9 + 7)


def main(n):
    # 输入规模 n 映射为二进制串长度，k 为 n 的按位 1 的个数
    length = max(1, n)
    s = "".join("1" if (i * 37 + 13) % 5 < 2 else "0" for i in range(length))
    k = bin(n).count("1")
    make_nCr_mod()
    result = bit(s, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)