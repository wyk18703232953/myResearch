#!/usr/bin/env python3

def main(n):
    # 定义矩阵规模：n 映射到 n x n
    if n <= 0:
        print("YES")
        return
    global cells, paper, n_rows, n_cols

    n_rows = n
    n_cols = n

    # 确定性生成 cells：简单的周期性图案，依赖行列下标
    # 规则：如果 (i + j) % 3 == 0 则为 '#'，否则为 '.'
    cells = []
    for i in range(n_rows):
        row_chars = []
        for j in range(n_cols):
            if (i + j) % 3 == 0:
                row_chars.append('#')
            else:
                row_chars.append('.')
        cells.append(''.join(row_chars))

    paper = [["." for _ in range(n_cols)] for _ in range(n_rows)]

    for r in range(n_rows):
        for c in range(n_cols):
            if writable(r, c):
                fill_ink(r, c)

    for r in range(n_rows):
        for c in range(n_cols):
            if cells[r][c] != paper[r][c]:
                print("NO")
                return

    print("YES")


def writable(r, c):
    if r + 2 >= n_rows or c + 2 >= n_cols:
        return False
    t = set()
    t.add(cells[r][c])
    t.add(cells[r][c + 1])
    t.add(cells[r][c + 2])
    t.add(cells[r + 1][c])
    t.add(cells[r + 1][c + 2])
    t.add(cells[r + 2][c])
    t.add(cells[r + 2][c + 1])
    t.add(cells[r + 2][c + 2])
    return '.' not in t


def fill_ink(r, c):
    paper[r][c] = "#"
    paper[r][c + 1] = "#"
    paper[r][c + 2] = "#"
    paper[r + 1][c] = "#"
    paper[r + 1][c + 2] = "#"
    paper[r + 2][c] = "#"
    paper[r + 2][c + 1] = "#"
    paper[r + 2][c + 2] = "#"


if __name__ == "__main__":
    main(10)