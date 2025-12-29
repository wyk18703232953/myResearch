import math
import random

def main(n: int):
    # 原逻辑：根据 n 计算并输出结果
    if n == 4:
        print(12)
    elif n <= 2:
        print(n)
    else:
        if n % 2 == 0:
            a = n * (n - 1) * (n - 3)
            if n % 3 == 0:
                a = a // 3
            b = n * (n - 1) * (n - 2)
            b = b // 2
            print(max(a, b, (n - 1) * (n - 2) * (n - 3)))
        else:
            print(n * (n - 1) * (n - 2))


if __name__ == "__main__":
    # 根据 n 生成测试数据，这里将 n 本身作为规模参数，
    # 也可以改为用 n 生成多个不同规模的测试用例。
    test_n = 10  # 示例：固定规模，也可改为其他值或多组测试
    main(test_n)