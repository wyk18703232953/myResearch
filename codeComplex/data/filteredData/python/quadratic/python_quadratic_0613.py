def main(n):
    # Input structure in original code:
    # n, m, k: integers
    # a: list of length n
    #
    # Here, external inputs are removed.
    # We interpret the user-provided `n` as the length of list `a`.
    # Then deterministically generate m, k, and a based on n.

    if n <= 0:
        # print(0)
        pass
        return

    # Deterministic generation of m and k from n
    m = max(1, n // 3)
    k = max(1, n // 2)

    # Deterministic generation of array a of length n
    # Example: a[i] = (i * 2 + 3) % (k + 3) + 1, ensuring strictly positive ints
    a = [((i * 2 + 3) % (k + 3)) + 1 for i in range(n)]

    sa = [0] * n
    ans = 0

    for i in range(n):
        sa[i] = a[i] - k
        s = a[i]
        # Original inner loop: for j in range(i-1, max(-1, i-m-1), -1):
        for j in range(i - 1, max(-1, i - m - 1), -1):
            sa[i] = max(sa[i], sa[j] + s - k)
            s += a[j]
        if i < m:
            sa[i] = max(sa[i], s - k)
        sa[i] = max(sa[i], 0)
        ans = max(ans, sa[i])

    # print(ans)
    pass
if __name__ == "__main__":
    # Example deterministic call for testing / experimentation
    main(10)