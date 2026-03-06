def check(mid, arr, m, n):
    ls = [[] for _ in range(1 << m)]
    for i in range(n):
        ans = 0
        for j in range(m):
            if arr[i][j] >= mid:
                ans += 1 << j
        ls[ans].append(i + 1)
    full_mask = (1 << m) - 1
    for i in range(len(ls)):
        if not ls[i]:
            continue
        for j in range(len(ls)):
            if ls[j] and (i | j) == full_mask:
                return ls[i][0], ls[j][0]
    return 0


def main(n):
    # Interpret n as number of rows; set m as a small fixed dimension
    m = 5
    # Deterministically generate an n x m matrix
    # Values are constructed so that they grow with i and j but are fully deterministic
    arr = [[(i + 1) * (j + 2) + (i // 2) for j in range(m)] for i in range(n)]

    hi, lo, ind1 = 10 ** 9, 0, (1, 1)
    while hi >= lo:
        mid = (hi + lo) // 2
        ind = check(mid, arr, m, n)
        if ind:
            ind1 = ind
            lo = mid + 1
        else:
            hi = mid - 1
    print(ind1[0], ind1[1])


if __name__ == "__main__":
    main(10)