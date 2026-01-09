def main(n):
    # Interpret n as both number of rows and columns for scalability
    rows = n
    cols = n

    # Deterministic generation of a: rows x cols matrix of 0/1
    # Example pattern: a[i][j] = (i + j) % 2
    a = [[(i + j) % 2 for j in range(cols)] for i in range(rows)]

    ignorable = [True] * rows

    for i in range(cols):
        cnt = 0
        for j in range(rows):
            cnt += a[j][i]
        if cnt == 1:
            for j in range(rows):
                if a[j][i]:
                    ignorable[j] = False

    if any(ignorable):
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)