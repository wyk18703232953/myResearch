def main(n):
    # Interpret n as both number of rows and columns for scalability.
    # Also set k (number of deletions allowed) proportional to n, but bounded.
    rows = n
    cols = n
    # Let k be up to min(n, total columns), but at least 0
    k = n // 2
    if k > cols:
        k = cols

    # Deterministic generation of the matrix 'a' of '0'/'1' strings
    # Pattern: cell (i,j) is '1' if (i + j) is divisible by 3, else '0'
    a = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i + j) % 3 == 0:
                row_chars.append('1')

            else:
                row_chars.append('0')
        a.append(''.join(row_chars))

    # Core algorithm logic preserved
    mem = [[float('inf') if i else 0 for _ in range(k + 1)] for i in range(rows + 1)]

    for i in range(rows):
        ixs = []
        for j in range(cols):
            if a[i][j] == '1':
                ixs.append(j)

        for j in range(k + 1):
            tem = 0
            if j < len(ixs):
                tem, c = float('inf'), 0
                for j1 in range(len(ixs) - j - 1, len(ixs)):
                    tem = min(tem, ixs[j1] - ixs[c] + 1)
                    c += 1

            for j1 in range(k + 1 - j):
                mem[i + 1][j1 + j] = min(mem[i + 1][j1 + j], mem[i][j1] + tem)

    # For timing experiments, we can print or return the result
    # print(mem[rows][k])
    pass
    return mem[rows][k]


if __name__ == "__main__":
    # Example call for complexity experiments
    main(200)