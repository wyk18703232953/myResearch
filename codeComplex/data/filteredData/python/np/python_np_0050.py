import math
from math import factorial
import random

def combination(n, r):
    return float(factorial(n)) / float(factorial(r)) / float(factorial(n - r))

def main(n):
    # 生成目标串 a：长度为 n，每个位置随机为 '+' 或 '-'
    a = ''.join(random.choice('+-') for _ in range(n))

    # 生成当前串 b：
    # 先随机选择其中若干位置为 '?'，其余位置为 '+' 或 '-'
    b_list = []
    for _ in range(n):
        c = random.random()
        if c < 0.3:
            b_list.append('?')            # 约 30% 概率为 '?'
        else:
            b_list.append(random.choice('+-'))
    b = ''.join(b_list)

    ap = a.count('+')
    am = a.count('-')
    bp = b.count('+')
    bm = b.count('-')
    nq = b.count('?')
    x = float(ap - bp)
    y = float(am - bm)

    if (x < 0 or y < 0 or x + y != nq):
        print(0.0)
    else:
        print(combination(nq, x) / (1 << nq))

if __name__ == "__main__":
    # 示例：规模为 10，可根据需要修改
    main(10)