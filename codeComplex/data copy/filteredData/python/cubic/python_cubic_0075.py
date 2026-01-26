def main(n):
    # Interpret n as the grid size N = M = n, and K = n deterministic points
    N = n
    M = n
    K = n

    # Deterministically generate K points (1-based indices in original code)
    # Pattern: (i % N + 1, (2 * i) % M + 1) for i in 0..K-1
    inputs = []
    for i in range(K):
        x = (i % N) + 1
        y = ((2 * i) % M) + 1
        inputs.extend([x, y])

    # Core algorithm logic (unchanged except removal of file I/O)
    map_max_dist = [[5000 for _ in range(M)] for _ in range(N)]
    p = 0
    while p <= K * 2 - 2:
        x, y = inputs[p] - 1, inputs[p + 1] - 1
        for r in range(N):
            for c in range(M):
                dist = abs(x - r) + abs(y - c)
                if dist < map_max_dist[r][c]:
                    map_max_dist[r][c] = dist
        p += 2

    max_val = 0
    max_index = (0, 0)
    for i in range(N):
        for j in range(M):
            if map_max_dist[i][j] > max_val:
                max_val = map_max_dist[i][j]
                max_index = (i, j)

    # Output in the same format as original code (1-based indices)
    # print("{} {}".format(max_index[0] + 1, max_index[1] + 1))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to change problem size
    main(10)