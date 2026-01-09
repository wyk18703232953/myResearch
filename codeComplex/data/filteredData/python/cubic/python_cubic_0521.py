def main(n):
    # Interpret n as grid dimension; k grows with n for scalability
    if n <= 0:
        return
    m = n
    k = 2 * ((n % 5) + 1)  # always even and >= 2

    # Deterministic generation of right and down cost matrices
    # right: n x m
    right = [[(i * m + j) % 7 + 1 for j in range(m)] for i in range(n)]
    # down: (n-1) x m
    if n > 1:
        down = [[(i * m + j * 3) % 9 + 1 for j in range(m)] for i in range(n - 1)]

    else:
        down = [[0] * m for _ in range(0)]

    # If k is odd (not here) would output -1, but k is constructed even
    # Prepare mem arrays
    mem = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            mem[i][j] = 0

    # DP transitions for k/2 steps
    steps = k // 2
    for _ in range(1, steps + 1):
        mem0 = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                best = float('inf')
                # up
                if i - 1 >= 0:
                    cost = mem[i - 1][j] + down[i - 1][j]
                    if cost < best:
                        best = cost
                # down
                if i + 1 < n:
                    cost = mem[i + 1][j] + down[i][j]
                    if cost < best:
                        best = cost
                # left
                if j - 1 >= 0:
                    cost = mem[i][j - 1] + right[i][j - 1]
                    if cost < best:
                        best = cost
                # right
                if j + 1 < m:
                    cost = mem[i][j + 1] + right[i][j]
                    if cost < best:
                        best = cost
                mem0[i][j] = best
        mem = mem0

    # Output result (kept for determinism and to prevent optimization away)
    for i in range(n):
        row = [mem[i][x] * 2 for x in range(m)]
        # print(*row)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scalability experiments
    main(5)