def main(n: int) -> int:
    # 原逻辑：返回 n + n // 2
    return n + (n // 2)


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据并调用 main
    # 这里简单使用 n 自身作为测试数据
    test_n = 10  # 可以按需修改或在其他地方调用 main
    print(main(test_n))