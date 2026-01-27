def main(n: int):
    # 根据 n 生成测试数据，这里构造 v，使得 1 <= v < n
    # 示例策略：v = max(1, n // 2)
    v = max(1, n // 2)

    if n <= v + 1:
        result = n - 1

    else:
        b = n - v
        result = v - 1 + ((b * (b + 1)) // 2)

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)