def main(n):
    # 将 n 解释为矩阵的行数和列数
    rows = n
    cols = n
    matrix = []

    # 构造一个确定性的矩阵：第 i 行在 (i, i) 和 (i, i+1) 放置两个 'B'（若合法），其余为 '.'
    # 这样第一行总是包含至少两个 'B'，与原逻辑兼容
    for i in range(rows):
        row = ['.'] * cols
        if i < cols:
            row[i] = 'B'
        if i + 1 < cols:
            row[i + 1] = 'B'
        matrix.append(''.join(row))

    # 原始逻辑：找到第一行包含 'B' 的行，并根据计数和位置输出
    for i in range(rows):
        mt = matrix[i]
        if mt.count('B') != 0:
            # print(mt.count('B') // 2 + i + 1, mt.count('B') // 2 + mt.index('B') + 1)
            pass
            break


if __name__ == "__main__":
    main(5)