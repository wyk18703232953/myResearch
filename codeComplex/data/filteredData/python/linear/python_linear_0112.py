import math

def main(n: int):
    # 根据规模 n 生成测试数据，这里直接使用 n 作为测试数据
    # 如果需要生成更多数据，可在此扩展
    result = math.ceil(n / 2) * (math.floor(n / 2) + 1)
    print(result)


if __name__ == "__main__":
    # 示例：可以在此修改 n 测试不同规模
    main(10)