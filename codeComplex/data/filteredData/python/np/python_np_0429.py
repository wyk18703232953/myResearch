hell = 1000000007
id1 = 0
id2 = 0
a = []


def check(n, m, x):
    global id1, id2, a
    b = [0] * (1 << m)
    idx = [0] * (1 << m)
    for i in range(n):
        mask = 0
        for j in range(m):
            if a[i][j] >= x:
                mask ^= (1 << j)
        b[mask] = 1
        idx[mask] = i + 1
    full = (1 << m) - 1
    for i in range(1 << m):
        if b[i]:
            for j in range(1 << m):
                if b[j]:
                    if (i | j) == full:
                        id1 = idx[i]
                        id2 = idx[j]
                        return 1
    return 0


def main(n):
    """
    n: number of rows (size parameter)
    Auto-generate test data of size n x m.
    """
    import random

    global id1, id2, a
    id1 = 0
    id2 = 0
    a = []

    # Choose a reasonable m based on n for testing (can be adjusted)
    m = max(1, min(8, n))  # keep m small to avoid 2^m explosion

    # Generate test data: integers in range [0, hell)
    for _ in range(n):
        row = [random.randint(0, hell) for _ in range(m)]
        a.append(row)

    lo = 0
    hi = hell
    while hi - lo > 0:
        mid = (hi + lo + 1) // 2
        if check(n, m, mid):
            lo = mid
        else:
            hi = mid - 1
    check(n, m, lo)
    print(id1, id2)


if __name__ == "__main__":
    # Example run with n = 5 (can be changed)
    main(5)