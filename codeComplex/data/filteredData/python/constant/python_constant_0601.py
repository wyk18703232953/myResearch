def main(n: int) -> None:
    # 根据规模 n 生成测试数据，这里令 k 相对 n 变化
    # 可根据需要调整生成规则
    k = max(1, n // 3 + 1)

    a = 2 * n
    b = 5 * n
    c = 8 * n
    result = (a + k - 1) // k + (b + k - 1) // k + (c + k - 1) // k
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)