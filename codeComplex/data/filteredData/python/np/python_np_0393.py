def check(a, mid, n, m, z):
    from collections import Counter
    b = Counter()
    for i in range(n):
        c = ["0"] * m
        for j in range(m):
            if a[i][j] >= mid:
                c[j] = "1"
        zz = int("".join(c), 2)
        b[zz] = i
    c = list(b.keys())
    lc = len(c)
    for i in range(lc):
        for j in range(i, lc):
            if c[i] | c[j] == z:
                mi, x, y = 10000000000, b[c[i]], b[c[j]]
                for k in range(m):
                    mi = min(mi, max(a[x][k], a[y][k]))
                if mi >= mid:
                    return (x, y)


def main(n):
    # n controls both number of rows and columns for scalability
    if n <= 0:
        return

    m = n
    # Deterministic generation of matrix a with values up to about 1e9 range
    a = [[(i * m + j) * 1234567 % (10**9) for j in range(m)] for i in range(n)]

    lo, hi, ans, y = 0, 10**9, [1, 1], (1 << m) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        z = check(a, mid, n, m, y)
        if z:
            lo = mid + 1
            ans = [z[0] + 1, z[1] + 1]
        else:
            hi = mid - 1
    print(*ans)


if __name__ == "__main__":
    main(5)