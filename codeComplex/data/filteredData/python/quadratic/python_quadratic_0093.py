#!/usr/bin/python3

import copy


def rotate90(n, f):
    return [[f[n - j - 1][i] for j in range(n)] for i in range(n)]

def fliphor(n, f):
    return [[f[i][n - j - 1] for j in range(n)] for i in range(n)]

def flipver(n, f):
    return [[f[n - i - 1][j] for j in range(n)] for i in range(n)]

def eq(n, f, g):
    for i in range(n):
        for j in range(n):
            if f[i][j] != g[i][j]:
                return False
    return True

def generate_matrices(n):
    if n <= 0:
        return 0, [], []
    size = n
    f = []
    g = []
    for i in range(size):
        row_f = []
        row_g = []
        for j in range(size):
            val_f = (i + j) % 2
            val_g = (i * 2 + j * 3) % 2
            row_f.append('#' if val_f == 0 else '.')
            row_g.append('#' if val_g == 0 else '.')
        f.append(row_f)
        g.append(row_g)
    return size, f, g

def core_logic(n, f, g):
    for doflipv in range(2):
        for dofliph in range(2):
            for nrot in range(4):
                h = copy.deepcopy(f)
                if dofliph == 1:
                    h = fliphor(n, h)
                if doflipv == 1:
                    h = flipver(n, h)
                for _ in range(nrot):
                    h = rotate90(n, h)
                if eq(n, h, g):
                    print("Yes")
                    return
    print("No")

def main(n):
    n_internal, f, g = generate_matrices(n)
    if n_internal == 0:
        print("No")
        return
    core_logic(n_internal, f, g)

if __name__ == "__main__":
    main(5)