def main(n):
    # n is the number of states/players; also controls matrix size n x n
    if n <= 0:
        return

    # deterministic probability matrix probs[n][n]
    # example construction: probs[i][j] = ((i + 1) * (j + 2)) mod (n + 3), then normalized per row
    probs = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        row_raw = [((i + 1) * (j + 2)) % (n + 3) for j in range(n)]
        # ensure at least some non-zero mass; if all zero, fallback to uniform
        s = sum(row_raw)
        if s == 0:
            for j in range(n):
                probs[i][j] = 1.0 / n
        else:
            for j in range(n):
                probs[i][j] = row_raw[j] / s

    dp = [[0.0 for _ in range(1 << n)] for _ in range(n)]
    dp[0][(1 << n) - 1] = 1.0
    ak = [[] for _ in range(n + 1)]
    for i in range(1 << n):
        ak[bin(i).count("1")].append(i)
    for k in range(1, n):
        for ele in ak[n - k + 1]:
            for j in range(n):
                if ele & (1 << j):
                    for w in range(n):
                        if (ele & (1 << w)) and j != w:
                            dp[k][ele - (1 << j)] += (
                                dp[k - 1][ele] * probs[w][j]
                            ) / (((n - k + 1) * (n - k)) / 2.0)
    result = [dp[n - 1][1 << i] for i in range(n)]
    for x in result:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    # example deterministic call; adjust n here for experiments
    main(4)