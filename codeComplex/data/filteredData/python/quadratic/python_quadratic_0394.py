def main(n):
    # 根据题意构造一个宽度 m 的棋盘，含连续的 'B'
    # 这里假设 m 与 n 相同，构造一个简单可控的测试数据：
    # 在第 n//2 行放一段连续的 'B'
    m = n

    listi = []
    target_row = n // 2
    segment_len = max(1, n // 3)  # 连续 'B' 段长度
    start_col = max(0, (m - segment_len) // 2)

    for i in range(n):
        if i == target_row:
            row = ['W'] * m
            for j in range(start_col, start_col + segment_len):
                row[j] = 'B'
            listi.append(''.join(row))
        else:
            listi.append('W' * m)

    # 以下是原逻辑（去掉 input），在生成的 listi 上运行
    rownum = 0
    flag = False

    for row in listi:
        for letter in row:
            if "B" in row:
                p = row.index("B")

                s = row[::-1]
                q = abs(m - s.index("B") - 1)

                if p == q:
                    print(rownum + 1, row.index(row[p]) + 1)
                    flag = True
                    break

                mr = (q + p) / 2
                length = abs(q - p + 1)
                rn = rownum + length // 2

                print(rn + 1, int(mr + 1))
                flag = True
                break

        if flag:
            break

        rownum += 1


# 示例：自行调用 main(5) 等进行测试
# main(5)