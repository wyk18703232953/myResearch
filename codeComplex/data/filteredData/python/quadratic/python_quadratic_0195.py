def main(n):
    from operator import xor

    # Deterministically construct original inputs based on n
    # Original structure:
    # n_orig: size
    # a[0]: initial array of length n_orig
    # m: number of queries
    # qur: list of (l, r) queries

    n_orig = n if n > 0 else 1

    # Build initial array a[0] deterministically
    # Example: a[0][i] = (i * (i + 1)) % (n_orig + 7)
    first_row = [(i * (i + 1)) % (n_orig + 7) for i in range(n_orig)]
    a = [first_row]

    # Number of queries scales linearly with n
    m = n_orig

    # Deterministically generate queries (1-based indices, l <= r)
    qur = []
    for i in range(1, m + 1):
        l = ((i * 2) % n_orig) + 1
        r = ((i * 3) % n_orig) + 1
        if l > r:
            l, r = r, l
        qur.append([l, r])

    out = []

    # Core logic: build xor triangle
    for i in range(1, n_orig):
        a.append(list(map(xor, a[-1][:-1], a[-1][1:])))

    # Core logic: propagate maximums
    for i in range(n_orig - 1):
        a[i + 1] = list(map(max, a[i][:-1], a[i][1:], a[i + 1]))

    # Answer queries
    for l, r in qur:
        out.append(a[r - l][l - 1])

    for v in out:
        print(v)


if __name__ == "__main__":
    main(5)