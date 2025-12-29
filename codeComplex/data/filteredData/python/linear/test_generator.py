import random
import string
import re
import subprocess


def col_to_rc(col_str, row_num):
    """字母列转数字列，生成R行C列格式"""
    columns = 0
    for i in range(len(col_str), 0, -1):
        columns += (ord(col_str[i - 1]) - 64) * (26 ** (len(col_str) - i))
    return f"R{row_num}C{columns}"


def rc_to_col(columns, rows):
    """数字列转字母列，生成字母+数字格式"""
    output = ""
    i = 0
    while columns > 0:
        alpha_index = (columns // (26 ** i) - 1) % 26
        output = chr(65 + alpha_index) + output
        columns -= (alpha_index + 1) * (26 ** i)
        i += 1
    return f"{output}{rows}"


def generate_single_col_letter(max_len=3):
    """生成单个字母组合"""
    length = random.randint(1, max_len)
    letters = ''.join(random.choices(string.ascii_uppercase, k=length))
    return letters


def generate_test_cases(num_cases=100, output_file='test_cases.txt'):
    """生成测试用例"""
    test_cases = []

    # 比例按原始程序大致固定，这里用 num_cases 缩放数量
    # 原始权重：20 + 20 + 20 + 15 + 25 = 100
    # 再加固定位数 edge + rc：12 + 11 = 23，略超，但主比例仍按 100 分配
    case_types_ratio = {
        'single_letter': 20,
        'two_letters': 20,
        'three_letters': 20,
        'edge_cases': 15,
        'random_mix': 25
    }
    total_ratio = sum(case_types_ratio.values())
    case_types = {}
    remaining = num_cases

    # 按比例向下取整
    for k, v in case_types_ratio.items():
        cnt = num_cases * v // total_ratio
        case_types[k] = cnt
        remaining -= cnt
    # 剩余的放到 random_mix
    case_types['random_mix'] += max(0, remaining)

    # 1. 单字母列
    for _ in range(case_types['single_letter']):
        letter = random.choice(string.ascii_uppercase)
        row = random.randint(1, 1000)
        test_cases.append(letter + str(row))

    # 2. 双字母列
    for _ in range(case_types['two_letters']):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        row = random.randint(1, 1000)
        test_cases.append(letters + str(row))

    # 3. 三字母列
    for _ in range(case_types['three_letters']):
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        row = random.randint(1, 500)
        test_cases.append(letters + str(row))

    # 4. 边界测试（固定集合）
    edge_cases = [
        'A1', 'Z1', 'AA1', 'AZ1', 'ZA1', 'ZZ1',
        'A100', 'B200', 'C300',
        'A999', 'B1000', 'C1024'
    ]
    test_cases.extend(edge_cases)

    # 5. R行C列格式（反向转换测试）（固定集合）
    rc_cases = [
        'R1C1', 'R1C26', 'R1C27', 'R1C52', 'R1C53',
        'R1C702', 'R1C703', 'R1C18278',
        'R100C55', 'R500C100', 'R1000C1000'
    ]
    test_cases.extend(rc_cases)

    # 6. 随机混合
    for _ in range(case_types['random_mix']):
        if random.choice([True, False]):
            col = generate_single_col_letter(3)
            row = random.randint(1, 10000)
            test_cases.append(col + str(row))
        else:
            row = random.randint(1, 10000)
            col = random.randint(1, 20000)
            test_cases.append(f"R{row}C{col}")

    # 写入文件
    with open(output_file, 'w') as f:
        f.write(str(len(test_cases)) + '\n')
        for case in test_cases:
            f.write(case + '\n')

    return test_cases


def generate_expected_outputs(test_cases, output_file='expected_outputs.txt'):
    """生成期望输出"""
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

    with open(output_file, 'w') as f:
        for out in expected:
            f.write(out + '\n')

    return expected


def verify_results(
    test_file='test_cases.txt',
    expected_file='expected_outputs.txt',
    target_script='python_linear_0001.py'
):
    """验证测试结果"""
    with open(test_file, 'r') as f:
        lines = f.readlines()
    inputs = int(lines[0].strip())
    test_cases = [line.strip() for line in lines[1:]]

    with open(expected_file, 'r') as f:
        expected = [line.strip() for line in f.readlines()]

    with open('temp_input.txt', 'w') as f:
        f.write(str(inputs) + '\n')
        for case in test_cases:
            f.write(case + '\n')

    result = subprocess.run(
        ['python', target_script],
        input=open('temp_input.txt').read(),
        capture_output=True,
        text=True
    )

    actual = result.stdout.strip().split('\n') if result.stdout.strip() else []

    print(f"测试用例数: {inputs}")
    print(f"期望输出数: {len(expected)}")
    print(f"实际输出数: {len(actual)}")

    correct = 0
    errors = []
    for i, (exp, act) in enumerate(zip(expected, actual)):
        if exp == act:
            correct += 1
        else:
            errors.append((test_cases[i], exp, act))

    print(f"正确数: {correct}/{inputs} ({(correct / inputs * 100) if inputs else 0:.1f}%)")

    if errors:
        print("\n错误详情:")
        for inp, exp, act in errors[:10]:
            print(f"  输入: {inp}")
            print(f"  期望: {exp}")
            print(f"  实际: {act}")
            print()

    return correct == inputs


def main(n):
    """
    n 为规模（期望的大致测试用例数量），将自动按比例生成各类测试数据，
    写入 test_cases.txt 和 expected_outputs.txt，并打印简单统计信息。
    """
    test_cases = generate_test_cases(n, 'test_cases.txt')
    expected = generate_expected_outputs(test_cases, 'expected_outputs.txt')
    print(f"生成了 {len(test_cases)} 个测试用例")
    print("测试用例已保存到 test_cases.txt")
    print("期望输出已保存到 expected_outputs.txt")
    return test_cases, expected


if __name__ == "__main__":
    # 示例：直接运行时默认规模为 100
    main(100)