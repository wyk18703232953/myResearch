import math

def main(n):
    # 映射：原程序中 a 为行数，b 为列数，这里都设为 n
    a = n
    b = n

    # 生成一个 a 行 b 列的矩阵，每行是字符串，由 '.' 和 'B' 组成
    # 为了保持可扩展性和确定性，我们在主对角线上放置 'B'
    grid = []
    for i in range(a):
        row = []
        for j in range(b):
            if i == j:
                row.append('B')

            else:
                row.append('.')
        grid.append(''.join(row))

    c = []
    e = []
    for i in range(a):
        d = grid[i]
        for j in range(b):
            if d[j] == "B":
                c = c + [i]
                e = e + [j]

    if not c:
        # 如果没有 'B'，原程序会在 min/max 时出错，这里约定返回 (0, 0)
        # print(0, 0)
        pass
        return

    p = min(c)
    p1 = min(e)
    p2 = max(c)
    plus = (max(c) - min(c)) // 2
    p3 = p + plus + 1
    p4 = p1 + plus + 1
    # print(p3, p4)
    pass
if __name__ == "__main__":
    main(5)