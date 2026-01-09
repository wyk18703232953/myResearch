def main(n):
    # Interpret n as grid size; k as an even path length proportional to n
    # Ensure at least 1x1 grid
    n = max(1, n)
    m = n
    # Choose an even k; scale with n to exercise the DP.
    # For example k = 2 * n (must be even).
    k = 2 * n
    if k & 1:
        res = [[-1] * m for _ in range(n)]
        for row in res:
            # print(*row)
            pass
        return

    # Deterministic weight generation
    # right[i][j]: weight from (i,j) to (i,j+1), for j in [0, m-2]
    # down[i][j]: weight from (i,j) to (i+1,j), for i in [0, n-2]
    right = [[0] * m for _ in range(n)]
    down = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # Only meaningful for j < m-1, but we fill all deterministically
            # Example deterministic formula:
            right[i][j] = (i + 1) * (j + 2)

    for i in range(n - 1):
        for j in range(m):
            # Only meaningful for i < n-1
            down[i][j] = (i + 2) * (j + 1)

    # Initialize DP array
    half_k = k // 2
    INF = float('inf')
    mem = [[[INF] * (half_k + 1) for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            mem[i][j][0] = 0

    for step in range(1, half_k + 1):
        for i in range(n):
            for j in range(m):
                best = INF
                # Up
                if i > 0:
                    cost = mem[i - 1][j][step - 1] + down[i - 1][j]
                    if cost < best:
                        best = cost
                # Down
                if i < n - 1:
                    cost = mem[i + 1][j][step - 1] + down[i][j]
                    if cost < best:
                        best = cost
                # Left
                if j > 0:
                    cost = mem[i][j - 1][step - 1] + right[i][j - 1]
                    if cost < best:
                        best = cost
                # Right
                if j < m - 1:
                    cost = mem[i][j + 1][step - 1] + right[i][j]
                    if cost < best:
                        best = cost
                mem[i][j][step] = best

    for i in range(n):
        row = [mem[i][j][half_k] * 2 for j in range(m)]
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)