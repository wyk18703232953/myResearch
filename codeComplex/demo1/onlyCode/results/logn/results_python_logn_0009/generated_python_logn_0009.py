import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 a, b
    # 这里约定：a, b 在 [0, 2^n - 1] 范围内随机生成
    if n <= 0:
        a = 0
        b = 0
    else:
        upper = (1 << n) - 1
        a = random.randint(0, upper)
        b = random.randint(0, upper)

    bitxor = a ^ b

    res = 1
    while bitxor:
        bitxor >>= 1
        res <<= 1

    # 输出与原程序一致的结果
    print(res - 1)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)