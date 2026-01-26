def main(n):
    # Interpret n as grid size and step parameter:
    # use n x n grid, k = 2 * n (always even to avoid trivial -1 case)
    rows = n
    cols = n
    k = 2 * n

    # Deterministic generation of H (horizontal weights) and V (vertical weights)
    # H: rows x (cols-1)
    H = [[(i * cols + j) % 9 + 1 for j in range(cols - 1)] for i in range(rows)]
    # V: (rows-1) x cols
    V = [[((i + 1) * cols + j + 3) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    if k & 1:
        # print('\n'.join(' '.join(['-1'] * cols) for _ in range(rows)))
        pass
        return

    d = [0] * (rows * cols)
    for _ in range(k // 2):
        nd = [0] * (rows * cols)
        for x in range(rows):
            for y in range(cols):
                v = x * cols + y
                w = []
                if x:
                    w.append(d[v - cols] + V[x - 1][y])
                if y:
                    w.append(d[v - 1] + H[x][y - 1])
                if x < rows - 1:
                    w.append(d[v + cols] + V[x][y])
                if y < cols - 1:
                    w.append(d[v + 1] + H[x][y])
                nd[v] = min(w)
        d = nd

    # print('\n'.join(' '.join(str(2 * x) for x in d[i * cols:i * cols + cols]) for i in range(rows)))
    pass
if __name__ == "__main__":
    main(5)