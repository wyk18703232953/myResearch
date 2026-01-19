def main(n):
    if n <= 0:
        return

    prob = [[0.0] * n for _ in range(n)]
    for i in range(n):
        row_sum = 0.0
        for j in range(n):
            if i == j:
                prob[i][j] = 0.0
            else:
                prob[i][j] = ((i + 1) * (j + 2)) % (n + 3) + 1.0
                row_sum += prob[i][j]
        if row_sum > 0:
            for j in range(n):
                if i != j:
                    prob[i][j] /= row_sum

    dp = [[0.0] * (1 << n) for _ in range(n)]
    dp[0][1] = 1.0

    for mask in range(3, 1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if i != j and (mask & (1 << j)):
                    dp[i][mask] = max(
                        dp[i][mask],
                        dp[i][mask - (1 << j)] * prob[i][j]
                        + dp[j][mask - (1 << i)] * prob[j][i]
                    )

    result = max(dp[i][(1 << n) - 1] for i in range(n))
    print(result)


if __name__ == "__main__":
    main(4)