import math
import random

def main(n):
    # 生成目标字符串 a：长度为 n，仅由 '+' 和 '-' 组成
    a = ''.join(random.choice(['+', '-']) for _ in range(n))
    # 生成含有不确定符号 '?' 的字符串 b：长度为 n，由 '+', '-', '?' 组成
    b = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    sa = a.count("+")
    ta = a.count("-")
    sb = b.count("+")
    tb = b.count("-")
    x = b.count("?")

    s = abs(sa - sb)
    t = abs(ta - tb)

    su = math.factorial(s + t)
    re = math.factorial(s)
    fa = math.factorial(t)
    result = su / (re * fa)

    if s + t <= x:
        print(float(result) / float(2 ** x))
    else:
        print(0.0)

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)