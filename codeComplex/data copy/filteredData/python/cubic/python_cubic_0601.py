def main(n):
    # Interpret n as both number of rows and columns; k scales with n
    m = n
    k = n // 2

    # Deterministic generation of input data:
    # For each of n rows, create a binary string of length m using simple arithmetic pattern
    cls = []
    for i in range(n):
        row_positions = []
        for j in range(m):
            # Example pattern: 1 if (i + j) is even, else 0
            if (i + j) % 2 == 0:
                row_positions.append(j)
        cls.append(row_positions)

    dp = [[n * m] * (k + 1) for _ in range(n + 1)]
    dp.append([0] * (k + 1))

    for i in range(n):
        row = cls[i]
        c2l = [m + 1] * (m + 1)
        c2l[0] = row[-1] - row[0] + 1 if row else 0
        c2l[len(row)] = 0
        for r in range(len(row)):
            for l in range(r + 1):
                length = row[r] - row[l] + 1
                removed = len(row) - (r - l + 1)
                if length < c2l[removed]:
                    c2l[removed] = length
        for j in range(k + 1):
            for c, l in enumerate(c2l):
                if j + c <= k and l < m + 1:
                    val = dp[i - 1][j + c] + l
                    if val < dp[i][j]:
                        dp[i][j] = val

    result = min(dp[n - 1])
    # print(result)
    pass
if __name__ == "__main__":
    main(10)