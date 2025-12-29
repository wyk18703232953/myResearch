from math import gcd
from collections import defaultdict as dd
import random


def main(n):
    """
    n: 生成的表达式数量（规模）
    自动生成形如： (A+B)/C 的字符串表达式，
    其中 A,B,C 为正整数，并复用一些相同的 (A+B)/C 以体现计数效果。
    """
    m = n  # 保持原逻辑中的变量名含义：m 为表达式数量

    # 生成测试数据：表达式列表 strs
    strs = []
    # 为了有重复的最简分数，先生成若干基准分数，再随机扰动
    base_count = max(1, m // 5)
    bases = []
    for _ in range(base_count):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.randint(1, 20)
        bases.append((a, b, c))

    for i in range(m):
        # 随机选一个基准，然后加上一点小变化
        a, b, c = random.choice(bases)
        # 偶尔加扰动，保证分数多样同时有重复
        if random.random() < 0.7:
            aa = a
            bb = b
            cc = c
        else:
            aa = random.randint(1, 30)
            bb = random.randint(1, 30)
            cc = random.randint(1, 30)

        s = f"({aa}+{bb})/{cc}"
        strs.append(s)

    # 原始逻辑开始（去掉 input，改为使用 strs 列表）
    d = dd(int)
    l = []
    ans = []

    for idx in range(m):
        s = strs[idx].split()[0]
        a = 0
        b = 0
        c = 0
        n_len = len(s)
        ind = 0

        # 解析 A：从 s[1] 开始，直到遇到 '+'
        for i in range(1, n_len):
            if s[i] == '+':
                ind = i + 1
                break
            a = a * 10 + int(s[i])

        # 解析 B：从 ind 开始，直到遇到 ')'
        for i in range(ind, n_len):
            if s[i] == ')':
                ind1 = i + 2  # 跳过 ")/"
                break
            b = b * 10 + int(s[i])

        # 解析 C：从 ind1 开始到结尾
        for i in range(ind1, n_len):
            c = c * 10 + int(s[i])

        # 化简 (A+B)/C
        a = a + b
        g = gcd(a, c)
        a //= g
        c //= g

        d[(a, c)] += 1
        l.append((a, c))

    for frac in l:
        ans.append(d[frac])

    # 输出结果（与原程序一样：空格分隔）
    print(*ans)


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)