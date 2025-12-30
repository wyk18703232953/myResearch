def main(n: int):
    # 根据 n 生成测试数据：这里设定 m 为 2*n 作为示例
    # 可根据需要调整生成规则
    m = 2 * n

    if n > (m + 1) / 2:
        print(m)
    else:
        print(int(m % (2 ** n)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)