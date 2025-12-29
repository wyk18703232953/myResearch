from math import factorial
import random

def main(n):
    # 生成测试数据：长度为 n 的 s1, s2
    # s1 只含 '+' 或 '-'；s2 含 '+', '-', '?' 三种
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = ''.join(random.choice(choices_s1) for _ in range(n))
    s2 = ''.join(random.choice(choices_s2) for _ in range(n))

    p = 0
    m = 0
    blank = 0
    for i in range(len(s1)):
        if s1[i] == "+":
            p += 1
        else:
            m += 1
        if s2[i] == "+":
            p -= 1
        elif s2[i] == "-":
            m -= 1
        else:
            blank += 1

    if m < 0 or p < 0:
        print(0)
    else:
        if m == 0:
            print(0.5 ** p)
        elif p == 0:
            print(0.5 ** m)
        else:
            b = blank
            print((factorial(b) / factorial(p) / factorial(m)) * (0.5 ** b))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)