import random

def main(n: int):
    # 根据 n 生成测试数据，这里直接使用 n 作为原始代码中的输入
    # 如果需要更复杂的测试数据生成，可在此扩展
    value = n

    # 原始逻辑：输出 n * n + (n - 1) ** 2
    result = value * value + (value - 1) ** 2
    print(result)


if __name__ == "__main__":
    # 示例：可在此处修改 n 以进行测试
    # 例如随机生成一个规模：
    n = 10  # 或者：n = random.randint(1, 100)
    main(n)