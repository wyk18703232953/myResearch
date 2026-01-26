def main(n):
    # n is the size N
    N = max(1, int(n))

    # Deterministic construction of arr of length N
    # Pattern: repeat 1..5
    arr = [(i % 5) + 1 for i in range(N)]

    dp = [[-1 for _ in range(N)] for _ in range(N)]

    for size in range(1, N + 1):
        for i in range(N - size + 1):
            j = i + size - 1
            if i == j:
                dp[i][j] = arr[i]

            else:
                for k in range(i, j):
                    if dp[i][k] != -1 and dp[i][k] == dp[k + 1][j]:
                        dp[i][j] = dp[i][k] + 1

    dp2 = [x + 1 for x in range(N)]

    for i in range(N):
        for k in range(i + 1):
            if dp[k][i] != -1:
                if k == 0:
                    dp2[i] = 1

                else:
                    dp2[i] = min(dp2[i], dp2[k - 1] + 1)

    # print(dp2[N - 1])
    pass
if __name__ == "__main__":
    # Example call for experimental purpose
    main(10)