from collections import Counter
import math
import random
import string


def main(n: int):
    # 1. 生成测试数据 i1, i2
    # 规则：
    #   - i1 和 i2 为长度为 n 的字符串
    #   - 字符集：'?', '+', '-', 以及少量字母，保证有一定随机性
    #   - 保持与原程序逻辑兼容（主要依赖 '?', '+')
    chars = ['?', '+', '-'] + list(string.ascii_lowercase[:5])
    i1 = [random.choice(chars) for _ in range(n)]
    i2 = [random.choice(chars) for _ in range(n)]

    # 可选：确保有一定数量的 '?' 和 '+'，避免长期输出为 0 的情况
    # 强制在 i1, i2 中各放入一些 '?' 和 '+'
    if n >= 2:
        i1[0] = '?'
        i2[0] = '?'
        i1[1] = '+'
        i2[1] = '+'

    # 2. 原始逻辑开始
    a = Counter(i1)
    b = Counter(i2)

    c = b - a  # Rem from b
    d = a - b  # Rem from a

    c1 = list(c.elements())
    d1 = list(d.elements())

    count = 0
    for ch in c1:
        if ch == "?":
            count += 1

    if count != len(d1):
        print(0)
    else:
        x = len(c1)
        that = 0
        for ch in d1:
            if ch == "+":
                that += 1
        out = math.factorial(x) / (math.factorial(that) * math.factorial(x - that))
        print(out / math.pow(2, x))


if __name__ == "__main__":
    # 示例：n = 10，可按需修改
    main(10)