def parse(line):
    i = 0
    while i < len(line) and line[i].isalpha():
        i += 1
    i1 = i
    while i < len(line) and line[i].isdigit():
        i += 1
    return line[:i1], int(line[i1:i]), line[i:]


def main(n):
    # 生成 n 条确定性测试数据
    # 奇数行使用 "RC" 形式：R{row}C{col}
    # 偶数行使用 "Excel 列+行号" 形式：{colLetters}{row}
    lines = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            row = i
            col = (i * 7) % 1000 + 1  # 保证列号为正且分布有变化
            lines.append(f"R{row}C{col}")

        else:
            row = i
            # 构造确定性的列号并转为列名
            col_num = (i * 13) % 1000 + 1
            tmp = col_num
            col_letters = ""
            while tmp:
                r = (tmp - 1) % 26
                col_letters = chr(r + ord('A')) + col_letters
                tmp = (tmp - r - 1) // 26
            lines.append(col_letters + str(row))

    # 按原算法处理生成的数据
    for line in lines:
        a1, n1, rest = parse(line)
        if rest:
            _, n2, _ = parse(rest)
            a2 = ''
            while n2:
                r = (n2 - 1) % 26
                a2 = chr(r + ord('A')) + a2
                n2 = (n2 - r - 1) // 26
            # print(a2 + str(n1))
            pass

        else:
            n2 = 0
            for c in a1:
                n2 = 26 * n2 + (ord(c) - ord('A') + 1)
            # print(f'R{n1}C{n2}')
            pass
if __name__ == "__main__":
    main(10)