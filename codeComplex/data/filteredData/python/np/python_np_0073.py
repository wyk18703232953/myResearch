import math
import random

def main(n: int):
    # 生成两个长度为 n 的字符串 a 和 b
    # a 只含 '+' 和 '-'，b 含 '+', '-', '?' 三种
    ops = ['+', '-']
    ops_with_q = ['+', '-', '?']
    a = ''.join(random.choice(ops) for _ in range(n))
    b = ''.join(random.choice(ops_with_q) for _ in range(n))

    x1 = a.count('+')
    y1 = a.count('-')
    x2 = b.count('+')
    y2 = b.count('-')
    l = b.count('?')

    if l == 0 and (x1 == x2 and y1 == y2):
        print(float(1))
    elif x1 > (x2 + l) or y1 > (y2 + l):
        print(float(0))
    else:
        w = math.factorial(l)
        m = math.factorial(x1 - x2)
        k = math.factorial(l - (x1 - x2))
        print((w / (m * k)) / 2 ** (x1 + y1 - x2 - y2))


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)