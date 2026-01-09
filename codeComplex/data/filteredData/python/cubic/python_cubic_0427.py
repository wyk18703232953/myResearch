import math

def build_deterministic_input(n):
    if n < 1:
        n = 1
    # Define grid size based on n
    rows = n
    cols = n
    k = 2 * n  # ensure even, non-trivial path length
    # Horizontal edges: (rows) lines, each with cols-1 weights
    horizontal = []
    for y in range(rows):
        horizontal.append([(y + x + 1) % 7 + 1 for x in range(cols - 1)])
    # Vertical edges: (rows-1) lines, each with cols weights
    vertical = []
    for y in range(rows - 1):
        vertical.append([(2 * y + 3 * x + 2) % 9 + 1 for x in range(cols)])
    return rows, cols, k, horizontal, vertical

def main(n):
    nrows, mcols, k, horiz, vert = build_deterministic_input(n)

    M = [[[] for _ in range(mcols)] for _ in range(nrows)]
    S = [[-1] * mcols for _ in range(nrows)]

    # Build horizontal edges
    for y in range(nrows):
        L = horiz[y]
        for x in range(mcols - 1):
            w = L[x]
            M[y][x].append(((y, x + 1), w))
            M[y][x + 1].append(((y, x), w))

    # Build vertical edges
    for y in range(nrows - 1):
        L = vert[y]
        for x in range(mcols):
            w = L[x]
            M[y][x].append(((y + 1, x), w))
            M[y + 1][x].append(((y, x), w))

    if k % 2 == 0:
        for _ in range(k // 2):
            S2 = [[0] * mcols for _ in range(nrows)]
            for y in range(nrows):
                for x in range(mcols):
                    Mi = 10000000000000000000000
                    for ((a, b), p) in M[y][x]:
                        val = max(0, S[a][b]) + p
                        if val < Mi:
                            Mi = val
                    S2[y][x] = Mi
            S = S2
        for y in range(nrows):
            for x in range(mcols):
                S[y][x] *= 2

    for y in range(nrows):
        # print(' '.join(map(str, S[y])))
        pass
if __name__ == "__main__":
    main(5)