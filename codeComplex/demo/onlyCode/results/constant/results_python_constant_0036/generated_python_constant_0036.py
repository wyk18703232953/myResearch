def main(n: int):
    # 根据规模 n 生成测试数据，这里假设原始含义是从 1 到 n 的整数中任选一个
    # 你可以根据需要调整数据生成逻辑
    test_value = n  # 简单情况下直接用 n 作为输入规模

    # 原始逻辑：n = n + n // 2，然后输出
    test_value = test_value + test_value // 2

    print(test_value)


if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)