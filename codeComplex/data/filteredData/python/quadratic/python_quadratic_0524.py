def main(n):
    # Map n to grid size: n -> n x n grid
    # Ensure minimum size for 3x3 checks
    if n < 3:
        n = 3
    rows = n
    cols = n

    # Deterministic grid generation:
    # Pattern: use (i+j) % 3 to decide '#' or '.'
    cl = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i * 2 + j) % 3 == 0:
                row_chars.append('#')

            else:
                row_chars.append('.')
        cl.append(''.join(row_chars))

    def is_squad(x, y):
        if (
            cl[x][y] == '#' and
            cl[x + 1][y] == '#' and
            cl[x + 2][y] == '#' and
            cl[x + 2][y + 1] == '#' and
            cl[x + 2][y + 2] == '#' and
            cl[x + 1][y + 2] == '#' and
            cl[x][y + 2] == '#' and
            cl[x][y + 1] == '#'
        ):
            return True

        else:
            return False

    def cv(x, y):
        if x - 2 >= 0 and y + 2 <= cols - 1 and is_squad(x - 2, y):
            return True
        elif x - 1 >= 0 and x + 1 <= rows - 1 and y + 2 <= cols - 1 and is_squad(x - 1, y):
            return True
        elif x + 2 <= rows - 1 and y + 2 <= cols - 1 and is_squad(x, y):
            return True
        elif x + 2 <= rows - 1 and y + 1 <= cols - 1 and y - 1 >= 0 and is_squad(x, y - 1):
            return True
        elif x + 2 <= rows - 1 and y - 2 >= 0 and is_squad(x, y - 2):
            return True
        elif x + 1 <= rows - 1 and x - 1 >= 0 and y - 2 >= 0 and is_squad(x - 1, y - 2):
            return True
        elif x - 2 >= 0 and y - 2 >= 0 and is_squad(x - 2, y - 2):
            return True
        elif x - 2 >= 0 and y - 1 >= 0 and y + 1 <= cols - 1 and is_squad(x - 2, y - 1):
            return True

        else:
            return False

    for i in range(rows):
        for j in range(cols):
            if cl[i][j] == '#':
                if not cv(i, j):
                    # print('NO')
                    pass
                    return

    # print('YES')
    pass
if __name__ == "__main__":
    main(10)