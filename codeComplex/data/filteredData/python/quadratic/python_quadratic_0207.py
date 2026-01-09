def main(n):
    # Map n to matrix dimensions
    if n <= 0:
        return
    # Define number of columns as n (square matrix)
    m = n

    # Deterministic generation of n x m binary matrix
    # Use simple arithmetic pattern based on i, j
    x = []
    for i in range(n):
        row = []
        for j in range(m):
            # Deterministic 0/1 pattern
            val = ((i + 1) * (j + 3)) % 2
            row.append(val)
        x.append(row)

    res = [0] * m
    for i in range(n):
        for j in range(m):
            res[j] += x[i][j]

    for i in range(n):
        ok = 1
        for j in range(m):
            if res[j] == 1 and x[i][j] == 1:
                ok = 0
                break
        if ok:
            # print("YES")
            pass
            return
    # print("NO")
    pass
if __name__ == "__main__":
    # Example call for scalability experiments
    main(5)