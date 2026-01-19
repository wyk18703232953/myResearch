def check(mid, arr, m, n):
    ls = [[] for _ in range(1 << m)]
    for i in range(n):
        ans = 0
        for j in range(m):
            if arr[i][j] >= mid:
                ans += 1 << j
        ls[ans].append(i + 1)
    for i in range(len(ls)):
        for j in range(len(ls)):
            if len(ls[i]) and len(ls[j]) and (i | j) == (1 << m) - 1:
                return ls[i][0], ls[j][0]
    return 0


def main(n):
    # Interpret n as number of rows; keep columns small and fixed for scaling
    if n <= 0:
        return

    m = 5  # fixed small dimension so that 2^m subsets stay manageable

    # Deterministic construction of arr[n][m]
    # Values grow with i and j so that binary search has some structure.
    arr = [[(i + 1) * (j + 2) + (i % (j + 2)) for j in range(m)] for i in range(n)]

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
    # Example deterministic call; change n to scale input size
    main(1000)