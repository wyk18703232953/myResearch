from math import factorial
import random


def nCr(n, r):
    f = factorial
    return f(n) / f(r) / f(n - r)


def main(n):
    """
    n 为规模参数，这里用于控制生成的随机测试数据长度。
    逻辑与原程序一致：给定字符串 s1, s2，计算概率。
    """

    # 生成测试数据：
    # s1 只包含 '+' 和 '-'，长度为 n
    # s2 包含 '+', '-', '?'，长度为 n
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = ''.join(random.choice(choices_s1) for _ in range(n))
    s2 = ''.join(random.choice(choices_s2) for _ in range(n))

    s1_pos, s2_pos = s1.count('+'), s2.count('+')
    s1_neg, s2_neg = s1.count('-'), s2.count('-')
    s1_q = s2.count('?')

    ans = 0.0
    if s1_q == 0:
        if s1_pos == s2_pos:
            ans = 1.0
        else:
            ans = 0.0
    else:
        diff1 = s1_pos - s2_pos
        if diff1 > s1_q or diff1 < 0:
            ans = 0.0
        else:
            ans = nCr(s1_q, diff1) / (2 ** s1_q)

    print('{:.12f}'.format(ans))


if __name__ == "__main__":
    # 示例：n = 10
    main(10)