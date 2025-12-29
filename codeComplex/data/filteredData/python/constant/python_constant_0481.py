def main(n):
    # 根据规模 n 生成测试数据，这里示例令 k = n 的平方
    k = n * n

    # 原逻辑：输出 ceil(k / n)
    # 对于 k = n^2，结果应为 n
    result = -(-k // n)
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    main(10)