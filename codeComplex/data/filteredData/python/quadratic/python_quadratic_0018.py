from collections import defaultdict

def main(n):
    mod = 10 ** 9 + 7

    # Precompute combinations C(i, j) modulo mod
    comb = [[1]]
    for i in range(1, 1010):
        x = [1]
        for j in range(1, i):
            x.append((comb[i - 1][j - 1] + comb[i - 1][j]) % mod)
        x.append(1)
        comb.append(x)

    # Precompute dp as in original program
    dp = [1]
    for i in range(1, 1010):
        r = 0
        for k in range(i):
            r += dp[k] * comb[i - 1][k]
            r %= mod
        dp.append(r)

    # Map n to input size:
    # Use m = n (number of rows), n_bits = n (number of columns / string length)
    if n <= 0:
        print(1)
        return

    m = n
    n_bits = n

    # Deterministically generate bit-strings of length m, repeated for n_bits columns.
    # Column j uses bits pattern: bit i = ((i + j) % 2)
    ns = [0 for _ in range(m)]
    for j in range(n_bits):
        for i in range(m):
            bit = (i + j) % 2
            ns[i] |= bit << j

    dd = defaultdict(int)
    for e in ns:
        dd[e] += 1

    ans = 1
    for b in dd.values():
        ans = ans * dp[b] % mod

    print(ans)


if __name__ == "__main__":
    main(10)