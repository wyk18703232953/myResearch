def main(n):
    # Map n to problem dimensions
    # For scalability, let m grow slowly with n so 4^m stays manageable
    if n <= 0:
        n = 1
    m = max(1, min(10, n // 5 + 1))  # 1 <= m <= 10
    rows = n

    # Deterministic data generation: arr[i][j] is a simple arithmetic function of (i, j, n, m)
    # Values are spread in a moderate range to exercise the binary search.
    base = 10 ** 8
    arr = tuple(
        tuple(((i + 1) * (j + 2) * (n + m) + i * j + j) % base for j in range(m))
        for i in range(rows)
    )

    lower_bound = 0
    upper_bound = int(1e9) + 1
    mask = (1 << m) - 1

    ans = (0, 0)

    def can_upper(mid):
        nonlocal ans
        d = {}
        for i in range(rows):
            bit = 0
            for j in range(m):
                if arr[i][j] >= mid:
                    bit |= 1 << j
            d[bit] = i

        keys = tuple(d.keys())
        for i in range(len(keys)):
            a1 = keys[i]
            for j in range(i, len(keys)):
                a2 = keys[j]
                if a1 | a2 == mask:
                    ans = (d[a1], d[a2])
                    return True
        return False

    while upper_bound - lower_bound > 1:
        middle = (upper_bound + lower_bound) >> 1
        if can_upper(middle):
            lower_bound = middle
        else:
            upper_bound = middle

    # Keep the original output behavior (1-based indices)
    print(ans[0] + 1, ans[1] + 1)


if __name__ == "__main__":
    # Example deterministic run; change n here to scale the experiment
    main(50)