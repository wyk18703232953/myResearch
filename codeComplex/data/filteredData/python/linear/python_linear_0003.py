def decimal_to_26(num):
    num = int(num)
    res = ''
    while num:
        mod = num % 26
        if mod == 0:
            res = 'Z' + res
            num = num // 26 - 1
        else:
            num //= 26
            res = chr(mod + 64) + res
    return res


def RXCY_to_Excel(r, c):
    new_row = decimal_to_26(r)
    return new_row + str(c)


def main(n):
    # 生成测试数据：
    # 一半为 "RxxCyy" 格式，一半为 "COLROW" 格式
    tests = []
    for i in range(n):
        if i % 2 == 0:
            # 生成 RXCY 格式
            r = (i + 1) * 3
            c = (i + 2) * 5
            tests.append(f"R{r}C{c}")
        else:
            # 生成 COLROW 格式
            col_num = i + 10

            # 把数字转成 Excel 列名（反向的过程）
            def num_to_col(x):
                s = ''
                while x:
                    x, rem = divmod(x - 1, 26)
                    s = chr(ord('A') + rem) + s
                return s

            col = num_to_col(col_num)
            row = (i + 1) * 7
            tests.append(f"{col}{row}")

    # 处理并输出结果
    for s in tests:
        di_index = []
        al_index = []
        temp = s
        t = s
        for j in range(len(t)):
            if t[j].isalpha():
                al_index.append(j)
                t = t.replace(t[j], ' ')
            elif t[j].isdigit():
                di_index.append(j)
                t = t.replace(t[j], ' ')
        s = temp

        if min(di_index) < max(al_index):  # RxxCyy 格式
            row = int(s[1:s.index('C')])
            col = int(s[s.index('C') + 1:])
            print(RXCY_to_Excel(row, col))
        else:  # COL + ROW 格式
            for k in range(len(s)):
                if s[k].isdigit():
                    num_start = k
                    break
            length = len(s[0:k])
            row_num = 0
            for m in range(num_start):
                row_num += 26 ** (length - 1) * (ord(s[m]) - 64) or (ord(s[m]) - 64)
                length -= 1
            print('R' + s[num_start:] + 'C' + str(row_num))


if __name__ == "__main__":
    # 示例：n = 5
    main(5)