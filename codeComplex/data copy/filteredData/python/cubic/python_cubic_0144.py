def main(n):
    # n controls the size N and the list A deterministically
    if n <= 0:
        return
    N = n
    A = [i % 7 + 1 for i in range(N)]

    dp = [[0] * N for _ in range(N)]
    for j in range(N):
        dp[j][0] = A[j]

    for l in range(1, N):
        for j in range(l, N):
            for k in range(j - l, j):
                if dp[k][k - j + l] == dp[j][j - k - 1] > 0:
                    dp[j][l] = 1 + dp[j][j - k - 1]
                    break

    dp = [None] + dp
    Dp = [0] * (N + 1)
    for j in range(1, N + 1):
        res = N
        for l in range(j):
            if dp[j][l]:
                res = min(res, 1 + Dp[j - l - 1])
        Dp[j] = res
    # print(Dp[N])
    pass
if __name__ == "__main__":
    main(10)