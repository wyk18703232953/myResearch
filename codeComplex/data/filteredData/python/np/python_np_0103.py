from math import factorial
import random

def main(n: int):
    """
    n 用作生成测试数据的长度，即 word1 和 word2 的长度。
    自动生成只包含 '+', '-' 的 word1，
    以及包含 '+', '-', '?' 的 word2。
    """
    # 生成测试数据
    # word1: 仅由 '+' 和 '-' 组成
    word1 = [random.choice(['+', '-']) for _ in range(n)]
    # word2: 由 '+', '-', '?' 组成，假设三者均匀随机
    word2 = [random.choice(['+', '-', '?']) for _ in range(n)]

    expected = 0
    for i in word1:
        if i == '+':
            expected += 1
        else:
            expected -= 1

    blank = 0
    for i in word2:
        if i == '+':
            expected -= 1
        elif i == '-':
            expected += 1
        else:
            blank += 1

    if abs(expected) > blank:
        print(float(0))
    elif blank == 0:
        if expected == 0:
            print(1)
        else:
            print(0)
    else:
        total = 2 ** blank
        if expected == blank - 1:
            print(float(0))
        else:
            f = (blank - expected) // 2
            if expected > 0:
                a, b = expected + f, f
            elif expected < 0:
                a, b = expected + f, f
            else:
                a, b = f, f
            ans = factorial(a + b) / (factorial(a))
            ans = ans / factorial(b)
            ans = ans / total
            print(ans)

if __name__ == "__main__":
    # 示例：n 可按需修改
    main(5)