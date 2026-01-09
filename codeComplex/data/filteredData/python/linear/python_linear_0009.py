def main(n):
    v = []

    # 生成 n 个测试字符串，前半为 "RxxCyy" 格式，后半为 "COLROW" 格式
    # 保证覆盖两种分支逻辑并且完全确定
    test_strings = []
    half = n // 2

    # 前半：R{row}C{col}
    # 行号和列号与 i 做简单算术映射，保证规模随 n 增长
    for i in range(1, half + 1):
        row = i
        col = i * 37 + 5  # 任意确定性线性映射
        test_strings.append(f"R{row}C{col}")

    # 后半：列名+行号，如 "AB123"
    # 列名根据 i 转换成 1~702 之间的列名模式
    def col_name_from_num(x):
        # 与原逻辑一致：1 -> A, 26 -> Z, 27 -> AA
        v_local = []
        while x > 0:
            if x % 26 == 0:
                v_local.append('Z')
                x = (x - 1) // 26

            else:
                v_local.append(chr(ord('A') + (x % 26 - 1)))
                x //= 26
        v_local.reverse()
        return "".join(v_local)

    for i in range(half + 1, n + 1):
        col_num = i
        col_str = col_name_from_num(col_num)
        row = i * 13 + 7
        test_strings.append(f"{col_str}{row}")

    for s in test_strings:
        p = s.find('C')

        if len(s) >= 2 and s[0] == 'R' and s[1].isdigit() and p > 1:
            r = int(s[1:p])
            c = int(s[(p + 1):])

            v.clear()
            while c > 0:
                if c % 26 == 0:
                    v.append('Z')
                    c = (c - 1) // 26

                else:
                    v.append(chr(ord('A') + (c % 26 - 1)))
                    c //= 26

            v.reverse()
            # print("%s%d" % ("".join(v), r))
            pass

        else:
            c = 0
            p = 0
            while p < len(s):
                if s[p].isdigit():
                    break
                c = c * 26 + (ord(s[p]) - ord('A') + 1)
                p += 1

            # print("R%sC%d" % (s[p:], c))
            pass
if __name__ == "__main__":
    main(10)