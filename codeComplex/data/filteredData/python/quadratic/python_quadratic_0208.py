def main(n):
    # Interpret n as both number of rows and columns
    if n <= 0:
        return
    rows = n
    cols = n

    # Deterministic grid generation:
    # grid[i][j] is '1' if (i + j) % 3 != 0, else '0'
    grid = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i + j) % 3 == 0:
                row_chars.append('0')

            else:
                row_chars.append('1')
        grid.append(''.join(row_chars))

    cnts = [0 for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            cnts[j] += 0 if grid[i][j] == '0' else 1

    for i in range(rows):
        flag = True
        for j in range(cols):
            if grid[i][j] == '1' and cnts[j] == 1:
                flag = False
                break
        if flag:
            # print('YES')
            pass
            return
    # print('NO')
    pass
if __name__ == "__main__":
    main(5)