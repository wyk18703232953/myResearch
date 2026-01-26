def main(n):
    # Interpret n as both the number of rows and the number of columns
    rows = n
    cols = n

    # Deterministically generate t test cases; here we use t = 1 for simplicity
    t = 1

    results = []

    for _ in range(t):
        # Generate an n x n matrix deterministically using a simple arithmetic pattern
        # mat[i][j] = (i * n + j) % (n + 7) + 1
        mat = []
        for i in range(rows):
            row = [((i * cols + j) % (n + 7)) + 1 for j in range(cols)]
            mat.append(row)

        # Build columns
        col = [[] for _ in range(cols)]
        for j in range(rows):
            line = mat[j]
            for k, item in enumerate(line):
                col[k].append(item)

        colmax = []
        for line in col:
            colmax.append([max(line), line])
        colmax.sort(reverse=True)
        colmax = colmax[:rows]
        ans = 0

        # Core algorithm, kept identical except using rows instead of n where appropriate
        # (rows == cols == original n)
        for j in range(rows ** (rows - 1)):
            index = j
            rot = [0]
            for k in range(rows - 1):
                rot.append(index % rows)
                index //= rows
            ret = 0
            for l in range(rows):
                val = 0
                for k in range(len(colmax)):
                    val = max(val, colmax[k][1][(l + rot[k]) % rows])
                ret += val
            ans = max(ans, ret)

        results.append(ans)

    # For scalability experiments you may want the function to return results instead of printing
    for res in results:
        print(res)


if __name__ == "__main__":
    # Example deterministic call; adjust n for complexity experiments
    main(3)