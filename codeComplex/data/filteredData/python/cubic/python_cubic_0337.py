from collections import Counter

mod = 998244353

def generate_input(n):
    # n is the length of the list a
    if n <= 0:
        n = 1
    # Deterministic construction of a: arithmetic pattern
    # Values are spread and include duplicates and zeros
    a = [i * 2 - (i // 3) for i in range(n)]
    return n, a

def core_algorithm(n, a):
    d = Counter(a)
    d[0] = 0
    b = list(d.items())
    b.sort()
    m = len(b)
    ba = [0] * m
    cn = [0] * (m + 1)
    k = h = 0
    for i, x in enumerate(b):
        while h < m and x[0] >= b[h][0] * 2:
            h += 1
        ba[i] = h - 1
        while k < m and x[0] * 2 > b[k][0]:
            k += 1
        cn[k] += x[1]
    for i in range(m):
        cn[i + 1] += cn[i]
    dp = [0] * m
    dp[0] = 1
    b_counts = [x[1] for x in b]
    for i in range(n):
        ndp = [0] * m
        for j in range(1, m):
            if cn[j] >= i - 1:
                ndp[j] = dp[j] * (cn[j] - i + 1) % mod
            dp[j] += dp[j - 1]
            if dp[j] >= mod:
                dp[j] -= mod
        for j in range(1, m):
            ndp[j] += dp[ba[j]] * b_counts[j]
            ndp[j] %= mod
        dp = ndp
    return sum(dp) % mod

def main(n):
    n_gen, a = generate_input(n)
    result = core_algorithm(n_gen, a)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)