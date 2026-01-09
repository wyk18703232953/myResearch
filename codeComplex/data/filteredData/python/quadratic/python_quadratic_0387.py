def main(n):
    # 这里根据 n 生成一个测试用的棋盘（n 行，n 列），中间一块连续的 'B'
    # 你可以按照需要修改生成逻辑
    m = n
    board = []
    mid_row = n // 2
    # 在中间一行放一段长度为 n//2 的连续 'B'
    b_len = max(1, n // 2)
    start_col = (m - b_len) // 2
    for i in range(n):
        if i == mid_row:
            row = ['W'] * m
            for j in range(start_col, start_col + b_len):
                row[j] = 'B'
            board.append(''.join(row))

        else:
            board.append('W' * m)

    # 以下是对原始逻辑的封装和等价实现
    listi = board
    rownum = 0
    flag = False

    for row in listi:
        for letter in row:
            if "B" in row:
                p = row.index("B")               # 左端第一个 B 的列号（0-based）
                s = row[::-1]
                q = abs(m - s.index("B") - 1)    # 右端第一个 B 的列号（0-based）

                if p == q:  # 只有一个 B
                    # print(rownum + 1, row.index(row[p]) + 1)
                    pass
                    flag = True
                    break

                mr = (q + p) / 2                 # 水平方向中心列（0-based，可能是 .5）

                length = abs(q - p + 1)
                rn = rownum + length // 2        # 垂直方向中心行（0-based）

                # print(rn + 1, int(mr + 1))# 输出 1-based 坐标       
                pass
                flag = True
                break

        if flag:
            break

        rownum += 1


# 示例：调用 main(8) 生成规模为 8 的测试数据并运行逻辑
if __name__ == "__main__":
    main(8)