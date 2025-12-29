import math
import random

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def main(n):
    # 生成测试数据：
    # s1: 长度为 n，由'+'和'-'随机组成
    # s2: 长度为 n，由'+', '-', '?' 随机组成
    choices_s1 = ['+', '-']
    choices_s2 = ['+', '-', '?']

    s1 = ''.join(random.choice(choices_s1) for _ in range(n))
    s2 = ''.join(random.choice(choices_s2) for _ in range(n))

    ans = 0
    for ch in s1:
        if ch == '+':
            ans += 1
        else:
            ans -= 1

    t = 0
    qm = 0
    for ch in s2:
        if ch == '+':
            t += 1
        elif ch == '-':
            t -= 1
        else:
            qm += 1

    if qm == 0:
        if ans == t:
            print(1.000000000000)
        else:
            print(0.000000000000)
    else:
        k = ans - t
        if abs(k) == qm:
            na = 1 / pow(2, qm)
            print(na)
        elif abs(k) > qm:
            print(0.000000000000)
        else:
            if (k % 2 == 0 and qm % 2 == 1) or (k % 2 == 1 and qm % 2 == 0):
                print(0.000000000000)
            else:
                a = abs((qm + k) // 2)
                b = abs((qm - k) // 2)
                nu = factorial(qm) / (factorial(a) * factorial(b))
                ans_value = nu / pow(2, qm)
                print(ans_value)

if __name__ == "__main__":
    # 示例：规模为 5
    main(5)