import sys

INF = int(1e8)

def around(r, c, n, m):
    a = []
    # up, right, down, left
    for i, j in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)):
        if 0 <= i < n and 0 <= j < m:
            a.append((i, j))
    return a

def solve(n, m, k, right, down):
    pdist = [[0] * m for _ in range(n)]
    if k & 1:
        return [[-1] * m for _ in range(n)]
    for _ in range(k // 2):
        dist = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                adist = []
                for ip, jp in around(i, j, n, m):
                    if ip == i:
                        if jp > j:
                            w = right[i][j]

                        else:
                            w = right[i][jp]

                    else:
                        if ip > i:
                            w = down[i][j]

                        else:
                            w = down[ip][j]
                    adist.append(pdist[ip][jp] + w)
                dist[i][j] = min(adist)
        pdist = dist
    for i in range(n):
        for j in range(m):
            pdist[i][j] *= 2
    return pdist

def generate_data(n):
    # Interpret n as grid size; keep k small relative to n for complexity scaling.
    # Ensure n >= 2 for a meaningful grid.
    if n < 2:
        n = 2
    # Use a square grid n x n
    rows = n
    cols = n
    # Let k grow with n but stay even
    k = (n // 2) * 2
    if k == 0:
        k = 2
    # Deterministic edge weights based on indices
    right = [[(i + j + 1) for j in range(cols - 1)] for i in range(rows)]
    down = [[(i * cols + j + 1) for j in range(cols)] for i in range(rows - 1)]
    return rows, cols, k, right, down

def main(n):
    rows, cols, k, right, down = generate_data(n)
    result = solve(rows, cols, k, right, down)
    for row in result:
        # print(*row)
        pass
if __name__ == "__main__":
    # Example deterministic call; change 10 to other values for experiments
    main(10)