import sys


def main(n):
    if n <= 0:
        return

    # Map n to grid size and steps:
    # n controls both rows/cols and k. This is deterministic and scalable.
    rows = n
    cols = n
    k = 2 * ((n % 5) + 1)  # always even, in [2, 10]

    # Precompute globals used by valid()
    global dx, dy
    dx, dy = (0, 1, 0, -1, 1, -1, 1, -1), (1, 0, -1, 0, 1, -1, -1, 1)

    # Define valid using current rows/cols
    def valid(x, y):
        return -1 < x < rows and -1 < y < cols

    # Deterministic construction of right and down edge weights
    right = [[0] * cols for _ in range(rows)]
    down = [[0] * cols for _ in range(rows)]

    # Right edges: row i, column j connects (i,j) -> (i,j+1)
    # Use simple arithmetic based on indices
    for i in range(rows):
        for j in range(cols):
            # Any non-negative weight; keep small to avoid overflow noise
            right[i][j] = (i + j + 1)

    # Down edges: row i, column j connects (i,j) -> (i+1,j)
    for i in range(rows - 1):
        for j in range(cols):
            down[i][j] = (i * 2 + j + 1)

    # DP memory: mem[i][j][t] = min cost to reach (i,j) in t steps
    half = k // 2
    mem = [[[float('inf')] * (half + 1) for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            mem[i][j][0] = 0

    for step in range(1, half + 1):
        for i in range(rows):
            for j in range(cols):
                ans = []
                if valid(i - 1, j):
                    ans.append(mem[i - 1][j][step - 1] + down[i - 1][j])
                if valid(i + 1, j):
                    ans.append(mem[i + 1][j][step - 1] + down[i][j])
                if valid(i, j - 1):
                    ans.append(mem[i][j - 1][step - 1] + right[i][j - 1])
                if valid(i, j + 1):
                    ans.append(mem[i][j + 1][step - 1] + right[i][j])
                mem[i][j][step] = min(ans)

    out_lines = []
    for i in range(rows):
        row_vals = [str(int(mem[i][x][-1] * 2)) for x in range(cols)]
        out_lines.append(" ".join(row_vals))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    # Example deterministic call; adjust n to scale the experiment.
    main(5)