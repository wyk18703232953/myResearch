import math
import random

def main(n):
    # 生成测试数据：长度为 n 的 s1 和 s2
    # s1 只由 '+' 和 '-' 组成
    # s2 由 '+', '-', '?' 组成
    s1 = ''.join(random.choice(['+', '-']) for _ in range(n))
    s2 = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    if s2.count('?') == 0:
        if s1.count('+') == s2.count('+') and s1.count('-') == s2.count('-'):
            p = 1.0
        else:
            p = 0.0
    else:
        if ((s1.count('+') < s2.count('+') != 0) or
            (s1.count('-') == 0 < s2.count('-') != 0)):
            p = 0.0
        else:
            pl = s1.count('+') - s2.count('+')
            mi = s1.count('-') - s2.count('-')
            p = (math.factorial(pl + mi) /
                 math.factorial(pl) /
                 math.factorial(mi)) / (2 ** (pl + mi))

    print('%1.9f' % p)

# 示例：调用 main(10)
if __name__ == "__main__":
    main(10)