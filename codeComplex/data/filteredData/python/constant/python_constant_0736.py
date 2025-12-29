import random

def main(n: int):
    # 生成测试数据，这里直接使用传入的 n 作为规模参数
    # 如需批量测试，可根据需要生成多个 n 的列表进行循环调用
    result = int(n ** 2 + (n - 1) ** 2)
    print(result)


if __name__ == "__main__":
    # 示例：使用 n=10 进行测试
    main(10)