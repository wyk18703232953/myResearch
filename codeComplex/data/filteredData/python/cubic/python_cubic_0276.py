def main(n):
    # Interpret n as the maximum size for r, g, b, capped by 200 (since dp is 201^3)
    max_size = min(max(1, n), 200)

    # Deterministically derive r, g, b from n
    # They are all at least 1 and at most max_size
    r = (n % max_size) + 1
    g = ((2 * n) % max_size) + 1
    b = ((3 * n) % max_size) + 1

    # Ensure they do not exceed 200 because dp is [201][201][201]
    r = min(r, 200)
    g = min(g, 200)
    b = min(b, 200)

    # Deterministically generate R, G, B lists of the required sizes
    # Original program expects:
    # - first line: r g b
    # - next: r integers for R (then prefixed with 0 and sorted)
    # - next: g integers for G
    # - next: b integers for B
    # We construct simple arithmetic sequences.
    R = [i for i in range(1, r + 1)]
    G = [2 * i for i in range(1, g + 1)]
    B = [3 * i for i in range(1, b + 1)]

    # Match original transformation: prepend 0 and sort
    R = [0] + R
    G = [0] + G
    B = [0] + B
    R.sort()
    G.sort()
    B.sort()

    # dp dimensions are fixed as in original (201^3)
    dp = [[[0] * 201 for _ in range(201)] for _ in range(201)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                x = dp[i - 1][j - 1][k] + R[i] * G[j] if i * j else 0
                y = dp[i][j - 1][k - 1] + G[j] * B[k] if j * k else 0
                z = dp[i - 1][j][k - 1] + R[i] * B[k] if i * k else 0
                current = dp[i][j][k]
                if x > current:
                    current = x
                if y > current:
                    current = y
                if z > current:
                    current = z
                dp[i][j][k] = current

    result = dp[r][g][b]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)