def main(n):
    # n controls the size: we construct arrays of length n and k = n//2
    if n <= 0:
        # print(0)
        pass
        return

    k = max(1, n // 2)

    # Deterministic construction of l, f, h
    # l: n integers
    l = [(i % (k + 1)) + 1 for i in range(n)]

    # f: n integers (same value range, but shifted pattern)
    f = [((i * 2) % (k + 1)) + 1 for i in range(n)]

    # h: k integers
    h = [((i + 1) * (i + 2)) % 1000 for i in range(k)]

    # Reproduce original logic
    d1 = dict({(a, 0) for a in f})
    d2 = dict({(a, 0) for a in f})

    for a in l:
        if a in d1:
            d1[a] += 1
    for a in f:
        d2[a] += 1

    # Original DP dimensions: dp[520][520*12]
    # We keep them fixed to preserve algorithm structure for complexity experiments
    max_x = 520
    max_y = 520 * 12

    dp = [[0 for _ in range(max_y)] for _ in range(max_x)]

    # Triple loop as in original code
    # Note: loops are based on original 'n' and 'k' from input;
    # here we use constructed n, k but dp size is fixed as in original.
    for x in range(n + 1):
        if x + 1 >= max_x:
            break
        for y in range(n * k + 1):
            if y >= max_y:
                break
            base = dp[x][y]
            for i in range(k + 1):
                yi = y + i
                if yi >= max_y:
                    break
                dp[x + 1][yi] = max(dp[x + 1][yi], base + (0 if i == 0 else h[i - 1]))

    ss = 0
    for i in d1:
        x_idx = d2[i]
        y_idx = d1[i]
        if x_idx < max_x and y_idx < max_y:
            ss += dp[x_idx][y_idx]
    # print(ss)
    pass
if __name__ == "__main__":
    main(50)