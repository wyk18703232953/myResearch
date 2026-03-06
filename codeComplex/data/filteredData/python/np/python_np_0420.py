def main(n):
    # Map n to matrix dimensions:
    # choose m relatively small because complexity has 4^m term.
    # Example: m = max(1, min(10, n // 10)), n_rows = n
    m = max(1, min(10, n // 10 if n >= 10 else 3))
    n_rows = n

    # Deterministic generation of matrix arr with values in [0, 1e9]
    MOD = 10**9 + 7  # large prime for pseudo-random-like but deterministic pattern

    def gen_value(i, j):
        # Simple deterministic hash-like arithmetic, bounded to [0, 1e9]
        v = (i * 1315423911 ^ (j * 2654435761)) & 0xFFFFFFFF
        return v % 1000000001  # values in [0, 1e9]

    arr = tuple(
        tuple(gen_value(i, j) for j in range(m))
        for i in range(n_rows)
    )

    lower_bound = 0
    upper_bound = int(1e9) + 1
    mask = (1 << m) - 1
    ans = (0, 0)

    def can_upper(mid):
        nonlocal ans
        d = {}
        for i in range(n_rows):
            bit = 0
            row = arr[i]
            for j in range(m):
                if row[j] >= mid:
                    bit |= 1 << j
            d[bit] = i

        keys = tuple(d.keys())
        for i in range(len(keys)):
            a1 = keys[i]
            for j in range(i, len(keys)):
                a2 = keys[j]
                if (a1 | a2) == mask:
                    ans = (d[a1], d[a2])
                    return True
        return False

    while upper_bound - lower_bound > 1:
        middle = (upper_bound + lower_bound) >> 1
        if can_upper(middle):
            lower_bound = middle
        else:
            upper_bound = middle

    # Keep same observable behavior pattern: print two 1-based indices
    print(ans[0] + 1, ans[1] + 1)


if __name__ == "__main__":
    # Example call; adjust n to scale input size
    main(100)