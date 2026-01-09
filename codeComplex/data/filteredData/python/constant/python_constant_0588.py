def main(n):
    # 原程序输入结构：
    # 第一行：n
    # 第二行：x y
    # 这里将 n 作为棋盘大小；x, y 作为棋盘上的坐标
    # 为了可规模化并保持确定性，生成 x, y 与 n 相关：
    # 让 x, y 在 [1, n] 内循环变化
    if n <= 0:
        return

    # 生成一个确定性的 (x, y)
    x = (n // 2) % n + 1
    y = (n // 3) % n + 1

    if n - x + n - y >= x - 1 + y - 1:
        # print("White")
        pass

    else:
        # print("Black")
        pass
if __name__ == "__main__":
    main(10)