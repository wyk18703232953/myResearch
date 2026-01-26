def main(n):
    MOD = 10 ** 9 + 7

    # Define input scale mapping:
    # n >= 1
    # string length: n
    # number of queries: q = n
    # queries: i-th query uses interval [1, i] (clipped to [1, n])
    if n <= 0:
        return []

    # Deterministically construct the binary string s of length n.
    # Pattern: s[i] is '1' iff i is odd.
    s_body = ''.join('1' if i % 2 == 1 else '0' for i in range(1, n + 1))
    s = 'x' + s_body  # 1-based indexing

    # Prefix sums of count of '1'
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        c[i] = c[i - 1] + (s[i] == '1')

    # Precompute powers of 2 up to 2 * n
    p2 = [1] * (2 * n + 1)
    for i in range(1, 2 * n + 1):
        p2[i] = p2[i - 1] * 2 % MOD

    # Deterministically generate q = n queries
    # Query i: [l, r] = [1, i] (with r clipped to n)
    out = []
    for q_idx in range(1, n + 1):
        l = 1
        r = q_idx
        if r > n:
            r = n
        o = c[r] - c[l - 1]
        z = (r - l + 1) - o
        ans = (p2[o + z] - 1 - p2[z] + 1) % MOD
        out.append(ans)

    return out


if __name__ == "__main__":
    # Example deterministic run
    results = main(10)
    for value in results:
        # print(value)
        pass