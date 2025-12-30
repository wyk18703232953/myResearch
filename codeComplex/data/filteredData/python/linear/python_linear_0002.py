from math import floor
import re
import random

z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_num(x: str) -> str:
    output = ""
    row, col = [int(x) for x in re.split(r"(\d+)", x) if x.isnumeric()]
    while col > 0:
        y = (col - 1) % 26
        output += z[y]
        col = floor((col - 1) / 26)
    return f"{output[::-1]}{row}"


def convert_alpha(x: str) -> str:
    output = 0
    word = ("".join([i for i in x if i.isalpha()]))[::-1]
    for i in range(len(word)):
        output += (z.index(word[i]) + 1) * 26 ** i
    ending = x[len(word):]
    return f"R{ending}C{output}"


def random_rc_style() -> str:
    # R<row>C<col>, row, col in [1, 26*26]
    row = random.randint(1, 26 * 26)
    col = random.randint(1, 26 * 26)
    return f"R{row}C{col}"


def random_excel_style() -> str:
    # <letters><row>
    col = random.randint(1, 26 * 26)
    # convert col number to letters (same as convert_num but without row)
    output = ""
    c = col
    while c > 0:
        y = (c - 1) % 26
        output += z[y]
        c = (c - 1) // 26
    letters = output[::-1]
    row = random.randint(1, 26 * 26)
    return f"{letters}{row}"


def main(n: int):
    tests = []
    for _ in range(n):
        if random.random() < 0.5:
            tests.append(random_rc_style())
        else:
            tests.append(random_excel_style())

    output = []
    for hehexd in tests:
        if hehexd.startswith("R") and len(hehexd) > 1 and hehexd[1].isnumeric() and "C" in hehexd:
            output.append(convert_num(hehexd))
        else:
            output.append(convert_alpha(hehexd))

    print("\n".join(output))


if __name__ == "__main__":
    # 示例：生成并处理 10 条测试数据
    main(10)