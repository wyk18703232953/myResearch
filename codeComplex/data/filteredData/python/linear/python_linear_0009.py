def main(n):
    v = []

    for i in range(1, n + 1):
        # 交替构造两种输入格式：
        # 奇数 i -> "R{row}C{col}"
        # 偶数 i -> "COL{row}"
        row = i
        col = i * 17 + 3  # 确定性列号
        if i % 2 == 1:
            s = f"R{row}C{col}"
        else:
            # 生成一个确定性的列名前缀，再接行号
            # 这里用简单的 1..k 进制 26 编码生成列名
            c = col
            v.clear()
            while c > 0:
                if c % 26 == 0:
                    v.append('Z')
                    c = (c - 1) // 26
                else:
                    v.append(chr(ord('A') + (c % 26 - 1)))
                    c //= 26
            v.reverse()
            col_name = "".join(v)
            s = f"{col_name}{row}"

        p = s.find('C')

        # R23C55 -> BC23
        if s[0] == 'R' and s[1].isdigit() and p > 1:
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
            print("%s%d" % ("".join(v), r))

        else:
            c = 0
            p = 0
            while p < len(s):
                if s[p].isdigit():
                    break
                c = c * 26 + (ord(s[p]) - ord('A') + 1)
                p += 1

            print("R%sC%d" % (s[p:], c))


if __name__ == "__main__":
    # 示例：使用 n=10 作为规模进行一次运行
    main(10)