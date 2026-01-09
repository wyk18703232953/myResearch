def main(n: int):
    # 根据 n 生成测试数据
    # 这里我们让 m 随 n 变化，例如 m = 3 * 2**n + 5
    m = 3 * (2 ** n) + 5

    # 输出 m % 2**n
    # print(m % (2 ** n))
    pass
if __name__ == "__main__":
    # 示例：调用 main，n 可根据需要修改
    main(5)