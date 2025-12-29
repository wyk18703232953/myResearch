import math
import random

def solve(str1: str, str2: str) -> float:
    value = 0
    value_2 = 0
    unknown = 0

    for x in str1:
        if x == '+':
            value += 1
        else:
            value -= 1

    for x in str2:
        if x == '+':
            value_2 += 1
        elif x == '-':
            value_2 -= 1
        else:
            unknown += 1

    plus_count = 0
    minus_count = 0
    rav = 0
    x = value - value_2

    if abs(x) <= unknown:
        if x >= 0:
            plus_count += x
            rav = unknown - plus_count
        else:
            minus_count += x
            rav = unknown - minus_count

        if plus_count == 0 and minus_count == 0 and rav == 0:
            return 1.0
        else:
            if rav % 2 == 0:
                rav = rav // 2
                plus_count += rav
                minus_count += rav
                k = max(plus_count, minus_count)
                C = math.factorial(unknown) / (math.factorial(unknown - k) * math.factorial(k))
                O = 2 ** unknown
                res = C / O
                return res
            else:
                return 0.0
    else:
        return 0.0


def generate_test_data(n: int):
    """
    根据规模 n 生成测试数据：
    - str1 长度为 n，只包含 '+' 和 '-'
    - str2 长度为 n，包含 '+', '-', '?'
    """
    # 保证 n >= 1
    n = max(1, n)

    choices_str1 = ['+', '-']
    choices_str2 = ['+', '-', '?']

    str1 = ''.join(random.choice(choices_str1) for _ in range(n))
    str2 = ''.join(random.choice(choices_str2) for _ in range(n))
    return str1, str2


def main(n: int):
    str1, str2 = generate_test_data(n)
    result = solve(str1, str2)
    # 按原程序格式输出
    print(f"{result:.12f}")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)