import random

def main(n):
    # 根据规模 n 生成测试数据，这里生成两个 [0, 2^n-1] 之间的整数
    max_val = (1 << n) - 1
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)

    a = a ^ b
    k = 0
    while a:
        k += 1
        a = a >> 1
    print(2**k - 1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)