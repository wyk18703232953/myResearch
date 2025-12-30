import random

def main(n):
    # n: grid size (n x n). This version generates an n×n grid as test data.
    # You can adjust data generation rules as needed.

    m = n  # keep a square grid

    # 随机生成由 '.' 和 '#' 组成的 n×n 网格，保证至少一行有 '.'，以触发 start 逻辑
    a = []
    has_dot_row = False
    for i in range(n):
        row = [random.choice(['.', '#']) for _ in range(m)]
        if '.' in row:
            has_dot_row = True
        a.append(row)

    # 如果没有任何含 '.' 的行，则强制第一行有一个 '.'
    if not has_dot_row and n > 0 and m > 0:
        a[0][0] = '.'

    # b 初始为全 '.'
    b = [list('.' * m) for _ in range(n)]

    start = 0
    for i in range(n):
        if start == 0 and '.' in a[i]:
            start = ((i - 3) // 3) * 3

    # 将前 start 行全部设为 '#'
    for i in range(max(0, start)):
        if 0 <= i < n:
            b[i] = list('#' * m)

    # 核心逻辑保持不变
    for i in range(start, n - 2):
        for j in range(m - 2):
            ok = True
            if a[i][j] == '#':
                for y in range(i, i + 3):
                    if not ok:
                        break
                    for x in range(j, j + 3):
                        if not (y == i + 1 and x == j + 1):
                            if a[y][x] != '#':
                                ok = False
                                break
                if ok:
                    for y in range(i, i + 3):
                        for x in range(j, j + 3):
                            if not (y == i + 1 and x == j + 1):
                                b[y][x] = '#'

    if a == b:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)