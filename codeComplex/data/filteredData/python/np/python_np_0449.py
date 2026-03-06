def main(n):
    from array import array

    # Map n to matrix dimensions:
    # For scalability, let m (number of columns) be at least 1 and at most, say, 20 (bitset limit)
    # and n be the number of rows. We can, for example, fix m = min(20, max(1, n // 2)).
    if n <= 0:
        return
    m = min(20, max(1, n // 2))
    rows = n

    # Deterministic matrix generation:
    # mat[i][j] = (i * 37 + j * 91) % 1000000007
    mat = [
        array('i', ((i * 37 + j * 91) % 1000000007 for j in range(m)))
        for i in range(rows)
    ]

    bit = [1 << i for i in range(m)]
    max_bit = 1 << m
    fullbit = max_bit - 1

    def solve(x):
        dp = array('i', [-1]) * max_bit
        for i in range(rows):
            mask = 0
            row = mat[i]
            for j, y in enumerate(row):
                if y >= x:
                    mask |= bit[j]
            dp[mask] = i

        for i in range(max_bit):
            if dp[i] == -1:
                continue
            for j in range(i, max_bit):
                if dp[j] != -1 and (i | j) == fullbit:
                    return dp[i], dp[j]

        return -1, -1

    ok, ng = 0, 10**9 + 1
    ans_i, ans_j = 1, 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) >> 1
        x, y = solve(mid)
        if x == -1:
            ng = mid
        else:
            ok = mid
            ans_i, ans_j = x + 1, y + 1

    print(ans_i, ans_j)


if __name__ == "__main__":
    main(10)