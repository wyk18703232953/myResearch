def main(n):
    # Interpret n as array length
    if n <= 0:
        return 0

    # Deterministically generate input array A of length n
    # Values in [1, 5] with a simple pattern
    N = n
    A = [(i % 5) + 1 for i in range(N)]

    dp = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = A[i]

    for X in range(2, N + 1):
        for i in range(N - X + 1):
            j = i + X - 1
            for k in range(i, j):
                if dp[i][k] == dp[k + 1][j] and dp[i][k] != -1:
                    dp[i][j] = dp[i][k] + 1
                    break

    ans = [10**9 + 1] * (N + 1)
    ans[0] = 0
    for i in range(1, N + 1):
        for k in range(1, i + 1):
            if dp[k - 1][i - 1] != -1:
                if ans[k - 1] + 1 < ans[i]:
                    ans[i] = ans[k - 1] + 1

    return ans[N]


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    # print(result)
    pass