def main(n):
    # Deterministic parameter mapping
    # k: small constant relative to n, at least 1
    k = max(1, n // 5)
    # lengths of lists follow original pattern: l, f, h are all of length n
    l_len = n
    f_len = n
    h_len = k

    # Deterministic data generation
    # l: length n
    l = [(i * 3 + 1) % (n + k + 7) for i in range(l_len)]
    # f: length n, values chosen from same range to create overlaps with l
    f = [(i * 5 + 2) % (n + k + 7) for i in range(f_len)]
    # h: length k, non-negative incremental pattern
    h = [(i + 1) for i in range(h_len)]

    # Core logic (unchanged algorithmically)
    d1 = dict({(a, 0) for a in f})
    d2 = dict({(a, 0) for a in f})
    for a in l:
        if a in d1:
            d1[a] += 1
    for a in f:
        d2[a] += 1

    max_x = n
    max_y = n * k
    dp_rows = max_x + 1
    dp_cols = max_y + k + 1  # ensure y+i is always in range

    dp = [[0 for _ in range(dp_cols)] for _ in range(dp_rows)]

    for x in range(max_x):
        for y in range(max_y + 1):
            base = dp[x][y]
            for i in range(k + 1):
                ny = y + i
                if ny < dp_cols:
                    dp[x + 1][ny] = max(dp[x + 1][ny], base + (0 if i == 0 else h[i - 1]))

    ss = 0
    for key in d1:
        if d2[key] < dp_rows and d1[key] < dp_cols:
            ss += dp[d2[key]][d1[key]]
    # print(ss)
    pass
if __name__ == "__main__":
    main(10)