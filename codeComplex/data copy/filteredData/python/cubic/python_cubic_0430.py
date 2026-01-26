def main(n):
    from math import inf

    # Map n to grid size and k
    # Ensure at least 1x1 grid and even k for non-trivial behavior
    rows = max(1, n)
    cols = max(1, n)
    k = max(2, 2 * (n // 2))  # ensure k is even and >= 2

    # Deterministic generation of hor (rows x (cols-1)) and ver ((rows-1) x cols)
    hor = [[(i + j + 1) % 10 + 1 for j in range(cols - 1)] for i in range(rows)]
    ver = [[(i * 2 + j + 3) % 10 + 1 for j in range(cols)] for i in range(rows - 1)]

    if k % 2:
        ml = [[-1 for _ in range(cols)] for _ in range(rows)]
        for row in ml:
            # print(*row)
            pass
        return

    k //= 2
    dp = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(k + 1)]
    for f in range(1, k + 1):
        for i in range(rows):
            for j in range(cols):
                a = inf
                if i != 0:
                    a = min(a, 2 * ver[i - 1][j] + dp[f - 1][i - 1][j])
                if i != rows - 1:
                    a = min(a, 2 * ver[i][j] + dp[f - 1][i + 1][j])
                if j != 0:
                    a = min(a, 2 * hor[i][j - 1] + dp[f - 1][i][j - 1])
                if j != cols - 1:
                    a = min(a, 2 * hor[i][j] + dp[f - 1][i][j + 1])
                dp[f][i][j] = a

    for row in dp[-1]:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)