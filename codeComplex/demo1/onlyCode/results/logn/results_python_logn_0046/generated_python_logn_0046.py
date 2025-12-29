import random

def main(n):
    # 生成规模为 n 的测试数据：两个不超过 2^n-1 的非负整数
    if n <= 0:
        a, b = 0, 0
    else:
        a = random.randint(0, (1 << n) - 1)
        b = random.randint(0, (1 << n) - 1)

    b1 = bin(b)[2:]
    a1 = bin(a)[2:]
    if len(a1) == len(b1):
        d = (b ^ a)
        v = d.bit_length()
        print(int("0" + "1" * v, 2))
    else:
        print(int("1" * len(b1), 2))


if __name__ == "__main__":
    # 示例：可以在这里指定规模 n
    main(10)