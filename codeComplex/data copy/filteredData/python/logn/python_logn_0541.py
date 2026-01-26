def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设：n 表示“第 n 个数字”（从 1 开始计数）
    # 若需要批量测试，可自行在此生成多个 n 并循环调用 main
    n = n - 1  # 与原程序保持一致，转为 0-based

    x = 1
    y = 9
    while n > x * y:
        n -= x * y
        y *= 10
        x += 1
    a = 10 ** (x - 1)
    a += n // x
    # print(str(a)[n % x])
    pass
if __name__ == "__main__":
    # 示例：调用 main(15)，表示查询第 15 个数字
    main(15)