def main(n):
    # Interpret n as the length of array a.
    # Deterministically generate m, k, and a.
    # Ensure m is at least 1 and at most n.
    if n <= 0:
        return 0

    m = max(1, n // 3)
    k = n // 5 + 1

    # Deterministic array generation
    a = [(i * 7) % 100 + (i // 3) for i in range(n)]
    sa = [0] * n

    ans = 0

    for i in range(n):
        sa[i] = a[i] - k
        s = a[i]
        # original loop: for j in range(i-1, max(-1, i-m-1), -1)
        for j in range(i - 1, max(-1, i - m - 1), -1):
            sa[i] = max(sa[i], sa[j] + s - k)
            s += a[j]
        if i < m:
            sa[i] = max(sa[i], s - k)
        sa[i] = max(sa[i], 0)
        ans = max(ans, sa[i])

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # Example call for time complexity experiments
    main(1000)