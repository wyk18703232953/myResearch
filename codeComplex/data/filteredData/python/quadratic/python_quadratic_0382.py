def main(n):
    # 映射关系：
    # 原程序有两个输入：n(行数)、m(列数)
    # 在重构中：n 表示行列的规模，同时用于生成矩阵行列数量
    # 行数 = n，列数 = n
    rows = n
    cols = n

    r = 0
    c = 0
    f = 1

    # 生成确定性的字符串矩阵
    # 规则：在第 rows//2 行放连续的一段 'B'，其余行全为 '.'
    # B 段长度 = max(1, cols//3)，起始位置 = max(0, (cols - length)//2)
    target_row = rows // 2 if rows > 0 else 0
    length = max(1, cols // 3) if cols > 0 else 0
    start = max(0, (cols - length) // 2) if cols > 0 else 0

    for i in range(rows):
        if i == target_row and cols > 0:
            s_list = ['.'] * cols
            for j in range(start, min(start + length, cols)):
                s_list[j] = 'B'
            s = ''.join(s_list)

        else:
            s = '.' * cols

        if f and "B" in s:
            f = 0
            ci = s.index('B')
            cc = s.count("B")
            r = i + 1 + cc // 2
            c = ci + cc // 2 + 1

    # print(r, c)
    pass
if __name__ == "__main__":
    main(10)