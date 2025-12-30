from math import gcd
from collections import defaultdict as dd
import random


def main(n: int):
    """
    n: 生成的表达式数量（规模）
    生成格式形如 '(a+b)/c' 的表达式，共 n 个，
    然后对每个表达式化简，看同一 (a+b)/c 结果出现了多少次。
    最后按出现顺序输出每个表达式对应的计数。
    """

    # 生成测试数据：m = n
    m = n

    # 生成 m 个表达式字符串，形如 "(a+b)/c"
    # 控制数字规模，避免超大：1 <= a,b,c <= 10*n
    expressions = []
    upper = max(1, 10 * n)
    for _ in range(m):
        a = random.randint(1, upper)
        b = random.randint(1, upper)
        c = random.randint(1, upper)
        # 保证 c != 0
        while c == 0:
            c = random.randint(1, upper)
        s = f"({a}+{b})/{c}"
        expressions.append(s)

    d = dd(int)
    l = []

    # 原逻辑：解析每个形如 "(a+b)/c" 的字符串，化简分数 (a+b)/c
    for s in expressions:
        a = 0
        b = 0
        c = 0
        n_s = len(s)
        ind = 0

        # 解析 a
        for i in range(1, n_s):
            if s[i] == '+':
                ind = i + 1
                break
            a = a * 10 + int(s[i])

        # 解析 b
        for i in range(ind, n_s):
            if s[i] == ')':
                ind1 = i + 2  # 跳过 ")/"
                break
            b = b * 10 + int(s[i])

        # 解析 c
        for i in range(ind1, n_s):
            c = c * 10 + int(s[i])

        a = a + b
        g = gcd(a, c)
        a //= g
        c //= g
        d[(a, c)] += 1
        l.append((a, c))

    # 输出结果
    for key in l:
        print(d[key], end=" ")


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)