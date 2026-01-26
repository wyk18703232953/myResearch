def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里示例：在棋盘中心附近取一个点 (x, y)
    x = (n + 1) // 2
    y = (n + 1) // 2

    # 原逻辑
    if abs(x - 1) + abs(y - 1) <= abs(x - n) + abs(y - n):
        # print('White')
        pass

    else:
        # print('Black')
        pass
if __name__ == "__main__":
    # 示例：调用 main(8)，实际使用时可在外部根据需要调用 main(n)
    main(8)