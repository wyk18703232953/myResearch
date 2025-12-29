from math import factorial
import random


def C(k, n):
    if k < 0 or k > n:
        return 0
    return factorial(n) // factorial(k) // factorial(n - k)


def generate_test_data(n):
    """
    根据规模 n 生成 s1, s2：
    - s1 只包含 '+' 和 '-'，长度为 n
    - s2 只包含 '+', '-', '?'，长度为 n
    """
    # 生成 s1：随机 '+' 和 '-'
    s1 = ''.join(random.choice(['+', '-']) for _ in range(n))

    # 生成 s2：
    # 为了避免总是概率为 0 的情况，适当控制 '+' 的数量
    s2_chars = []
    for _ in range(n):
        s2_chars.append(random.choice(['+', '-', '?']))
    s2 = ''.join(s2_chars)

    return s1, s2


def main(n):
    s1, s2 = generate_test_data(n)

    n1 = s1.count('+')
    n2 = s2.count('+')
    n3 = s2.count('?')

    if n2 > n1:
        result = 0.0
    else:
        result = C(n1 - n2, n3) / (2 ** n3) if n3 >= 0 else 0.0

    # 输出与原程序行为一致：只打印结果
    print(result)


if __name__ == "__main__":
    # 可在此修改 n 进行测试
    main(10)