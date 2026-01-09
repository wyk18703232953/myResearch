def parse(line: str):
    i = 0
    while i < len(line) and line[i].isalpha():
        i += 1
    i1 = i
    while i < len(line) and line[i].isdigit():
        i += 1
    return line[:i1], int(line[i1:i]), line[i:]


def convert_cell_notation(line: str) -> str:
    a1, n1, rest = parse(line)
    if rest:
        # RC -> Excel style
        _, n2, _ = parse(rest)
        a2 = ''
        while n2:
            r = (n2 - 1) % 26
            a2 = chr(r + ord('A')) + a2
            n2 = (n2 - r - 1) // 26
        return a2 + str(n1)

    else:
        # Excel style -> RC
        n2 = 0
        for c in a1:
            n2 = 26 * n2 + (ord(c) - ord('A') + 1)
        return f'R{n1}C{n2}'


def main(n: int):
    """
    n: number of test cases to generate and convert
    生成 n 条测试数据并进行转换，打印输出。
    测试数据规则：
    - 前 n//2 条为 RC 格式：R{row}C{col}
    - 后 n - n//2 条为 Excel 格式：列字母 + 行数字
    行号、列号、列字母按简单规则生成，覆盖不同规模。
    """
    # 生成前一半为 RC 格式
    for i in range(1, n // 2 + 1):
        row = i * 10
        col = i * 7
        line = f"R{row}C{col}"
        # print(convert_cell_notation(line))
        pass

    # 生成后一半为 Excel 格式
    def num_to_col(x: int) -> str:
        s = ''
        while x:
            r = (x - 1) % 26
            s = chr(r + ord('A')) + s
            x = (x - r - 1) // 26
        return s

    for i in range(n // 2 + 1, n + 1):
        row = i * 5
        col = i  # 用 i 生成列号，然后转为列字母
        col_letters = num_to_col(col)
        line = f"{col_letters}{row}"
        # print(convert_cell_notation(line))
        pass
if __name__ == "__main__":
    # 示例：可在此处手动设置规模 n
    main(5)