import math
import random

def solve(s1: str, s2: str) -> float:
    plus, minus = s1.count('+'), s1.count('-')
    pre_plus = s2.count('+')
    pre_minus = s2.count('-')

    req_plus = plus - pre_plus
    req_minus = minus - pre_minus

    if req_minus < 0 or req_plus < 0:
        return 0.0

    unknowns = len(s1) - (pre_minus + pre_plus)
    if unknowns == 0:
        return 1.0

    den = 2 ** unknowns
    num = math.factorial(unknowns) / (
        math.factorial(req_plus) * math.factorial(req_minus)
    )
    return num / den


def gen_test_case(n: int):
    # 目标串 s1：长度 n，由 '+' 和 '-' 随机组成
    s1 = ''.join(random.choice('+-') for _ in range(n))

    # 根据 s1 生成 s2：将若干位置替换为 '?'
    # 控制未知数比例（这里大约 1/3 为 '?'）
    s2_list = list(s1)
    for i in range(n):
        if random.random() < 1/3:
            s2_list[i] = '?'
    s2 = ''.join(s2_list)
    return s1, s2


def main(n: int):
    s1, s2 = gen_test_case(n)
    ans = solve(s1, s2)
    # 模拟原程序的输出格式（保留 12 位小数）
    print(f"{ans:.12f}")


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)