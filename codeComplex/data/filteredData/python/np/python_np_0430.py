def main(n):
    # Interpret n as both number of rows and columns (square matrix)
    # m controls bitmask size; keep it reasonably small (e.g., up to 10)
    m = min(10, max(1, n))  # ensure 1 <= m <= 10
    rows = n

    # Deterministically generate matrix l of size rows x m
    # l[i][j] are integers constructed from i and j
    l = [[(i * m + j) % (10**6) for j in range(m)] for i in range(rows)]

    left = 0
    right = 10**9 + 1
    ans = (1, 1)  # default in case algorithm never sets it, for completeness

    while left < right:
        mid = (left + right) // 2
        dicta = {}
        for i in range(rows):
            mask = 0
            for j in range(m):
                mask <<= 1
                if l[i][j] >= mid:
                    mask += 1
            dicta[mask] = i
        ok = False
        full_mask = (1 << m) - 1
        for i_mask in dicta:
            for j_mask in dicta:
                if (i_mask | j_mask) == full_mask:
                    ok = True
                    ans = (dicta[i_mask] + 1, dicta[j_mask] + 1)
                    break
            if ok:
                break
        if ok:
            left = mid + 1
        else:
            right = mid

    # Original program prints the pair of indices
    print(*ans)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)