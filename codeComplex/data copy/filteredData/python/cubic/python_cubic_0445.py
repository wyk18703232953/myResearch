from array import array

def main(n):
    # Interpret n as grid size; ensure at least 1x1
    if n < 1:
        n = 1
    k = n  # step count parameter grows with n
    size = n
    m = size

    # Deterministic construction of left and down arrays
    # left: n rows, each with m-1 entries; pad to length m with last value for simplicity
    left = []
    for i in range(size):
        row = [i * 3 + j * 2 + 1 for j in range(m - 1)]
        if m > 1:
            row.append(row[-1])

        else:
            row.append(1)
        left.append(array("i", row))

    # down: n-1 rows, each with m entries
    down = []
    for i in range(size - 1):
        row = [(i + 1) * 5 + j * 4 + 2 for j in range(m)]
        down.append(array("i", row))

    dp = [array("i", [(-1 if k & 1 else 0) for _ in range(m)]) for _ in range(size)]
    if k & 1 == 0:
        for _ in range(k // 2):
            dp1 = [array("i", [10 ** 8 for _ in range(m)]) for _ in range(size)]
            for i in range(size):
                for j in range(m):
                    if j > 0:
                        dp1[i][j] = min(dp1[i][j], dp[i][j - 1] + 2 * left[i][j - 1])
                    if j < m - 1:
                        dp1[i][j] = min(dp1[i][j], dp[i][j + 1] + 2 * left[i][j])
                    if i > 0:
                        dp1[i][j] = min(dp1[i][j], dp[i - 1][j] + 2 * down[i - 1][j])
                    if i < size - 1:
                        dp1[i][j] = min(dp1[i][j], dp[i + 1][j] + 2 * down[i][j])
            dp = dp1

    for row in dp:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)