def main(n):
    # Interpret n as grid size: n x n grid, k proportional to n
    rows = n
    cols = n
    k = 2 * n  # even, scales with n

    from collections import defaultdict

    dic = defaultdict(lambda: {})

    # Deterministic weight generator for horizontal edges
    # For row i, between column j and j+1, weight = (i + j + 1)
    for i in range(rows):
        line = tuple((i + j + 1) for j in range(cols - 1))
        for j in range(cols - 1):
            w = line[j] * 2
            dic[i * cols + j][i * cols + j + 1] = w
            dic[i * cols + j + 1][i * cols + j] = w

    # Deterministic weight generator for vertical edges
    # Between row i and i+1 at column j, weight = (i + j + 1)
    for i in range(rows - 1):
        line = tuple((i + j + 1) for j in range(cols))
        for j in range(cols):
            w = line[j] * 2
            dic[i * cols + j][(i + 1) * cols + j] = w
            dic[(i + 1) * cols + j][i * cols + j] = w

    if k % 2 != 0:
        result = []
        for _ in range(rows):
            result.append(' '.join(('-1',) * cols))
        # print('\n'.join(result))
        pass

    else:
        prev = []
        di = (1, 0, -1, 0)
        dj = (0, 1, 0, -1)
        for _ in range(rows):
            prev.append((0,) * cols)

        for _ in range(k // 2):
            new = []
            for _ in range(rows):
                new.append([100_000_000] * cols)

            for num in dic:
                i = num // cols
                j = num % cols
                for idx in range(4):
                    ii = i + di[idx]
                    jj = j + dj[idx]
                    if not (0 <= ii < rows and 0 <= jj < cols):
                        continue
                    cost = prev[i][j] + dic[i * cols + j][ii * cols + jj]
                    if cost < new[ii][jj]:
                        new[ii][jj] = cost

            prev = new

        result = []
        for i in range(rows):
            result.append(' '.join(map(str, prev[i])))
        # print('\n'.join(result))
        pass
if __name__ == "__main__":
    main(5)