def main(n):
    # 生成测试数据：这里根据规模 n 构造 v
    # 示例策略：让 v 在合理范围 [0, n] 内变化，这里简单设 v = n // 2
    v = n // 2

    if v >= (n - 1):
        result = n - 1

    else:
        result = n - 1 + ((n - 1 - v) * (n - v) // 2)

    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main，使用某个规模 n
    main(10)