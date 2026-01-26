def main(n):
    if n <= 0:
        return
    prob = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                prob[i][j] = 0.0
            else:
                prob[i][j] = ((i + 1) / (i + j + 2))
    dp = [[0.0] * n for _ in range(1 << n)]
    dp[1][0] = 1.0
    for mask in range(3, 1 << n):
        for i in range(n):
            if not (mask & (1 << i)):
                continue
            for j in range(n):
                if i != j and (mask & (1 << j)):
                    v = dp[mask - (1 << j)][i] * prob[i][j] + dp[mask - (1 << i)][j] * prob[j][i]
                    if v > dp[mask][i]:
                        dp[mask][i] = v
    print(max(dp[-1]))


if __name__ == "__main__":
    main(4)