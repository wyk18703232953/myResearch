def main(n):
    from collections import deque

    # Scale mapping:
    # n -> grid of size (n x n)
    # k (number of initially filled cells) = max(1, min(n*n, n))
    rows = n
    cols = n
    k = max(1, min(rows * cols, n))

    # Deterministic generation of initial filled cells:
    # pick k distinct cells along a deterministic pattern
    initial_cells = []
    for i in range(k):
        x = (i * 2) % rows
        y = (i * 3) % cols
        initial_cells.append((x, y))

    # Original logic begins (adapted to use generated data)
    a = [[0] * cols for _ in range(rows)]
    dq = deque()
    for x, y in initial_cells:
        if a[x][y] == 0:
            a[x][y] = 1
            dq.append((x, y))

    x, y = -1, -1
    while dq:
        x, y = dq.popleft()
        for tx, ty in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= tx < rows and 0 <= ty < cols and not a[tx][ty]:
                a[tx][ty] = 1
                dq.append((tx, ty))

    # Return the final cell in 1-based coordinates (matching original program)
    return (x + 1, y + 1)


if __name__ == "__main__":
    # Example call for experimental purpose
    n = 100
    result = main(n)
    # print(result)
    pass