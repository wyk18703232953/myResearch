def main(n):
    # Map n to matrix dimensions and number of test cases
    # Choose small N so 2^N DP is tractable; let N = min(8, max(1, n // 2))
    N = min(8, max(1, n // 2))
    M = max(1, n - N)
    T = max(1, n // 3)

    results = []

    for t in range(T):
        # Deterministic matrix X of size N x M
        # Example pattern: X[i][j] = (i * 17 + j * 31 + t * 7) % 100
        X = [[(i * 17 + j * 31 + t * 7) % 100 for j in range(M)] for i in range(N)]

        dp = [[0] * (1 << N) for _ in range(M + 1)]

        for j in range(M):
            for mask in range(1 << N):
                maskpre = mask
                while maskpre >= 0:
                    maskpre &= mask
                    ma = 0
                    for k in range(N):
                        s = 0
                        for i in range(N):
                            if ((maskpre >> i) & 1) == 0 and ((mask >> i) & 1):
                                s += X[i - k][j]
                        if s > ma:
                            ma = s
                    cur = dp[j][maskpre] + ma
                    if cur > dp[j + 1][mask]:
                        dp[j + 1][mask] = cur
                    maskpre -= 1

        results.append(dp[-1][-1])

    # Aggregate results to produce a single deterministic output
    # For example, print the sum of all test case answers.
    total = 0
    for v in results:
        total += v
    print(total)


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)