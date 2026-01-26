import sys
from collections import deque

def main(n):
    # n controls grid size; ensure minimum size
    n = max(2, n)
    m = n

    # Deterministic construction of k and pairs:
    # use k = n, and select n distinct cells along a pattern
    k = n
    a = [[0] * m for _ in range(n)]
    dq = deque()

    # Build "line" equivalent as in the original input:
    # original expects 2*k integers (1-based indices), then subtracts 1
    # Here we generate k positions deterministically:
    line = []
    for i in range(k):
        # simple deterministic mapping: row and col based on i
        r = i % n
        c = (i * 2) % m
        line.append(r)
        line.append(c)

    # Apply the same logic as the original code (using 0-based indices directly)
    for i in range(0, 2 * k, 2):
        a[line[i]][line[i + 1]] = 1
        dq.append((line[i], line[i + 1]))

    x, y = -1, -1
    while dq:
        x, y = dq.popleft()
        for tx, ty in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= tx < n and 0 <= ty < m and not a[tx][ty]:
                a[tx][ty] = 1
                dq.append((tx, ty))

    # Return the final coordinates in 1-based form to mirror the original print
    # print(f"{x + 1} {y + 1}")
    pass
    return x + 1, y + 1

if __name__ == "__main__":
    # example deterministic call
    main(5)