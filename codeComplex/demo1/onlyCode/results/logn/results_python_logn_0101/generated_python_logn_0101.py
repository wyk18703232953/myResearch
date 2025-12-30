import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里生成两个 [0, 2^n - 1] 范围内的整数
    # 你也可以根据需要修改为其他数据生成方式
    max_val = (1 << n) - 1
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)

    x = a ^ b
    k = 0
    while x:
        k += 1
        x >>= 1
    result = (1 << k) - 1

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改
    main(10)