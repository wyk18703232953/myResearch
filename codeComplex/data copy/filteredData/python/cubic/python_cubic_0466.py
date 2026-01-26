def main(n):
    # Map n to problem parameters:
    # Use n as both number of rows and columns; keep k proportional to n and even.
    rows = n
    cols = n
    K = 2 * n  # ensures K is even

    # Deterministic generation of horizontal and vertical edge weights
    # horizontal: rows x (cols-1)
    horizontal = [
        [(i + j + 1) % 7 + 1 for j in range(cols - 1)]
        for i in range(rows)
    ]
    # vertical: (rows-1) x cols
    vertical = [
        [(i * 3 + j * 5 + 2) % 9 + 1 for j in range(cols)]
        for i in range(rows - 1)
    ]

    n_local, m, k = rows, cols, K

    if k % 2 or max(n_local, m) == 1:
        result = [["-1"] * m for _ in range(n_local)]
        return result

    half = k // 2
    dp = [[[0] * (half + 1) for _ in range(m)] for _ in range(n_local)]

    for length in range(1, half + 1):
        for i in range(n_local):
            for j in range(m):
                left_path = 10e7 if j == 0 else horizontal[i][j - 1] + dp[i][j - 1][length - 1]
                right_path = 10e7 if j == m - 1 else horizontal[i][j] + dp[i][j + 1][length - 1]
                top_path = 10e7 if i == 0 else vertical[i - 1][j] + dp[i - 1][j][length - 1]
                bottom_path = 10e7 if i == n_local - 1 else vertical[i][j] + dp[i + 1][j][length - 1]
                dp[i][j][length] = min(left_path, right_path, top_path, bottom_path)

    result = [[dp[i][j][half] * 2 for j in range(m)] for i in range(n_local)]
    return result


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    n = 5
    ans = main(n)
    for row in ans:
        # print(*row)
        pass