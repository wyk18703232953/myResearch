import math
import random

def main(n):
    # 生成测试数据：
    # s1：长度为 n，由'+'和'-'组成
    # s2：长度为 n，由'+', '-', '?'组成
    ops = ['+', '-']
    s1 = ''.join(random.choice(ops) for _ in range(n))
    ops2 = ['+', '-', '?']
    s2 = ''.join(random.choice(ops2) for _ in range(n))

    ps1 = ms1 = ps2 = ms2 = qs2 = 0

    for ch in s1:
        if ch == '+':
            ps1 += 1
        elif ch == '-':
            ms1 += 1

    for ch in s2:
        if ch == '+':
            ps2 += 1
        elif ch == '-':
            ms2 += 1
        elif ch == '?':
            qs2 += 1

    if ps2 <= ps1 and ms2 <= ms1:
        # C(qs2, ps1-ps2) * (0.5 ** qs2)
        result = (math.factorial(qs2) /
                  (math.factorial(ps1 - ps2) * math.factorial(ms1 - ms2)) *
                  (0.5 ** qs2))
        print(result)
    else:
        print(0.00000000)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)