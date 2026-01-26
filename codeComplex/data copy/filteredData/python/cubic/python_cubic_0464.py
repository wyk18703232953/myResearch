def main(n):
    # Interpret n as both number of rows and columns: n x n grid
    # Also set k as an even value depending on n for scalability
    rows = n
    cols = n
    k = 2 * max(1, n // 2)  # ensure k is even and scalable with n

    # Core logic from original slv(), adapted to deterministic data
    if k % 2 != 0:
        for _ in range(rows):
            # print(*([-1] * cols))
            pass
        return

    half_k = k // 2

    # DP dimensions: (half_k+1) x rows x cols
    DP = [[[0] * cols for _ in range(rows)] for _ in range(half_k + 1)]

    # Graph G: for each cell (i,j), store list of (cost, x, y) to neighbor
    G = [[[] for _ in range(cols)] for _ in range(rows)]

    # Deterministic horizontal edge costs
    # For row i, between (i,j) and (i,j+1)
    # Example cost function: cost = (i + j + 1)
    for i in range(rows):
        for j in range(cols - 1):
            cost = i + j + 1
            G[i][j].append((cost, i, j + 1))
            G[i][j + 1].append((cost, i, j))

    # Deterministic vertical edge costs
    # For between (i,j) and (i+1,j)
    # Example cost function: cost = (i + j + 2)
    for i in range(rows - 1):
        for j in range(cols):
            cost = i + j + 2
            G[i][j].append((cost, i + 1, j))
            G[i + 1][j].append((cost, i, j))

    # DP transitions
    for p in range(1, half_k + 1):
        for u in range(rows):
            for v in range(cols):
                DP[p][u][v] = min(DP[p - 1][x][y] + cost for (cost, x, y) in G[u][v])

    # Output final answers (multiplied by 2 as in original code)
    for i in range(rows):
        ans = [DP[half_k][i][j] * 2 for j in range(cols)]
        # print(*ans)
        pass
if __name__ == "__main__":
    # Example call; adjust n as needed for experiments
    main(5)