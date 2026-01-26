def main(n):
    # Interpret n as the dimension of a single n x n matrix and number of test cases T = n
    T = n if n > 0 else 1
    results = []

    for t in range(T):
        # For each test case, use the same n x n matrix size
        rows = n if n > 0 else 1
        cols = n if n > 0 else 1

        # Deterministically generate matrix a (rows x cols)
        # a[i][j] = (i * cols + j) % (rows + cols + 1)
        a = [[(i * cols + j) % (rows + cols + 1) for j in range(cols)] for i in range(rows)]

        x = [[a[i][j] for i in range(rows)] for j in range(cols)]
        x.sort(key=lambda xx: -max(xx))
        dp = [[0 for _ in range(1 << rows)] for _ in range(cols + 1)]

        for i in range(cols):
            for prev in range(1 << rows):
                for pres in range(1 << rows):
                    if prev ^ pres != prev + pres:
                        continue
                    ma = 0
                    for j in range(rows):
                        for st in range(rows):
                            if pres & (1 << st):
                                ma += x[i][(st + j) % rows]
                    new_mask = pres ^ prev
                    current = dp[i][prev] + ma
                    if current > dp[i + 1][new_mask]:
                        dp[i + 1][new_mask] = current

        results.append(dp[cols][(1 << rows) - 1])

    for res in results:
        print(res)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(3)