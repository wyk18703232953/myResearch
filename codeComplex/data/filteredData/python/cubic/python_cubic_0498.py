def main(n):
    # Interpret n as both grid dimensions and K
    N = max(1, n)
    M = max(1, n)
    K = 2 * max(1, n)  # ensure K is even and scales with n

    # Deterministically generate edge weights
    colEdges = []
    for i in range(N):
        row = [1 + (i + j) % 9 for j in range(M - 1)]
        colEdges.append(row)

    rowEdges = []
    for i in range(N - 1):
        row = [1 + (i * 3 + j * 2) % 9 for j in range(M)]
        rowEdges.append(row)

    if K % 2:
        for _ in range(N):
            # print((" -1" * M).strip())
            pass
        return

    dp = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    p = [[[(i, j) for j in range(M)] for i in range(N)] for _ in range(2)]
    prev = 0

    for _ in range(K // 2):
        cur = prev ^ 1
        for i in range(N):
            for j in range(M):
                cand = (float('inf'), None)

                if j:
                    nxt = (dp[prev][i][j - 1] + colEdges[i][j - 1], p[prev][i][j - 1])
                    if nxt < cand:
                        cand = nxt
                if j < M - 1:
                    nxt = (dp[prev][i][j + 1] + colEdges[i][j], p[prev][i][j + 1])
                    if nxt < cand:
                        cand = nxt
                if i:
                    nxt = (dp[prev][i - 1][j] + rowEdges[i - 1][j], p[prev][i - 1][j])
                    if nxt < cand:
                        cand = nxt
                if i < N - 1:
                    nxt = (dp[prev][i + 1][j] + rowEdges[i][j], p[prev][i + 1][j])
                    if nxt < cand:
                        cand = nxt

                dp[cur][i][j], p[cur][i][j] = cand
        prev = cur

    for i in range(N):
        row_out = []
        for j in range(M):
            row_out.append(str(dp[prev][i][j] * 2))
        # print(" ".join(row_out))
        pass
if __name__ == "__main__":
    main(5)