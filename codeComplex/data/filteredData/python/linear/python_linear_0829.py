def matches(pos, c, case):
    if case == 0:
        return pos % 3 == "RGB".index(c)
    elif case == 1:
        return pos % 3 == "GBR".index(c)
    else:
        return pos % 3 == "BRG".index(c)


def solve_single(n, k, s):
    mglobal = k
    r = g = b = 0

    # Initial window [0, k)
    for i, c in enumerate(s[:k]):
        r += not matches(i, c, 0)
        g += not matches(i, c, 1)
        b += not matches(i, c, 2)

    mglobal = min(mglobal, r, g, b)

    # Slide window
    for i, c in enumerate(s[k:], start=k):
        r += -(not matches(i - k, s[i - k], 0)) + (not matches(i, c, 0))
        g += -(not matches(i - k, s[i - k], 1)) + (not matches(i, c, 1))
        b += -(not matches(i - k, s[i - k], 2)) + (not matches(i, c, 2))
        mglobal = min(mglobal, r, g, b)

    return mglobal


def main(n):
    # n controls both: number of testcases q = n, and size of each string
    q = n if n > 0 else 1
    results = []

    for t in range(q):
        # For testcase t, set string length = n + t, and k as a fraction of length
        length = n + t if n + t > 0 else 1
        k = max(1, length // 2)

        # Deterministic construction of s of length `length` using "RGB" pattern
        base = "RGB"
        s = "".join(base[(i + t) % 3] for i in range(length))

        res = solve_single(length, k, s)
        results.append(res)

    # Output all results, one per line
    for x in results:
        print(x)


if __name__ == "__main__":
    main(10)