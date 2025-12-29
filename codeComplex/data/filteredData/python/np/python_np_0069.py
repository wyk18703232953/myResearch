from math import factorial
import random

def main(n: int):
    # 生成长度为 n 的原字符串 s，仅包含 '+' 和 '-'
    s = ''.join(random.choice('+-') for _ in range(n))

    # 生成长度为 n 的目标字符串 new，包含 '+', '-', '?' 三种符号
    # 为了规模和随机性，这里也使用 n 作为 new 的长度
    choices = ['+', '-', '?']
    new = ''.join(random.choice(choices) for _ in range(n))

    questions = 0
    plus = s.count('+')
    minus = s.count('-')

    for ch in new:
        if ch == '+':
            plus -= 1
        elif ch == '-':
            minus -= 1
        else:
            questions += 1

    if plus < 0 or minus < 0:
        result = 0.0
    else:
        # 计算组合数 C(questions, plus) / 2^questions
        # 若 plus + minus != questions，组合数自动为 0
        if plus + minus != questions:
            result = 0.0
        else:
            num = factorial(questions) / (factorial(plus) * factorial(minus))
            den = 2 ** questions
            result = num / den

    print("{0:.10f}".format(result))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)