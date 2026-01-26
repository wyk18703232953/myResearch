def main(n):
    from collections import defaultdict

    # Interpret n as N (length of sequence)
    N = max(1, n)

    # Deterministic generation of X of length N
    # Example pattern: X[i] = (i % 5)
    X = [(i % 5) for i in range(N)]

    dp = defaultdict(lambda: -1)
    M = 1000001

    for i in range(N):
        dp[i + M] = X[i]

    for i in range(2, N + 1):
        for j in range(N - i + 1):
            for k in range(1, i):
                u, v = dp[j + M * k], dp[j + k + M * (i - k)]
                if u == -1 or v == -1 or u != v:
                    continue
                dp[j + M * i] = u + 1
                break

    dp2 = [0] * (N + 1)
    for i in range(N):
        dp2[i + 1] = dp2[i] + 1
        for j in range(i + 1):
            if dp[j + (i + 1 - j) * M] == -1:
                continue
            dp2[i + 1] = min(dp2[i + 1], dp2[j] + 1)

    # print(dp2[-1])
    pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(1000)