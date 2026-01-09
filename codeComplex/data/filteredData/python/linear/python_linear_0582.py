def main(n):
    MOD = 10 ** 9 + 7

    # Map n to string length and query count deterministically
    str_len = n
    q = n

    # Deterministically generate a binary string of length str_len
    # Pattern: s[i] = '1' iff i is odd (1-based index)
    s = 'x' + ''.join('1' if (i % 2 == 1) else '0' for i in range(1, str_len + 1))

    n_local = str_len

    c = [0] * (n_local + 1)
    for i in range(1, n_local + 1):
        c[i] = c[i - 1] + (s[i] == '1')

    p2 = [1] * (2 * n_local + 1)
    for i in range(1, 2 * n_local + 1):
        p2[i] = p2[i - 1] * 2 % MOD

    # Deterministically generate q queries (l, r) within [1, n_local]
    # Example pattern: l = (i % n) + 1, r = n_local - (i % n)
    # Ensure l <= r; if not, swap.
    queries = []
    if n_local == 0:
        queries = []

    else:
        for i in range(q):
            l = (i % n_local) + 1
            r = n_local - (i % n_local)
            if l > r:
                l, r = r, l
            queries.append((l, r))

    out = []
    for l, r in queries:
        o = c[r] - c[l - 1]
        z = (r - l + 1) - o
        ans = (p2[o + z] - 1 - p2[z] + 1) % MOD
        out.append(ans)

    # For experiment purposes, return the results instead of printing
    return out


if __name__ == "__main__":
    # Example deterministic call
    results = main(10)
    for v in results:
        # print(v)
        pass