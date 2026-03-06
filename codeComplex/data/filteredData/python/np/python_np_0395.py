def main(n):
    # Map n to matrix dimensions: use n as both number of rows and columns
    # Ensure at least 1x1 matrix
    n = max(1, n)
    m = n

    # Deterministically generate matrix a of size n x m
    # Example pattern: a[i][j] = (i * m + j) % (10**9 + 7)
    MOD = 10 ** 9 + 7
    a = [[(i * m + j) % MOD for j in range(m)] for i in range(n)]

    l = -1
    r = 10 ** 9 + 1
    ans1, ans2 = -1, -1
    full_mask = (1 << m) - 1

    while r - l > 1:
        x = (l + r) // 2
        idx = {}
        for i in range(n):
            v = 0
            for j in range(m):
                if a[i][j] >= x:
                    v += 1
                v <<= 1
            idx[v >> 1] = i
        ok = False
        idx1, idx2 = 0, 0
        for aa, bb in idx.items():
            for cc, dd in idx.items():
                for _ in range(m):
                    if (aa | cc) == full_mask:
                        ok = True
                        idx1 = bb + 1
                        idx2 = dd + 1
        if ok:
            l = x
            ans1 = idx1
            ans2 = idx2
        else:
            r = x

    print(ans1, ans2)


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(5)