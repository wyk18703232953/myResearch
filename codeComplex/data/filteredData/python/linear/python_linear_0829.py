def matches(pos, c, case):
    if case == 0:
        return pos % 3 == "RGB".index(c)
    elif case == 1:
        return pos % 3 == "GBR".index(c)

    else:
        return pos % 3 == "BRG".index(c)


def solve_single_case(n, k, s):
    mglobal = k
    r = g = b = 0

    for i, c in enumerate(s[:k]):
        r += not matches(i, c, 0)
        g += not matches(i, c, 1)
        b += not matches(i, c, 2)

    mglobal = min(mglobal, r, g, b)

    for i, c in enumerate(s[k:]):
        i += k
        r += -(not matches(i - k, s[i - k], 0)) + (not matches(i, c, 0))
        g += -(not matches(i - k, s[i - k], 1)) + (not matches(i, c, 1))
        b += -(not matches(i - k, s[i - k], 2)) + (not matches(i, c, 2))
        mglobal = min(mglobal, r, g, b)

    return mglobal


def main(n):
    # Interpret n as total length of all strings.
    # We'll construct q test cases deterministically.
    # Let q grow like max(1, n // 10), and each string length n_i ≈ 10.
    if n <= 0:
        return

    q = max(1, n // 10)
    results = []

    # total length should not exceed n, adjust per-case length
    base_len = max(3, n // q)  # at least 3 for meaningful k
    remaining = n

    for t in range(q):
        # Last case takes all remaining to ensure sum lengths == n
        if t == q - 1:
            length = max(3, remaining)

        else:
            length = min(base_len, remaining - 3 * (q - t - 1))
            length = max(3, length)

        remaining -= length

        # Deterministic k between 1 and length
        k = 1 + (t % length)

        # Deterministic string s of length 'length'
        # pattern cycles to keep structure but fully deterministic
        pattern = "RGB"
        s = "".join(pattern[(i + t) % 3] for i in range(length))

        res = solve_single_case(length, min(k, length), s)
        results.append(res)

    # To keep behavior simple and deterministic, print one result per line
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(1000)