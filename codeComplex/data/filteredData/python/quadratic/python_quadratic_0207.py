def main(n):
    # Interpret n as both number of rows and columns
    m = n

    # Deterministically generate an n x m 0/1 matrix
    # Pattern: x[i][j] = 1 if (i + j) % 2 == 0 else 0
    x = [[1 if (i + j) % 2 == 0 else 0 for j in range(m)] for i in range(n)]

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
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)