from math import factorial, pow
import random


def wifi(s1, s2):
    count1, count2, count3 = 0, 0, 0
    for i in range(len(s1)):
        if s1[i] == '+':
            count1 += 1
        elif s1[i] == '-':
            count2 += 1
        if s2[i] == "+":
            count1 -= 1
        elif s2[i] == '-':
            count2 -= 1
        else:
            count3 += 1
    if count1 < 0 or count2 < 0:
        return '{:.9f}'.format(0)
    q = factorial(count1 + count2) / (factorial(count1) * factorial(count2))
    r = q / pow(2, count3)
    return r


def main(n):
    # 生成长度为 n 的 t1：只包含 '+' 和 '-'
    t1 = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 生成长度为 n 的 t2：包含 '+', '-', '?'
    t2 = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    result = wifi(t1, t2)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数，可根据需要修改
    main(10)