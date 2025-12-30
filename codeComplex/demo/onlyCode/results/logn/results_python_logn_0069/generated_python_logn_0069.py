import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里生成两个非负整数 l, r
    # 使得它们的比特长度不超过 n（可根据需求调整生成逻辑）
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)

    pop = l ^ r
    result = 1

    while result <= pop:
        result = result << 1

    print(result - 1)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)