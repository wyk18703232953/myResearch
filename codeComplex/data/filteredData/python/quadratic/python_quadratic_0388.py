import math
import random

def main(n):
    # n 作为规模，这里生成一个 n x n 的棋盘
    a = n
    b = n

    # 生成测试数据：随机在棋盘上放一些 'B'
    # 确保至少有一个 'B'
    grid = []
    has_B = False
    for i in range(a):
        row = []
        for j in range(b):
            # 概率放置 'B'
            if random.random() < 0.3:
                row.append('B')
                has_B = True
            else:
                row.append('.')
        grid.append(''.join(row))

    if not has_B:
        # 如果随机没有生成 'B'，则强制在中心放一个
        mid = a // 2
        row = list(grid[mid])
        row[b // 2] = 'B'
        grid[mid] = ''.join(row)

    # 原始逻辑开始
    c = []
    e = []
    for i in range(a):
        d = grid[i]
        for j in range(b):
            if d[j] == "B":
                c = c + [i]
                e = e + [j]

    p = min(c)
    p1 = min(e)
    plus = (max(c) - min(c)) // 2
    p3 = p + plus + 1
    p4 = p1 + plus + 1

    print(p3, p4)


if __name__ == "__main__":
    # 可以在这里简单测试，比如 n = 5
    main(5)