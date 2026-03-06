def main(n):
    # Map n to original n, m and matrix l deterministically
    # Here we let m = max(1, min(10, n)) and number of rows equal to n
    m = max(1, min(10, n))
    rows = n

    mask = (1 << m) - 1

    # Deterministic generation of l: rows x m matrix
    # Values increase with row and column indices, scaled to a range
    l = []
    for i in range(rows):
        row = []
        base = i * 3 + 1
        for j in range(m):
            val = base + j * 2
            row.append(val)
        l.append(row)

    lo = -1  # Possible
    hi = 10 ** 9 + 1  # Impossible
    outi = 0
    outj = 0

    while hi - lo > 1:
        test = (hi + lo) // 2

        things = dict()
        for i in range(rows):
            curr = 0
            for v in l[i]:
                curr *= 2
                if v >= test:
                    curr += 1
            things[curr] = i

        works = False
        for v1 in things:
            for v2 in things:
                if v1 | v2 == mask:
                    outi = things[v1]
                    outj = things[v2]
                    works = True
                    break
            if works:
                break

        if works:
            lo = test
        else:
            hi = test

    print(outi + 1, outj + 1)


if __name__ == "__main__":
    main(100)