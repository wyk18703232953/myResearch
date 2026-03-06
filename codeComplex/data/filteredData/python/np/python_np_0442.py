def main(n):
    from collections import defaultdict as dd

    # Map n to problem parameters:
    # Let m (number of columns) grow slowly with n to keep 2^m manageable.
    # For complexity experiments you can adjust this mapping.
    m = 5 + (n % 6)  # m ranges from 5 to 10
    if n <= 0:
        n = 1

    # Deterministic data generation
    # l will be a list of n rows, each row has m integers.
    # Use simple arithmetic patterns depending on i, j, n, m.
    l = []
    for i in range(n):
        row = []
        for j in range(m):
            # Construct a value that depends on i and j but is deterministic.
            # Ensure values are positive and spread over a range.
            val = (i + 1) * (j + 2) + (i // 2) + (j % 3) + n
            row.append(val)
        l.append(row)

    # Convert to original structure: each row will later be extended by its 1-based index.
    an = -1
    a = b = 0
    for idx in range(n):
        k = l[idx]
        l[idx] = k + [idx + 1]
        if an < min(k):
            a = b = idx + 1
            an = min(k)

    le = an
    r = 10 ** 9 + 1
    while le < r:
        md = (le + r) // 2
        f = 0
        a1 = a2 = -1
        s = [0] * n
        for i in range(n):
            for j in range(m):
                if l[i][j] >= md:
                    s[i] |= 1 << j

        po = 1 << m
        d = [0] * po
        for i in range(n):
            d[s[i]] = i + 1
        for i in range(1, po):
            if d[i]:
                pp = i
                while pp:
                    d[pp] = d[i]
                    pp = (pp - 1) & i
        if d[po - 1]:
            f = 1
            a1 = a2 = d[po - 1]
        for i in range(1, po):
            if d[i] and d[(po - 1) ^ i]:
                f = 1
                a1 = d[i]
                a2 = d[(po - 1) ^ i]
                break
        if f:
            le = md + 1
            if md > an:
                a, b = a1, a2
                an = md
        else:
            r = md
    print(a, b)


if __name__ == "__main__":
    # Example call for complexity experiments
    main(1000)