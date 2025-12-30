import re
import random
import string


def excel_col_to_num(col: str) -> int:
    num = 0
    for ch in col:
        num = num * 26 + (ord(ch) - 64)
    return num


def num_to_excel_col(num: int) -> str:
    # 1-based
    res = []
    while num > 0:
        num, r = divmod(num - 1, 26)
        res.append(chr(65 + r))
    return "".join(reversed(res))


def main(n: int):
    """
    n: 测试数据规模，即生成的坐标数量
    """

    random.seed(0)

    for _ in range(n):
        # 随机决定生成哪种格式: True -> RnCm, False -> Excel格式
        use_rc_format = random.choice([True, False])

        # 生成行号和列号，控制在一定范围内
        row = random.randint(1, 10**6)
        col = random.randint(1, 10**6)

        if use_rc_format:
            coordinates = f"R{row}C{col}"
        else:
            letters = num_to_excel_col(col)
            coordinates = f"{letters}{row}"

        match = re.match(r"R(\d+)C(\d+)", coordinates)
        if match:
            rows = int(match.group(1))
            columns = int(match.group(2))

            output = ""
            i = 0
            while columns > 0:
                alpha_index = (columns // (26 ** i) - 1) % 26
                output = chr(65 + alpha_index) + output
                columns -= (alpha_index + 1) * (26 ** i)
                i += 1
            output += str(rows)
            print(output)
        else:
            match = re.match(r"(\D+)(\d+)", coordinates)
            letters = match.group(1)
            rows = match.group(2)
            columns = 0
            for i in range(len(letters), 0, -1):
                columns += (ord(letters[i - 1]) - 64) * (26 ** (len(letters) - i))
            output = f"R{rows}C{columns}"
            print(output)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)