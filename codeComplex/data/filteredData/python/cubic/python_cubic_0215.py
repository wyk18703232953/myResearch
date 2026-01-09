def main(n):
    # Interpret n as the size of each of the three arrays and dp dimensions
    # Original program: n is a list of 3 integers [n0, n1, n2]
    n0 = n
    n1 = n
    n2 = n

    # Deterministically generate three arrays u[0], u[1], u[2]
    # Use simple arithmetic sequences depending only on n and index
    u0 = [i + 1 for i in range(n0)]
    u1 = [2 * (i + 1) for i in range(n1)]
    u2 = [3 * (i + 1) for i in range(n2)]

    u = [u0, u1, u2]

    # Apply the same sorting as original code (descending)
    u[0].sort(reverse=True)
    u[1].sort(reverse=True)
    u[2].sort(reverse=True)

    dp = [[[0] * (n2 + 1) for _ in range(n1 + 1)] for _ in range(n0 + 1)]

    for i in range(n0 + 1):
        for j in range(n1 + 1):
            for k in range(n2 + 1):
                if i < n0 and j < n1:
                    val = dp[i][j][k] + u[0][i] * u[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if j < n1 and k < n2:
                    val = dp[i][j][k] + u[1][j] * u[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if i < n0 and k < n2:
                    val = dp[i][j][k] + u[0][i] * u[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val

    res = 0
    for u1 in dp:
        for u2 in u1:
            for x in u2:
                if x > res:
                    res = x

    # print(res)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to change input scale
    main(5)