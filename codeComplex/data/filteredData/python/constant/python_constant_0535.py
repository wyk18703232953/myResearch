def main(n: int):
    # 根据规模 n 生成测试数据，这里构造一个简单的 s
    # 示例：令 s = n 的平方，便于测试
    s = n * n

    # 原逻辑：给定 n, s，输出 (s + n - 1) // n
    result = (s + n - 1) // n
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改 n
    main(10)