import random

def main(n: int) -> None:
    # 根据 n 生成测试数据，这里原题只用到一个整数 n
    # 可以在此按需扩展更复杂的测试数据逻辑
    test_n = n if n is not None else 0

    # 原逻辑：输出 3 * n // 2
    print(3 * test_n // 2)


if __name__ == "__main__":
    # 示例：可在此处手动调用 main 进行本地测试
    # 实际使用时由外部代码调用 main(n)
    main(10)