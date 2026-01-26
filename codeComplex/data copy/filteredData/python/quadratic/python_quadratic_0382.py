def main(n):
    # 将 n 映射为矩阵大小 n x n
    m = n
    r = 0
    c = 0
    f = 1

    # 构造一个全为 '.' 的 n 行字符串列表
    grid = ["." * m for _ in range(n)]

    # 在中间一行构造一段连续的 'B'
    if n > 0 and m > 0:
        row = n // 2
        # 保证至少有一个 'B'
        length = max(1, m // 2)
        # 从中间向左对齐的确定性起点
        start = max(0, (m - length) // 2)
        row_chars = list(grid[row])
        for j in range(start, start + length):
            row_chars[j] = 'B'
        grid[row] = "".join(row_chars)

    for i in range(n):
        s = grid[i]
        if f and "B" in s:
            f = 0
            ci = s.index('B')
            cc = s.count("B")
            r = i + 1 + cc // 2
            c = ci + cc // 2 + 1

    # print(r, c)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行实验
    main(10)