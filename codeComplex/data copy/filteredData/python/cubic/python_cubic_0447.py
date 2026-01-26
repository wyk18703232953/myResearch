def main(n):
    # Map n to problem dimensions.
    # Ensure positive sizes and even K for meaningful DP.
    if n < 2:
        n = 2
    N = n
    M = n
    K = 2 * (n // 2)

    # Deterministic generation of edge weights
    HEdge = [[(i + j) % 7 + 1 for j in range(M - 1)] for i in range(N)]
    if N > 1:
        VEdge = [[(i * 2 + j) % 9 + 1 for j in range(M)] for i in range(N - 1)]

    else:
        VEdge = []

    if K % 2:
        for _ in range(N):
            # print(*[-1] * M)
            pass
        return

    half_k = K // 2
    dp = [[[0] * M for _ in range(N)] for _ in range(half_k + 1)]
    INF = 10 ** 9

    for step in range(1, half_k + 1):
        prev_layer = dp[step - 1]
        curr_layer = dp[step]
        for i in range(N):
            for j in range(M):
                val1 = val2 = val3 = val4 = INF
                if i > 0:
                    val1 = prev_layer[i - 1][j] + VEdge[i - 1][j]
                if i < N - 1:
                    val2 = prev_layer[i + 1][j] + VEdge[i][j]
                if j > 0:
                    val3 = prev_layer[i][j - 1] + HEdge[i][j - 1]
                if j < M - 1:
                    val4 = prev_layer[i][j + 1] + HEdge[i][j]
                curr_layer[i][j] = min(val1, val2, val3, val4)

    for row in dp[half_k]:
        # print(*[x * 2 for x in row])
        pass
if __name__ == "__main__":
    main(5)