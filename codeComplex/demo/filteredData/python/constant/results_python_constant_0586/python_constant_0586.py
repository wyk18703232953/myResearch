def main(n):
    # 根据题意，原始输入结构为：
    # n: 单个整数
    # x, y: 单行两个整数
    #
    # 将规模 n 映射为棋盘大小，同时确定性生成 x, y
    # 保证 1 <= x, y <= n 且确定性
    if n <= 0:
        return

    x = (n // 2) + 1
    if x > n:
        x = n
    y = (n // 3) + 1
    if y > n:
        y = n

    val1 = max(x, y) - 1
    val2 = n - min(x, y)
    if val1 <= val2:
        # print('White')
        pass

    else:
        # print('Black')
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 以进行规模化实验
    main(10)