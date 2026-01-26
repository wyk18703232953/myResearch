def main(n):
    # Interpret n as grid size n x n; k proportional to n for scalability
    rows = n
    cols = n
    k = 2 * n  # even to exercise main DP branch

    # Deterministic generation of rlist and clist based on indices
    # rlist: rows x cols
    rlist = [[(i + j) % 7 + 1 for j in range(cols)] for i in range(rows)]
    # clist: (rows-1) x cols
    if rows > 1:
        clist = [[(i * 3 + j * 2) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    else:
        clist = []

    dway = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if k % 2:
        res = [[-1] * cols for _ in range(rows)]

    else:
        flist = [[0] * cols for _ in range(rows)]
        for _ in range(k // 2):
            glist = [[10 ** 9] * cols for _ in range(rows)]
            for dx, dy in dway:
                klist = rlist if dx == 0 else clist
                for x in range(rows):
                    for y in range(cols):
                        xx, yy = x + dx, y + dy
                        if not (0 <= xx < rows) or not (0 <= yy < cols):
                            continue
                        tx = xx if dx == -1 else x
                        ty = yy if dy == -1 else y
                        glist[x][y] = min(glist[x][y], flist[xx][yy] + klist[tx][ty] * 2)
            flist = glist
        res = flist

    for row in res:
        # print(' '.join(map(str, row)))
        pass
if __name__ == "__main__":
    main(5)