#!/usr/bin/env python

def generate_matrix(n, m):
    mat = []
    for i in range(n):
        row = []
        for j in range(m):
            # Simple deterministic pattern: True on a checkerboard pattern
            row.append(((i + j) % 2) == 0)
        mat.append(row)
    return mat

def check(m, v, x, y):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) == (0, 0):
                continue
            if not m[x + i][y + j]:
                return

    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) != (0, 0):
                v[x + i][y + j] = True

def core_algorithm(mat):
    n = len(mat)
    if n == 0:
        return True
    m = len(mat[0])
    v = [[False] * m for _ in range(n)]

    if n >= 3 and m >= 3:
        for x in range(1, n - 1):
            for y in range(1, m - 1):
                check(mat, v, x, y)

    flag = True
    for i in range(n):
        for j in range(m):
            if mat[i][j] and (not v[i][j]):
                flag = False
    return flag

def main(n):
    # Interpret n as matrix size: n x n
    if n <= 0:
        # print("YES")
        pass
        return
    mat = generate_matrix(n, n)
    result = core_algorithm(mat)
    if result:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)