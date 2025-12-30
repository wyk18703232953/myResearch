import math
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设生成两个 1 ~ n 之间的正整数 a, b
    a = random.randint(1, n)
    b = random.randint(1, n)

    if a % b == 0:
        print(int(a / b))
    else:
        c = 0
        while b:
            c += a // b
            temp = a
            a = b
            b = temp % b
        print(c)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数，可自行修改
    main(1000)