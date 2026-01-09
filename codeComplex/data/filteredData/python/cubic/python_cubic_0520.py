def main(n):
    # Interpret n as grid size parameter: n_rows = n, m_cols = n, steps k = 2*n (even)
    # This keeps structure similar while making everything depend deterministically on n.
    if n <= 0:
        return
    rows = n
    cols = n
    steps = 2 * n  # guaranteed even

    # Generate deterministic right and down cost matrices
    # right: rows x cols, but only cols-1 effective; we still allocate full as original
    right = [[0] * cols for _ in range(rows)]
    down = [[0] * cols for _ in range(rows)]

    # Fill right costs: deterministic arithmetic pattern
    # Use small positive integers so values are manageable but non-trivial.
    for i in range(rows):
        for j in range(cols):
            # e.g., cost depends on row and column indices
            right[i][j] = (i + j + 1) % 7 + 1

    # Fill down costs: rows-1 effective, but allocate full as in original
    for i in range(rows - 1):
        for j in range(cols):
            down[i][j] = (i * 3 + j * 2 + 2) % 9 + 1

    # If steps is odd, original logic prints -1 grid; here steps is always even for determinism
    if steps & 1:
        for _ in range(rows):
            # print(*([-1] * cols))
            pass
        return

    # mem dimensions follow original: (rows+1) x (cols+1)
    mem = [[float('inf') for _ in range(cols + 1)] for _ in range(rows + 1)]
    for i in range(rows):
        for j in range(cols):
            mem[i][j] = 0

    half_k = steps // 2
    for _ in range(1, half_k + 1):
        mem0 = [[float('inf') for _ in range(cols + 1)] for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                up = mem[i - 1][j] + (down[i - 1][j] if i - 1 >= 0 else float('inf'))
                down_cost = mem[i + 1][j] + (down[i][j] if i + 1 < rows else float('inf'))
                left = mem[i][j - 1] + (right[i][j - 1] if j - 1 >= 0 else float('inf'))
                right_cost = mem[i][j + 1] + (right[i][j] if j + 1 < cols else float('inf'))
                mem0[i][j] = min(up, down_cost, left, right_cost)
        mem = mem0

    for i in range(rows):
        row_res = [int(mem[i][x] * 2) if mem[i][x] != float('inf') else -1 for x in range(cols)]
        # print(*row_res)
        pass
if __name__ == "__main__":
    main(5)