def main(n):
    # 根据 n 构造一个 n 行 m 列（这里设 m = n）的测试棋盘
    m = n
    s = [""] * n

    # 示例测试数据：第 0 行中间放一段连续的 'B'，其余为 '.'
    # 你可以根据需要修改测试数据生成逻辑
    for i in range(n):
        if i == 0:
            row = ['.'] * m
            # 放一段长度为 len_B 的连续 'B'
            len_B = max(1, m // 3)
            start = (m - len_B) // 2
            for j in range(start, start + len_B):
                row[j] = 'B'
            s[i] = "".join(row)
        else:
            s[i] = "." * m

    # 原始逻辑
    for i in range(n):
        for j in range(m):
            if s[i][j] == 'B':
                cnt = 1
                for k in range(j + 1, m):
                    if s[i][k] == 'B':
                        cnt += 1
                    else:
                        break
                print(i + 1 + cnt // 2, j + 1 + cnt // 2)
                return  # 代替 exit(0)


if __name__ == "__main__":
    # 示例调用：n 可按需调整
    main(5)