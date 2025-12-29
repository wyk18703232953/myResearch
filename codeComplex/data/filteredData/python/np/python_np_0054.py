import math
import random

def main(n: int):
    # 生成测试数据：长度为 n 的 s1, s2
    # s1 只包含 '+' 或 '-'
    # s2 包含 '+', '-', '?' 三种
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = [random.choice(choices_s1) for _ in range(n)]
    s2 = [random.choice(choices_s2) for _ in range(n)]

    p1 = m1 = p2 = m2 = c = 0

    for i in range(len(s1)):
        if s1[i] == '+':
            p1 += 1
        if s1[i] == '-':
            m1 += 1
        if s2[i] == '+':
            p2 += 1
        if s2[i] == '-':
            m2 += 1
        if s2[i] == '?':
            c += 1

    p = abs(p1 - p2)
    m = abs(m1 - m2)

    if (p + m) == c:
        result = math.factorial(c) / (math.factorial(p) * math.factorial(m) * pow(2, c))
    else:
        result = 0.0

    print(result)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)