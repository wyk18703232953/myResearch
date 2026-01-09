def main(n):
    # 根据规模 n 生成测试数据：
    # 原程序从输入中读取 n, v
    # 这里只保留 n 为参数，通过构造 v 来生成测试数据。
    # 选择一个简单的规则：若 n > 1，则 v = n // 2，否则 v = 1。
    if n > 1:
        v = n // 2

    else:
        v = 1

    if n > v:
        val = v - 1 + int(((n - v) * (n - v + 1)) / 2)
        # print(val)
        pass

    else:
        # print(n - 1)
        pass
if __name__ == "__main__":
    # 示例：可在此处调用 main 测试不同规模
    main(10)