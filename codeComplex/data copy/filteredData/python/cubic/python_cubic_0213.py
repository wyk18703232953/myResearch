def main(n):
    # Interpret n as total length of three arrays R, G, B
    # Split n as evenly as possible into r, g, b
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # Ensure at least 1 element in each if n >= 3, otherwise allow zeros
    if n >= 3:
        if r == 0:
            r = 1
        if g == 0:
            g = 1
        if b == 0:
            b = 1

    # Regenerate n to match r+g+b so complexity is consistent
    # but keep the original split logic deterministic
    # R, G, B: deterministic increasing sequences
    R = [(i + 1) for i in range(r)]
    G = [(2 * (i + 1)) for i in range(g)]
    B = [(3 * (i + 1)) for i in range(b)]

    R.sort()
    G.sort()
    B.sort()

    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    val = dp[i][j][k] + R[i] * G[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < r and k < b:
                    val = dp[i][j][k] + R[i] * B[k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < g and k < b:
                    val = dp[i][j][k] + G[j] * B[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val

    # For timing experiments, it's useful to return the result instead of printing
    result = dp[r][g][b]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example: run with a specific scale n
    main(9)