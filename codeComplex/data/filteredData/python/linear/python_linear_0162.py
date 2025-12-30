from math import gcd
import random


def main(n: int):
    # 随机生成 n 条形如 "(a+b)/c" 的数据，a,b,c 为正整数
    # 保证分母 c > 0
    qs = []
    d = dict()

    expressions = []
    for _ in range(n):
        # 生成 a, b, c
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        # 构造形如 "(a+b)/c" 的字符串
        s = f"({a}+{b})/{c}"
        expressions.append(s)

    # 使用原逻辑处理
    for s in expressions:
        a = int(s[1:s.index('+')])
        b = int(s[s.index('+') + 1: s.index(')')])
        c = int(s[s.index(')') + 2:])
        a = a + b
        gc = gcd(a, c)
        res = (a // gc, c // gc)
        qs.append(res)
        if res in d:
            d[res] += 1
        else:
            d[res] = 1

    for q in qs:
        print(d[q], end=' ')


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)