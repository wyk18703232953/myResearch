def main(n):
    # Interpret n as the total size split among three arrays R, G, B
    # Ensure at least size 1 for each when n >= 3
    if n <= 0:
        # print(0)
        pass
        return

    # Simple deterministic split of n into r, g, b
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    if r == 0:
        r = 1
    if g == 0 and n >= 2:
        g = 1
    if b == 0 and n >= 3:
        b = 1

    # Re-adjust if sum exceeds n, which can only happen for very small n
    total = r + g + b
    while total > n and b > 1:
        b -= 1
        total -= 1
    while total > n and g > 1:
        g -= 1
        total -= 1
    while total > n and r > 1:
        r -= 1
        total -= 1

    # Deterministic generation of arrays
    # Use descending patterns so that after sorting(reverse=True) they remain the same
    R = [r * 2 - i for i in range(r)]
    G = [g * 3 - i for i in range(g)]
    B = [b * 5 - i for i in range(b)]

    # Core algorithm logic (unchanged except using generated R,G,B)
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for j in range(g - 1, -1, -1):
        for k in range(b - 1, -1, -1):
            dp[r][j][k] = G[j] * B[k] + dp[r][j + 1][k + 1]

    for i in range(r - 1, -1, -1):
        for k in range(b - 1, -1, -1):
            dp[i][g][k] = R[i] * B[k] + dp[i + 1][g][k + 1]

    for i in range(r - 1, -1, -1):
        for j in range(g - 1, -1, -1):
            dp[i][j][b] = R[i] * G[j] + dp[i + 1][j + 1][b]

    for i in range(r - 1, -1, -1):
        for j in range(g - 1, -1, -1):
            for k in range(b - 1, -1, -1):
                case1 = dp[i + 1][j][k]
                case2 = dp[i][j + 1][k]
                case3 = dp[i][j][k + 1]

                case4 = R[i] * G[j] + dp[i + 1][j + 1][k]
                case5 = R[i] * B[k] + dp[i + 1][j][k + 1]
                case6 = G[j] * B[k] + dp[i][j + 1][k + 1]

                dp[i][j][k] = max(case1, case2, case3, case4, case5, case6)

    # print(dp[0][0][0])
    pass
if __name__ == "__main__":
    # Example: run with a specific input scale n
    main(10)