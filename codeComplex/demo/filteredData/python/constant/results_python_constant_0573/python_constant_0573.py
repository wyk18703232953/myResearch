def main(n: int):
    # 根据规模 n 生成测试数据 a, b
    # 这里示例：取棋盘中间或靠中间的一个格子
    a = (n + 1) // 2
    b = (n + 1) // 2

    white = abs(a - 1) + abs(b - 1)
    black = abs(n - a) + abs(n - b)
    if white <= black:
        # print("White")
        pass

    else:
        # print("Black")
        pass
if __name__ == "__main__":
    # 示例调用：你可以根据需要修改 n
    main(8)