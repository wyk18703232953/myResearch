from math import factorial
import random

def solve(a: str, b: str) -> float:
    plus, minus, ques = '+', '-', '?'
    ops1 = {plus: 0, minus: 0}
    ops2 = {plus: 0, minus: 0, ques: 0}

    for ai, bi in zip(a, b):
        ops1[ai] += 1
        ops2[bi] += 1

    final_pos = ops1[plus] - ops1[minus]
    initial_pos = ops2[plus] - ops2[minus]
    diff = final_pos - initial_pos
    abs_diff = abs(diff)

    if abs_diff > ops2[ques]:
        return 0.0
    if (ops2[ques] - abs_diff) % 2 != 0:
        return 0.0

    total = 2 ** ops2[ques]
    one_type = (ops2[ques] - abs_diff) // 2
    other_type = abs_diff + one_type
    numerator = factorial(ops2[ques]) / (factorial(one_type) * factorial(other_type))
    return numerator / total

def generate_test_data(n: int):
    # 生成长度为 n 的 a：只包含 '+' 和 '-'
    a = ''.join(random.choice(['+', '-']) for _ in range(n))
    # 生成长度为 n 的 b：包含 '+', '-', '?'
    b = ''.join(random.choice(['+', '-', '?']) for _ in range(n))
    return a, b

def main(n: int):
    a, b = generate_test_data(n)
    ans = solve(a, b)
    print(ans)

if __name__ == "__main__":
    # 示例：规模 n = 10，可自行修改
    main(10)