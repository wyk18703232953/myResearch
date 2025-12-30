def main(n: int):
    # 根据 n 生成测试数据，这里直接使用传入的 n 作为规模
    # 可按需要扩展，例如生成从 1 到 n 的多组测试：
    # for x in range(1, n + 1):
    #     print(2 * x * x - 2 * x + 1)
    #
    # 当前保持与原程序等价：仅对规模 n 计算一次。
    result = 2 * n * n - 2 * n + 1
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)