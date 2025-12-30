def main(n: int):
    # 根据规模 n 生成测试数据，这里示例用棋盘中心位置
    # 你可以根据需要修改生成规则
    x = (n + 1) // 2
    y = (n + 1) // 2

    num = (x - 1) + (y - 1)
    num2 = (n - x) + (n - y)
    ans = num <= num2

    if ans:
        print("White")
    else:
        print("Black")


if __name__ == "__main__":
    # 示例：调用 main(8)
    main(8)