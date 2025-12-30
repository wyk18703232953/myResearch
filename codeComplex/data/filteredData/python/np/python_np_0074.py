import math
import random

def main(n):
    # 1. 生成规模为 n 的测试数据 a, b
    # a/b 每个位置为 '+', '-'，b 还可能有 '?'
    # 保证 a 和 b 的长度均为 n
    choices_a = ['+', '-']
    choices_b = ['+', '-', '?']

    a = ''.join(random.choice(choices_a) for _ in range(n))
    b = ''.join(random.choice(choices_b) for _ in range(n))

    # 2. 原始逻辑
    l = a.count("+") - a.count("-")
    k = b.count("?")

    if k == 0:
        if (b.count("+") - b.count("-")) == l:
            print(1)
        else:
            print(0)
    else:
        n2 = 2 ** k
        r = k
        c = []
        t = 0
        while r >= 0:
            c.append(r - t)
            t += 1
            r -= 1

        d = []
        for i in range(k + 1):
            d.append(math.factorial(k) // (math.factorial(i) * math.factorial(k - i)))

        f = b.count("+") - b.count("-")
        if l - f in c:
            print(d[c.index(l - f)] / sum(d))
        else:
            print(0)


# 示例调用
if __name__ == "__main__":
    main(5)