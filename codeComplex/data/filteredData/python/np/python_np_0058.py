import math
import random

def main(n: int):
    """
    n: 问题规模，表示字符串 s 和 p 的长度
    自动生成测试数据 s、p，然后计算原程序的答案并返回/打印。
    """
    # 1. 生成测试数据
    # s 只包含 '+' 或 '-'
    s = ''.join(random.choice(['+', '-']) for _ in range(n))

    # p 包含 '+', '-', '?'，这里简单设定概率分布
    # 例如：'+' 40%，'-' 40%，'?' 20%
    def random_p_char():
        r = random.random()
        if r < 0.4:
            return '+'
        elif r < 0.8:
            return '-'
        else:
            return '?'

    p = ''.join(random_p_char() for _ in range(n))

    # 2. 逻辑与原程序一致
    c = 1
    ss = 0
    ps = 0
    k = 0

    for i in range(len(s)):
        if p[i] == '?':
            c *= 2
            k += 1
        if s[i] == '+':
            ss += 1
        else:
            ss -= 1
        if p[i] == '+':
            ps += 1
        elif p[i] == '-':
            ps -= 1

    y = math.fabs(ss - ps)
    x = k - y
    a = y + x / 2
    b = k - a

    if k < y:
        ans = 0.0
    else:
        ans = math.factorial(int(a + b)) / (math.factorial(int(a)) * math.factorial(int(b)))
        ans /= c

    print(f"{ans:.12f}")
    return ans

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)