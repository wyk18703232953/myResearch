from math import gcd
from collections import defaultdict as dd

def generate_input(n):
    # n 作为表达式数量 m
    m = max(1, n)
    expressions = []
    for i in range(m):
        # 构造三个正整数 a, b, c
        a = i + 1
        b = (i * 2) + 3
        c = (i + 2) * 3
        # 保证 c 不为 0
        if c == 0:
            c = 1
        s = f"({a}+{b})/{c}"
        expressions.append(s)
    return m, expressions

def core_logic(m, expressions):
    d = dd(int)
    l = []
    for idx in range(m):
        s = expressions[idx]
        a = 0
        b = 0
        c = 0
        n = len(s)
        ind = 0
        for i in range(1, n):
            if s[i] == '+':
                ind = i + 1
                break
            a = a * 10 + int(s[i])
        for i in range(ind, n):
            if s[i] == ')':
                ind1 = i + 2
                break
            b = b * 10 + int(s[i])
        for i in range(ind1, n):
            c = c * 10 + int(s[i])
        a = a + b
        g = gcd(a, c)
        a = a // g
        c = c // g
        d[(a, c)] += 1
        l.append((a, c))
    output = []
    for frac in l:
        output.append(str(d[frac]))
    return " ".join(output)

def main(n):
    m, expressions = generate_input(n)
    result = core_logic(m, expressions)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)