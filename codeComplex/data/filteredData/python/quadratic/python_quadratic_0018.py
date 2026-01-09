from collections import defaultdict

def main(n):
    mod = 10 ** 9 + 7

    comb = [[1]]
    for i in range(1, 1010):
        x = [1]
        for j in range(1, i):
            x.append((comb[i - 1][j - 1] + comb[i - 1][j]) % mod)
        x.append(1)
        comb.append(x)

    dp = [1]
    for i in range(1, 1010):
        r = 0
        for k in range(i):
            r += dp[k] * comb[i - 1][k]
            r %= mod
        dp.append(r)

    # Deterministic input generation based on n
    # Interpret n as both number of rows and columns (m = n = n)
    m = n
    if m <= 0:
        # print(1)
        pass
        return
    if m > 1000:
        m = 1000
    cols = m

    ns = [0 for _ in range(m)]
    for j in range(cols):
        # s[i] is deterministically generated as (i + j) % 2
        for i in range(m):
            bit = (i + j) % 2
            ns[i] |= bit << j

    dd = defaultdict(int)
    for e in ns:
        dd[e] += 1

    ans = 1
    for b in dd.values():
        ans = ans * dp[b] % mod

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)