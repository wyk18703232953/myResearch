def main(n):
    # 原程序输入结构：
    # 第一行：单个整数 n（已由 main 的参数提供）
    # 第二行：两个整数 x, y
    # 将 n 作为棋盘大小，同时确定性生成 x, y 作为棋盘上的一个点
    # 这里选择 x, y 在 [1, n] 范围内，且有简单确定性关系
    if n <= 0:
        return

    # 确定性生成 x, y
    x = n // 2 + 1 if n > 1 else 1
    y = (n // 3 + 1) if n > 2 else 1
    x = min(x, n)
    y = min(y, n)

    d1 = abs(x - 1) + abs(y - 1)
    d2 = abs(n - x) + abs(n - y)

    result = "White" if d1 <= d2 else "Black"
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行时间复杂度实验
    main(10)