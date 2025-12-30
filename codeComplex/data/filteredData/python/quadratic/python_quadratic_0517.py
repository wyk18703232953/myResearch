#!/usr/bin/env python3
import random

def main(n):
    # 1. 随机生成规模：n 行，m 列
    # 这里令 m 与 n 相同，也可按需修改为其他规则
    m = n

    # 2. 随机生成原始图案 cells：字符为 '#' 或 '.'
    # 为了更有结构性，这里稍微偏向 '.'，减少随机“噪声”
    cells = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append('#' if random.random() < 0.4 else '.')
        cells.append(''.join(row))

    # 3. 按原程序逻辑构造 paper，并比较 cells 与 paper
    paper = [["." for _ in range(m)] for _ in range(n)]

    def writable(r, c):
        if r + 2 >= n or c + 2 >= m:
            return False
        t = set()
        t.add(cells[r][c])
        t.add(cells[r][c+1])
        t.add(cells[r][c+2])
        t.add(cells[r+1][c])
        t.add(cells[r+1][c+2])
        t.add(cells[r+2][c])
        t.add(cells[r+2][c+1])
        t.add(cells[r+2][c+2])
        return '.' not in t

    def fill_ink(r, c):
        paper[r][c] = "#"
        paper[r][c+1] = "#"
        paper[r][c+2] = "#"
        paper[r+1][c] = "#"
        paper[r+1][c+2] = "#"
        paper[r+2][c] = "#"
        paper[r+2][c+1] = "#"
        paper[r+2][c+2] = "#"

    for r in range(n):
        for c in range(m):
            if writable(r, c):
                fill_ink(r, c)

    for r in range(n):
        for c in range(m):
            if cells[r][c] != paper[r][c]:
                print("NO")
                return

    print("YES")


if __name__ == "__main__":
    # 示例：调用 main(5) 做一次测试
    main(5)