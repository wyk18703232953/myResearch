def main(n):
    """
    按原逻辑生成一串长度为 n 的字符串并返回。
    测试数据生成规则：k 取一个依赖 n 的值（例如 k = max(1, n // 3)）。
    """
    # 生成测试数据：根据 n 选择一个 k
    k = max(1, n // 3)

    if k == 1:
        s = "1" + "0" * (n - 1)
    else:
        tmp = "0" * ((n - k) // 2) + "1"
        s = tmp * (n // len(tmp) + 1)
        s = s[:n]
    print(s)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)