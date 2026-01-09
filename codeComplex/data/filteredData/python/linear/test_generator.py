import re

def col_to_rc(col_str, row_num):
    columns = 0
    for i in range(len(col_str), 0, -1):
        columns += (ord(col_str[i - 1]) - 64) * (26 ** (len(col_str) - i))
    return f"R{row_num}C{columns}"

def rc_to_col(columns, rows):
    output = ""
    i = 0
    while columns > 0:
        alpha_index = (columns // (26 ** i) - 1) % 26
        output = chr(65 + alpha_index) + output
        columns -= (alpha_index + 1) * (26 ** i)
        i += 1
    return f"{output}{rows}"

def generate_single_col_letter(index, max_len=3):
    length = index % max_len + 1
    letters = ''.join(chr(65 + (index + k) % 26) for k in range(length))
    return letters

def generate_test_cases(n):
    test_cases = []

    # 单字母列: 大约 20% 的 n
    single_cnt = n // 5
    for i in range(single_cnt):
        letter = chr(65 + (i % 26))
        row = i + 1
        test_cases.append(letter + str(row))

    # 双字母列: 大约 20% 的 n
    two_cnt = n // 5
    for i in range(two_cnt):
        letters = ''.join(chr(65 + ((i + k) % 26)) for k in range(2))
        row = (i + 1) * 2
        test_cases.append(letters + str(row))

    # 三字母列: 大约 20% 的 n
    three_cnt = n // 5
    for i in range(three_cnt):
        letters = ''.join(chr(65 + ((i + k) % 26)) for k in range(3))
        row = (i + 1) * 3
        test_cases.append(letters + str(row))

    # 部分 R 行 C 列格式: 大约 20% 的 n
    rc_cnt = n // 5
    for i in range(rc_cnt):
        row = i + 1
        col = (i + 1) * 10
        test_cases.append(f"R{row}C{col}")

    # 如果数量不足 n，填充混合模式
    while len(test_cases) < n:
        i = len(test_cases)
        if i % 2 == 0:
            col = generate_single_col_letter(i, 3)
            row = (i + 1) * 7
            test_cases.append(col + str(row))

        else:
            row = (i + 1) * 3
            col = (i + 1) * 5
            test_cases.append(f"R{row}C{col}")

    # 截断到刚好 n 个
    return test_cases[:n]

def generate_expected_outputs(test_cases):
    expected = []
    for coord in test_cases:
        match_rc = re.match(r"R(\d+)C(\d+)", coord)
        match_alpha = re.match(r"(\D+)(\d+)", coord)

        if match_rc:
            rows = int(match_rc.group(1))
            columns = int(match_rc.group(2))
            output = rc_to_col(columns, rows)

        else:
            letters = match_alpha.group(1)
            rows = match_alpha.group(2)
            columns = 0
            for i in range(len(letters), 0, -1):
                columns += (ord(letters[i - 1]) - 64) * (26 ** (len(letters) - i))
            output = f"R{rows}C{columns}"
        expected.append(output)
    return expected

def main(n):
    test_cases = generate_test_cases(n)
    expected = generate_expected_outputs(test_cases)
    for out in expected:
        # print(out)
        pass
if __name__ == "__main__":
    main(1000)