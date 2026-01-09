def main(n):
    # Interpret n as grid size; also define m and K deterministically from n
    # For scalability tests you can vary n; m and K scale with n deterministically
    m = n
    K = max(0, n // 2) * 2  # ensure K is even for meaningful computation

    # Deterministic generation of edges input structure
    # Original program expects:
    # First line: n, m, K
    # Next n lines: m integers (horizontal edges between columns)
    # Next n-1 lines: m integers (vertical edges between rows)

    # Generate horizontal edges weights: n rows, each with m integers
    horiz = [[(i * m + j) % 7 + 1 for j in range(m)] for i in range(n)]
    # Generate vertical edges weights: (n-1) rows, each with m integers
    vert = [[(i * m + j) % 5 + 1 for j in range(m)] for i in range(n - 1)]

    # Build edges structure exactly as original program
    edges = []
    for i in range(n):
        edges.append([[]])
        lis = horiz[i]
        for j in range(m - 1):
            edges[i][j].append((1, 0, lis[j]))
            edges[i].append([])
            edges[i][j + 1].append((-1, 0, lis[j]))
    for i in range(n - 1):
        lis = vert[i]
        for j in range(m):
            edges[i][j].append((0, 1, lis[j]))
            edges[i + 1][j].append((0, -1, lis[j]))

    if K % 2 == 1:
        lis = [[-1] * m for _ in range(n)]

    else:
        lis = [[0] * m for _ in range(n)]
        for _ in range(1, (K // 2) + 1):
            new_lis = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    dist = []
                    for e in edges[i][j]:
                        dist.append(e[2] + lis[i + e[1]][j + e[0]])
                    new_lis[i][j] = min(dist)
            lis = new_lis
        for i in range(n):
            for j in range(m):
                lis[i][j] *= 2

    for row in lis:
        # print(*row)
        pass
if __name__ == "__main__":
    main(10)