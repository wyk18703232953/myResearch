import math
from math import factorial
import random

def combination(n, r):
    return float(factorial(n)) / float(factorial(r)) / float(factorial(n - int(r)))

def main(n):
    # 生成测试数据：
    # a: 由'+'和'-'组成，长度为n
    # b: 在a的基础上，随机将部分位置替换为'?'
    #    保证至少存在一种方式使得b可以还原成a
    chars = ['+', '-']
    a_list = [random.choice(chars) for _ in range(n)]
    a = ''.join(a_list)

    b_list = []
    for ch in a_list:
        # 以一定概率替换为'?'
        if random.random() < 0.5:
            b_list.append('?')
        else:
            b_list.append(ch)
    b = ''.join(b_list)

    # 保持原始逻辑
    ap = a.count('+')
    am = a.count('-')
    bp = b.count('+')
    bm = b.count('-')
    qn = b.count('?')  # 问号数量
    x = float(ap - bp)
    y = float(am - bm)

    if x < 0 or y < 0 or x + y != qn:
        print(0.0)
    else:
        print(combination(qn, x) / (1 << qn))

if __name__ == "__main__":
    # 示例：n 为规模，可按需修改或在外部调用 main(n)
    main(10)