import random

def main(n: int):
    # 根据 n 生成测试数据，这里简单地用 n 自身作为数据规模
    # 如需更复杂的测试数据，可以在此处扩展
    result = int(3 * n / 2)
    print(result)

if __name__ == "__main__":
    # 示例：自动生成一个测试规模并调用 main
    # 你也可以直接调用 main(10) 之类的形式进行测试
    test_n = random.randint(1, 100)
    main(test_n)