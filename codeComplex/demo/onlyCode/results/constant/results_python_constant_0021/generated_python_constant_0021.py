import random

def main(n: int) -> None:
    # 生成测试数据：此题逻辑只依赖一个整数 n，本身就是规模
    # 若需要更复杂的测试数据，可在此根据 n 构造其他数据结构
    result = 3 * (n // 2)
    print(result)


if __name__ == "__main__":
    # 示例：根据规模 n 随机生成一个不超过 n 的测试输入
    # 这里将测试用的实际 n 设置为一个 1~n 的随机整数
    n = 10  # 可以根据需要修改规模
    test_n = random.randint(1, n)
    main(test_n)