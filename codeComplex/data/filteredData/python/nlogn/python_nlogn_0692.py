def main(n):
    # Define sizes based on n
    # Ensure at least size 1 for both lists
    m = max(1, n // 2)
    n_b = max(1, n - m)

    # Deterministic generation of b and g
    # b: increasing sequence, then shuffled deterministically by simple formula
    b = [(i * 2 + 3) % (n_b + 5) + 1 for i in range(n_b)]
    g = [(i * 3 + 1) % (m + 7) + 1 for i in range(m)]

    # Ensure at least one valid configuration where max(b) <= min(g)
    # Adjust g so that its minimum is >= maximum of b when needed
    mab = max(b)
    mig = min(g)
    if mab > mig:
        diff = mab - mig
        g = [x + diff for x in g]
        mig = min(g)

    mab = max(b)
    mig = min(g)
    if mab > mig:
        print(-1)
        return

    b = sorted(b, reverse=True)
    g = sorted(g)
    num = 0
    j = 0
    for i in range(n_b):
        k = 0
        l = 1
        while j < m and k < m - l and b[i] <= g[j]:
            if b[i] == g[j]:
                l = 0
            num += g[j]
            j += 1
            k += 1
        num += b[i] * (m - k)

    print(num)


if __name__ == "__main__":
    main(10)