import random

def main(n: int):
    # 根据规模 n 生成两个整数 a, b
    # 这里示例：a, b 在 [0, 2^n) 范围内随机生成
    if n <= 0:
        a = 0
        b = 0
    else:
        upper = 1 << n
        a = random.randrange(0, upper)
        b = random.randrange(0, upper)

    bitxor = a ^ b

    res = 1
    while bitxor:
        bitxor >>= 1
        res <<= 1

    # 原程序行为：输出结果
    print(res - 1)


if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要调整
    main(10)