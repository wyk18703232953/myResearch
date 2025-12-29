import random

def main(n: int):
    # 根据 n 生成测试数据，这里直接使用 n 本身作为测试规模
    # 若需要更复杂数据，可在此处构造（例如数组、图等）
    result = 3 * n // 2
    print(result)

if __name__ == "__main__":
    # 示例：可修改此处以测试不同规模
    main(10)