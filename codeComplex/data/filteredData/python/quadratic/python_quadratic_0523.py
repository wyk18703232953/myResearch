def main(n):
    # Define matrix size based on n
    # For time complexity scaling, use n x n grid
    rows = n
    cols = n

    # Deterministic generation of mat: pattern based on indices
    # We'll create a checker-like pattern of '#' and '.' so both True/False paths are hit
    # mat[i][j] is '#' iff (i + j) % 2 == 0
    mat = [[((i + j) % 2 == 0) for j in range(cols)] for i in range(rows)]
    v = [[False] * cols for _ in range(rows)]

    def check(mmat, vv, x, y):
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if (di, dj) == (0, 0):
                    continue
                if not mmat[x + di][y + dj]:
                    return
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if (di, dj) != (0, 0):
                    vv[x + di][y + dj] = True

    if rows >= 3 and cols >= 3:
        for x in range(1, rows - 1):
            for y in range(1, cols - 1):
                check(mat, v, x, y)

    flag = True
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] and (not v[i][j]):
                flag = False

    if flag:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(10)