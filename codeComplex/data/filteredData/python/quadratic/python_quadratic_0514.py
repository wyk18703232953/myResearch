def main(n):
    # Map n to grid size: use an n x n grid
    rows = n
    cols = n

    # Deterministic generation of s: pattern of '#' and '.'
    # Example: cell is '#' if (i + j) % 3 != 0, else '.'
    s = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i + j) % 3 != 0:
                row_chars.append('#')

            else:
                row_chars.append('.')
        s.append(''.join(row_chars))

    mapp = [[False] * cols for _ in range(rows)]

    rnd = (
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    )

    def gene(x, y, p):
        cx = x - rnd[p][0]
        cy = y - rnd[p][1]
        ans = []
        for i in range(8):
            ans.append((cx + rnd[i][0], cy + rnd[i][1]))
        return ans

    def judge(ps):
        for x, y in ps:
            if 0 <= x < rows and 0 <= y < cols and s[x][y] == '#':
                continue

            else:
                return False
        return True

    def dye(ps):
        for x, y in ps:
            mapp[x][y] = True

    def check(x, y):
        for i in range(8):
            r = gene(x, y, i)
            if judge(r):
                dye(r)
                return True
        return False

    for i in range(rows):
        for j in range(cols):
            if s[i][j] == '#' and mapp[i][j] is False:
                if check(i, j):
                    continue

                else:
                    # print('NO')
                    pass
                    return
    # print('YES')
    pass
if __name__ == "__main__":
    main(10)