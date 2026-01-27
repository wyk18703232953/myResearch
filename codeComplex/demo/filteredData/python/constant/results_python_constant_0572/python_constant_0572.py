def main(n):
    # 原程序输入结构：
    # n: 棋盘大小
    # x, y: 棋盘上的位置
    #
    # 这里将规模 n 同时作为棋盘大小，并确定性构造 (x, y)
    # 使用简单的算术映射：x = n // 2 + 1, y = n // 3 + 1 ，并限制在 [1, n]
    if n <= 0:
        return

    board_size = n
    x = n // 2 + 1
    y = n // 3 + 1
    if x > board_size:
        x = board_size
    if y > board_size:
        y = board_size

    white = max(x - 1, y - 1)
    black = max(board_size - x, board_size - y)
    result = "White" if white <= black else "Black"
    # print(result)
    pass
if __name__ == "__main__":
    main(10)