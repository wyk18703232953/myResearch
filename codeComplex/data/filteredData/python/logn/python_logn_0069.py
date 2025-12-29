import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里生成两个不超过 2^n 的非负整数 l 和 r
    max_val = max(1, 2 ** n - 1)
    l = random.randint(0, max_val)
    r = random.randint(0, max_val)

    pop = l ^ r
    result = 1

    while result <= pop:
        result <<= 1

    print(result - 1)


if __name__ == "__main__":
    # 示例：n = 10，可按需修改或在其他模块中调用 main(n)
    main(10)